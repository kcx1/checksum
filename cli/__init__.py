from __future__ import annotations

import argparse
from pathlib import Path

from checksum import HashTypes, compare_checksums, hash_new_checksum


class TermColors:
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    END = "\033[0m"


parser = argparse.ArgumentParser(prog="Check Sum", description="Check sum a file against a known Checksum")

parser.add_argument(
    "file",
    action="store",
    type=Path,
    help="File that you wish to run a Checksum against",
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
    help="Choose the Checksum that you would like to use: [ %(choices)s ]",
)

args = parser.parse_args()


def main(
    file: Path,
    expected_result: str | Path | None,
    hash_type: str = "sha256",
):
    if expected_result is None:
        result = (
            f"Checksum for {file.name} is: \n {TermColors.CYAN}{hash_new_checksum(file, hash_type)}{TermColors.END}"
        )
    elif compare_checksums(file, expected_result, hash_type):
        result = f"Checksum results: {TermColors.GREEN}PASS{TermColors.END}"
    else:
        result = f"Checksum results: {TermColors.RED}FAIL{TermColors.END}"
    print(result)


def entry_point():
    main(args.file, args.expected_result, args.type)
