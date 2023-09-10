from __future__ import annotations

import argparse
from pathlib import Path

from checksum import HashTypes, hash_new_checksum, compare_checksums


class TermColors:
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"


parser = argparse.ArgumentParser(prog="Check Sum", description="Check sum a file against a known checksum")

parser.add_argument(
    "file",
    action="store",
    type=Path,
    help="File that you wish to run a checksum against",
)

parser.add_argument(
    "expected_result",
    nargs="?",
    default=None,
    action="store",
    help="OPTIONAL: Paste in the check sum you expect",
)

parser.add_argument(
    "-t",
    "--type",
    nargs="?",
    default="sha256",
    type=str,
    choices=[hash_type.name for hash_type in HashTypes],
    metavar="Hash type",
    help="Choose the checksum that you would like to use: [ %(choices)s ]",
)

args = parser.parse_args()


def main(
    file: Path,
    expected_result: str | Path | None,
    hash_type: str = "sha256",
):
    if expected_result is None:
        result = (
            f"Checksum for {file.name} is: \n {TermColors.OKCYAN}{hash_new_checksum(file, hash_type)}{TermColors.ENDC}"
        )
    elif compare_checksums(file, expected_result, hash_type):
        result = f"Checksum results: {TermColors.OKGREEN}PASS{TermColors.ENDC}"
    else:
        result = f"Checksum results: {TermColors.FAIL}FAIL{TermColors.ENDC}"
    print(result)


if __name__ == "__main__":
    main(args.file, args.expected_result, args.type)
