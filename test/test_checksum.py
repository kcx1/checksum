from cli import hash_new_checksum, compare_checksums

correct_sha256 = "535c978e5d26ead85acda8e4295b971765392ef9623e7a64e353c1f19551007c"
correct_sha512 = "37d8607d4011b3573601be5695a50087674eab8c315db6c83e2340b26fcca8e48b5a630fedaaf16e92e23abbcb7b6869e1ebc3753399e8c799acb718eae8f325"
correct_blake2 = "598f9494cb3c1ad12de254f21b025920f69f5e39fddb23351489baa654e5115a5745c5e18bb408ebbf51a1b6152e8448a011a50308f022b4dd7598204112ad0f"


def test_generate_checksums():
    assert hash_new_checksum("test/test_file.iso") == correct_sha256
    assert hash_new_checksum("test/test_file.iso", hash_type="sha512") == correct_sha512
    assert hash_new_checksum("test/test_file.iso", hash_type="blake2b") == correct_blake2


def test_compare_checksums():
    assert compare_checksums("test/test_file.iso", correct_sha256) is True
    assert compare_checksums("test/test_file.iso", correct_sha512, hash_type="sha512") is True
    assert compare_checksums("test/test_file.iso", correct_blake2, hash_type="blake2b") is True
