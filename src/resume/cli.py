import argparse
from .resume import markdownResume

def get_parser():
    formatter_class = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=formatter_class)
    subparsers = parser.add_subparsers(dest='command', required=True)

    p1 = subparsers.add_parser("make", help="make pdf and html from markdown")
    p1.add_argument('--input', type=str, default='resume.md', help='input markdown file')
    p1.add_argument('--html', type=str, default='index.html', help='output html file')
    p1.add_argument('--pdf', type=str, default='Resume_HanSun.pdf', help='output pdf file')
    p1.add_argument('--chrome', type=str, default='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', help='Path to Chrome executable')
    p1.add_argument('--css', type=str, default='resume.css', help='Path to CSS file, using the one in the static folder by default')
    p2 = subparsers.add_parser("push", help="push the directory to github, internal use only")
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    if args.command == 'make':
        md = markdownResume(input_markdown=args.input, output_html=args.html, output_pdf=args.pdf, chrome=args.chrome)
        md.make_html()
        md.html_to_pdf()

    elif args.command == 'push':
        md = markdownResume()
        md.push_to_github()

if __name__ == '__main__':
    main()
