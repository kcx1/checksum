from __future__ import annotations

import hashlib
import sys
from enum import Enum
from io import BytesIO
from pathlib import Path


class HashTypes(Enum):
    SHA1 = hashlib.sha1
    SHA224 = hashlib.sha224
    SHA256 = hashlib.sha256
    SHA384 = hashlib.sha384
    SHA512 = hashlib.sha512
    BLAKE2B = hashlib.blake2b
    BLAKE2S = hashlib.blake2s
    MD5 = hashlib.md5


def hash_new_checksum(file: Path, hash_type: str = "sha256") -> str:
    try:
        with open(file, "rb") as _file:
            digest = hashlib.file_digest(BytesIO(_file.read()), HashTypes[hash_type.upper()].value)
            return digest.hexdigest()
    except FileNotFoundError as err:
        sys.exit(f"ERROR: {err.strerror}\t{err.filename}")


def compare_checksums(file: Path, expected_result: str | Path, hash_type: str = "sha256") -> bool:
    if Path(expected_result).exists():
        with open(expected_result, "r", encoding="utf-8") as _file:
            expected_result = _file.read()
    return hash_new_checksum(file, hash_type) == expected_result
