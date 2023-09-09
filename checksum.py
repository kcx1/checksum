import argparse
import pathlib
import hashlib
import sys
from io import BytesIO
from enum import Enum


class TermColors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


class HashTypes(Enum):
    sha1 = hashlib.sha1
    sha224 = hashlib.sha224
    sha256 = hashlib.sha256
    sha384 = hashlib.sha384
    sha512 = hashlib.sha512
    blake2b = hashlib.blake2b
    blake2s = hashlib.blake2s
    md5 = hashlib.md5


parser = argparse.ArgumentParser(
    prog="Check Sum", description="Check sum a file against a known checksum"
)

parser.add_argument(
    "file",
    action="store",
    type=pathlib.Path,
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


def run_checksum() -> str:
    try:
        with open(args.file, "rb") as f:
            digest = hashlib.file_digest(BytesIO(f.read()), HashTypes[args.type].value)
            return digest.hexdigest()
    except FileNotFoundError as e:
        sys.exit(f"ERROR: {e.strerror}\t{e.filename}")


def get_checksum() -> str | None:
    if args.expected_result is None:
        return run_checksum()


def compare_checksums() -> bool:
    if pathlib.Path(args.expected_result).exists():
        with open(args.expected_result, "r") as f:
            args.expected_result = f.read()
    return run_checksum() == args.expected_result


def print_to_terminal():
    if get_checksum():
        result = f"Checksum for {args.file.name} is: \n {TermColors.OKCYAN}{get_checksum()}{TermColors.ENDC}"
    elif compare_checksums():
        result = f"Checksum results: {TermColors.OKGREEN}PASS{TermColors.ENDC}"
    else:
        result = f"Checksum results: {TermColors.FAIL}FAIL{TermColors.ENDC}"
    print(result)


if __name__ == "__main__":
    print_to_terminal()
