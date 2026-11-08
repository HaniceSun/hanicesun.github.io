#!/usr/bin/env python
import os
import re
import shutil
import subprocess
import tempfile
from html import escape
from importlib import resources

import markdown

DEFAULT_CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

CHROME_CANDIDATES = [
    DEFAULT_CHROME,
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
    '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
    'google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser', 'chrome', 'msedge',
]

PDF_ICON = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/></svg>'
)


class MarkdownResume:
    def __init__(self, input_markdown='resume.md', output_html='index.html', output_pdf='Resume_HanSun.pdf',
                 chrome=DEFAULT_CHROME, css='resume.css', pdf_link=True):

        self.prefix = input_markdown.split('.md')[0]

        try:
            with open(input_markdown, encoding='utf-8') as f:
                self.md = f.read()
        except FileNotFoundError:
            print(f"Error: could not find markdown file {input_markdown}")
            self.md = ""

        if not os.path.exists(css):
            css = str(resources.files("resume") / "static" / css)
        try:
            with open(css, encoding='utf-8') as f:
                self.css = f.read()
        except FileNotFoundError:
            print(f"Warning: could not find CSS file {css}")
            self.css = ""

        self.chrome = chrome
        self.output_html = output_html
        self.output_pdf = output_pdf
        self.pdf_link = pdf_link
        self.title = ''
        self.html = ''

        self.preamble = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
{css}
</style>
</head>
<body>
{pdf_link}<main id="resume">
"""

        self.postamble = """
</main>
</body>
</html>
"""

    def make_html(self):
        self._get_title()

        body = markdown.markdown(self.md, extensions=["smarty", "attr_list", "sane_lists"])
        body = self._structure(body)

        self.html = self.preamble.format(
            title=escape(self.title), css=self.css, pdf_link=self._pdf_link_html()
        ) + body + self.postamble

        if self.output_html:
            with open(self.output_html, 'w', encoding='utf-8') as outfile:
                outfile.write(self.html)
            print(f"Wrote {self.output_html}")

    def html_to_pdf(self):
        if not self.html:
            self.make_html()

        chrome = self._find_chrome()
        if chrome is None:
            print(f"Error: could not find Chrome/Chromium (tried {self.chrome}); use --chrome to set its path")
            return

        # Print from a temporary file rather than a data: URL so that large
        # documents work and web fonts can load before printing.
        with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8') as tmp:
            tmp.write(self.html)
            tmp_path = tmp.name

        options = [
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--print-to-pdf-no-header",
            "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=10000",
        ]
        try:
            sp = subprocess.run(
                [chrome, *options, f"--print-to-pdf={os.path.abspath(self.output_pdf)}", f"file://{tmp_path}"],
                timeout=60, capture_output=True,
            )
            if sp.returncode == 0 and os.path.exists(self.output_pdf):
                print(f"Wrote {self.output_pdf}")
            else:
                print("Error generating PDF:", sp.stderr.decode(errors='ignore')[-500:])
        except Exception as e:
            print("Error generating PDF:", e)
        finally:
            os.remove(tmp_path)

    def push_to_github(self):
        subprocess.run('git add .; git commit -m hanice; git push -u origin main', shell=True)

    # ------------------------------------------------------------------ helpers

    def _get_title(self):
        """
        Use the contents of the first markdown heading as the document title.
        """
        for line in self.md.splitlines():
            if line.startswith("#"):
                self.title = re.sub(r'<[^>]+>', '', line.strip("#")).strip()
                return
        raise ValueError("Cannot find any lines that look like markdown headings")

    def _pdf_link_html(self):
        if not (self.pdf_link and self.output_pdf and self.output_html):
            return ''
        html_dir = os.path.dirname(os.path.abspath(self.output_html))
        href = os.path.relpath(os.path.abspath(self.output_pdf), html_dir)
        return f'<a class="pdf-link" href="{escape(href)}" download>{PDF_ICON}PDF</a>\n'

    @staticmethod
    def _structure(body):
        """
        Wrap the flat markdown output in semantic containers so the CSS can
        style it and keep entries together across PDF page breaks:

            <header>  h1 + the contact list right after it
            <section class="section">  each h2 and everything until the next h2
            <div class="entry">  each h3 and everything until the next h3/h2
        """
        # header: first h1 plus an immediately following list
        m = re.search(r'<h1[^>]*>.*?</h1>\s*(<ul>.*?</ul>)?', body, flags=re.S)
        if m:
            body = body[:m.start()] + '<header>\n' + m.group(0).strip() + '\n</header>' + body[m.end():]

        # split on top-level h2 / h3 (markdown puts block tags at line start)
        parts = re.split(r'(?m)^(?=<h[23][\s>])', body)
        out = []
        in_section = in_entry = False
        for part in parts:
            if part.startswith('<h2'):
                if in_entry:
                    out.append('</div>\n')
                    in_entry = False
                if in_section:
                    out.append('</section>\n')
                out.append('<section class="section">\n')
                in_section = True
            elif part.startswith('<h3'):
                if in_entry:
                    out.append('</div>\n')
                out.append('<div class="entry">\n')
                in_entry = True
            out.append(part)
        if in_entry:
            out.append('</div>\n')
        if in_section:
            out.append('</section>\n')
        return ''.join(out)

    def _find_chrome(self):
        for candidate in [self.chrome, *CHROME_CANDIDATES]:
            if not candidate:
                continue
            if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
                return candidate
            found = shutil.which(candidate)
            if found:
                return found
        return None


if __name__ == "__main__":
    mr = MarkdownResume()
    mr.make_html()
    mr.html_to_pdf()
