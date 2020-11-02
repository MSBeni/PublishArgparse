import argparse
import sys

from ManagingTweets.Adding_Simple import AddingSimple


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--counttill100', required=False, action='store_true', help='Print count till 100')

    return parser


def main(argv=None):
    """
    :desc: Entry point method
    """
    if argv is None:
        argv = sys.argv

    try:
        parser = create_parser()
        args = parser.parse_args(argv[1:])

        # Arguments initialization
        counttill100 = args.counttill100

        # Parser check
        if counttill100:
            print(AddingSimple().print_till100())
            # counttill100fun()

    except KeyboardInterrupt:
        print('\nGood Bye.')

    return 0


def counttill100fun():
    for i in range(1, 101):
        print(i)


if __name__ == '__main__':
    sys.exit(main(sys.argv))

