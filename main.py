from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path
from io import BytesIO
from enum import Enum


class TermColors:
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"


class HashTypes(Enum):
    sha1 = hashlib.sha1
    sha224 = hashlib.sha224
    sha256 = hashlib.sha256
    sha384 = hashlib.sha384
    sha512 = hashlib.sha512
    blake2b = hashlib.blake2b
    blake2s = hashlib.blake2s
    md5 = hashlib.md5


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


def hash_new_checksum(file: Path, hash_type: str = "sha256") -> str:
    try:
        with open(file, "rb") as f:
            digest = hashlib.file_digest(BytesIO(f.read()), HashTypes[hash_type].value)
            return digest.hexdigest()
    except FileNotFoundError as e:
        sys.exit(f"ERROR: {e.strerror}\t{e.filename}")


def compare_checksums(file: Path, expected_result: str | Path, hash_type: str = "sha256") -> bool:
    if Path(expected_result).exists():
        with open(expected_result, "r") as f:
            expected_result = f.read()
    return hash_new_checksum(file, hash_type) == expected_result


def _print_to_terminal(
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
    _print_to_terminal(args.file, args.expected_result, args.type)
