import argparse
import os
from .resume import MarkdownResume

def get_parser():
    formatter_class = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=formatter_class)
    subparsers = parser.add_subparsers(dest='command', required=True)

    p1 = subparsers.add_parser("resume", help="make pdf and html resume from markdown")
    p1.add_argument('--md', type=str, default='resume.md', help='input markdown file')
    p1.add_argument('--html', type=str, default='index.html', help='output html file')
    p1.add_argument('--pdf', type=str, default='Resume_HanSun.pdf', help='output pdf file')
    p1.add_argument('--chrome', type=str, default='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', help='Path to Chrome executable')
    p1.add_argument('--css', type=str, default='resume.css', help='Path to CSS file, using the one in the static folder by default')

    p2 = subparsers.add_parser("letter", help="make pdf and html cover letter from markdown")
    p2.add_argument('--md', type=str, default='cover_letter.md', help='input markdown file')
    p2.add_argument('--html', type=str, default='cover_letter.html', help='output html file')
    p2.add_argument('--pdf', type=str, default='cover_letter.pdf', help='output pdf file')
    p2.add_argument('--chrome', type=str, default='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', help='Path to Chrome executable')
    p2.add_argument('--css', type=str, default='resume.css', help='Path to CSS file, using the one in the static folder by default')

    p3 = subparsers.add_parser("push", help="push the directory to github, internal use only")
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    if args.command == 'resume':
        mr = MarkdownResume(input_markdown=args.md, output_html=args.html, output_pdf=args.pdf, chrome=args.chrome)
        mr.make_html()
        mr.html_to_pdf()

    elif args.command == 'letter':
        input_markdown = args.md
        output_html = input_markdown.replace('.md', '.html')
        output_pdf = input_markdown.replace('.md', '.pdf')
        mr = MarkdownResume(input_markdown=input_markdown, output_html=output_html, output_pdf=output_pdf, chrome=args.chrome)
        mr.make_html()
        mr.html_to_pdf()
        try:
            os.remove(output_html)
        except OSError:
            pass

    elif args.command == 'push':
        mr = MarkdownResume()
        mr.push_to_github()

if __name__ == '__main__':
    main()
