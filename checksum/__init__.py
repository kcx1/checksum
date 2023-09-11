from __future__ import annotations

import hashlib
import sys
from enum import Enum
from io import BytesIO
from pathlib import Path


class HashTypes(Enum):
    sha1 = hashlib.sha1
    sha224 = hashlib.sha224
    sha256 = hashlib.sha256
    sha384 = hashlib.sha384
    sha512 = hashlib.sha512
    blake2b = hashlib.blake2b
    blake2s = hashlib.blake2s
    md5 = hashlib.md5


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
