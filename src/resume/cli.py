import argparse
import os
from .resume import MarkdownResume, DEFAULT_CHROME


def get_parser():
    parser = argparse.ArgumentParser(
        prog='mdcv',
        description='Make html/pdf resumes and cover letters from markdown. '
                    'With no --resume/--letter option, builds the resume from resume.md.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    g1 = parser.add_argument_group('resume')
    g1.add_argument('--resume', nargs='?', const='resume.md', metavar='MD',
                    help='build html and pdf resume from this markdown file (resume.md if no file given)')
    g1.add_argument('--html', type=str, default='index.html', help='output html file for the resume')
    g1.add_argument('--pdf', type=str, default='Resume_HanSun.pdf', help='output pdf file for the resume')
    g1.add_argument('--no-pdf-link', action='store_true', help='do not add a "download PDF" button to the html page')

    g2 = parser.add_argument_group('cover letter')
    g2.add_argument('--letter', nargs='?', const='cover_letter.md', metavar='MD',
                    help='build pdf cover letter from this markdown file (cover_letter.md if no file given)')
    g2.add_argument('--letter-pdf', type=str, default=None,
                    help='output pdf file for the cover letter; if omitted, the markdown name with .pdf')

    g3 = parser.add_argument_group('shared')
    g3.add_argument('--chrome', type=str, default=DEFAULT_CHROME, help='path to Chrome executable')
    g3.add_argument('--css', type=str, default='resume.css',
                    help='path to CSS file, using the one in the static folder by default')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    if args.resume is None and args.letter is None:
        args.resume = 'resume.md'

    if args.resume:
        mr = MarkdownResume(input_markdown=args.resume, output_html=args.html, output_pdf=args.pdf,
                            chrome=args.chrome, css=args.css, pdf_link=not args.no_pdf_link)
        mr.make_html()
        mr.html_to_pdf()

    if args.letter:
        output_pdf = args.letter_pdf or os.path.splitext(args.letter)[0] + '.pdf'
        mr = MarkdownResume(input_markdown=args.letter, output_html=None, output_pdf=output_pdf,
                            chrome=args.chrome, css=args.css, pdf_link=False)
        mr.make_html()
        mr.html_to_pdf()


if __name__ == '__main__':
    main()
