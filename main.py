import argparse
from dateutil.parser import parse
import pandas as pd

import sys


def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True

    Source: https://stackoverflow.com/questions/25341945/check-if-string-has-date-any-format
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file_name", help="File name of highlights to convert with its suffix"
    )
    parser.add_argument(
        "-t", "--title", nargs="?", const="arg_was_not_given", help="Name of the book"
    )
    parser.add_argument(
        "-a",
        "--author",
        nargs="?",
        const="arg_was_not_given",
        help="Name of the author(s)",
    )
    args = parser.parse_args()

    if args.title == "arg_was_not_given":
        print("Please provide the title information")
    elif args.title is None:
        print("Please provide provide the title using -t argument")
        sys.exit()

    if args.author == "arg_was_not_given":
        print("Please provide the author information")
    elif args.author is None:
        print("Please provide the author using -a argument")
        sys.exit()

    return args


def get_contents(file_name):
    blocks = list()
    with open(file_name, "r") as f:
        # (highlights, notes, time)
        block = list()
        for line in f:
            if line == "\n":
                continue
            info = line.rstrip("\n")
            # info = line

            if is_date(info, fuzzy=False):
                if len(block) == 1:
                    block.append("")

                dt = parse(info.rstrip("."))
                block.append(dt.strftime("%Y-%m-%d 17:00:00"))
                blocks.append(block)
                block = list()
                continue
            block.append(info)
    return blocks


if __name__ == "__main__":
    args = get_args()
    file_name = args.file_name
    blocks = get_contents(file_name)
    df = pd.DataFrame(blocks, columns=["Highlight", "Note", "Date"])
    df["Title"] = args.title
    df["Author"] = args.author
    df = df[["Highlight", "Title", "Author", "Note","Date"]]
    df.to_csv("highlights.csv", index=False)
