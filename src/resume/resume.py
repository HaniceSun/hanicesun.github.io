#!/usr/bin/env python
import os
import subprocess
import markdown
import base64
from importlib import resources

class MarkdownResume:
    def __init__(self, input_markdown='resume.md', output_html='index.html', output_pdf='Resume_HanSun.pdf', chrome='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', css='resume.css'):

        self.prefix = input_markdown.split('.md')[0]

        try:
            with open(input_markdown) as f:
                self.md = f.read()
        except FileNotFoundError:
            print(f"Error: could not find markdown file {input_markdown}")
            self.md = ""

        if not os.path.exists(css):
            css = f'{resources.files("resume")}/static/{css}'
        try:
            with open(css) as f:
                self.css = f.read()
        except FileNotFoundError:
            print(f"Warning: could not find CSS file {css}")
            self.css = ""

        self.chrome = chrome
        self.output_html = output_html
        self.output_pdf = output_pdf

        self.preamble = """ \
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>
        {css}
        </style>
        </head>
        <body>
        <div id="resume">
        """

        self.postamble = """ \
        </div>
        </body>
        </html>
        """

    def make_html(self):

        self._get_title()

        self.html = ''.join(
                (
                    self.preamble.format(title=self.title, css=self.css),
                    markdown.markdown(self.md, extensions=["smarty"]),
                    self.postamble,
                    )
                )

        if self.output_html:
            with open(self.output_html, 'w') as outfile:
                outfile.write(self.html + '\n')
        print(f"Wrote {self.output_html}")

    def html_to_pdf(self):
        html64 = base64.b64encode(self.html.encode("utf-8"))
        options = [
                "--headless",
                "--no-pdf-header-footer",
                "--disable-gpu",
                ]

        try:
            sp = subprocess.run(
                    [
                        self.chrome,
                        *options,
                        f"--print-to-pdf={self.output_pdf}",
                        "data:text/html;base64," + html64.decode("utf-8"),
                        ], timeout=3, capture_output=True
                    )
            if sp.returncode == 0:
                print(f"Wrote {self.output_pdf}")
        except Exception as e:
            print("Error generating PDF:", e)

    def push_to_github(self):
        subprocess.run(f'git add .; git commit -m hanice; git push -u origin main', shell=True)

    def _get_title(self):
        """
        Return the contents of the first markdown heading in md, which we
        assume to be the title of the document.
        """
        for line in self.md.splitlines():
            if line[0] == "#":
                self.title = line.strip("#").strip()
                return
        raise ValueError("Cannot find any lines that look like markdown headings")


if __name__ == "__main__":
    mr = MarkdownResume()
    mr.make_html()
    mr.html_to_pdf()
    mr.push_to_github()
