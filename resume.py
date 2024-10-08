#!/usr/bin/env python
import subprocess
import markdown
import base64

class markdownResume:
    def __init__(self, prefix='resume', html_output='index.html', pdf_output='Resume_HanSun.pdf'):

        self.prefix = prefix
        self.md = open(f'{self.prefix}.md').read()
        self.css = open(f'static/resume.css').read()
        self.chrome = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

        self.html_output = html_output
        self.pdf_output = pdf_output

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

        if self.html_output:
            with open(f'{self.html_output}', 'w') as ouFile:
                ouFile.write(self.html + '\n')

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
                        f"--print-to-pdf={self.pdf_output}",
                        "data:text/html;base64," + html64.decode("utf-8"),
                        ], timeout=3, capture_output=True
                    )
        except:
            pass

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

    def push_to_github(self):
        subprocess.call(f'git add .; git commit -m hanice; git push origin master', shell=True)


if __name__ == "__main__":
    mdresume = markdownResume()
    mdresume.make_html()
    mdresume.html_to_pdf()
    mdresume.push_to_github()

    mdresume = markdownResume(prefix='resumeCN', html_output='', pdf_output='ResumeCN_HanSun.pdf')
    mdresume.make_html()
    mdresume.html_to_pdf()
    mdresume.push_to_github()


