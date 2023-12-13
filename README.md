# Checksum
Simple python script to verify and check checksums

### Install
This project can be pip installed from GitHub:

```bash
pip install git+https://github.com/kcx1/checksum
```

### CLI Usage

Once pip installed the script can be accessed directly

```
checksum arg1 arg2
```

Alternatively, this repo can be cloned and the script can be called with python from inside of the cloned directory:

```
python3 -m cli arg1 arg2
```

There are 2 positional arguments:

1. **File**: The file you would like to run a checksum against
2. **Expected Result**: *Optional* - If none is given, then the script will simply return the checksum hash of the file supplied in the first argument. Otherwise the script will check to see if the resulting checksum from the provided file matches the expected result. 

**NOTE** *The expected result argument can accept either a string or a file with a single checksum result inside.*

You can specify the checksum that you would like to use by using the -t / --type flag. If none are given, then the default sha256 will be used. 


### Example CLI

```bash
checksum example.iso dc9f4f22700beb2895197fa0995e25075feb14457fde09ff3ac46dd35d75661a -t sha256
```
```bash
checksum example.iso sha256.txt -t sha256
```

### Example Python Usage
```python
from checksum import hash_new_checksum, compare_checksums

# Get a new checksum
new_checksum = hash_new_checksum('test/test_file.iso', hash_type="sha512")
print(new_checksum)

# Check if a checksum matches
matches = compare_checksums('test/test_file.iso', 'test/test_checksum_sha512.txt', hash_type="sha512")
print(matches)
```


### Help File
```
usage: Check Sum [-h] [-t [Hash type]] file [expected_result]

Check sum a file against a known checksum

positional arguments:
  file                  File that you wish to run a checksum against
  expected_result       OPTIONAL: Paste in the check sum you expect FILE | Str

options:
  -h, --help            show this help message and exit
  -t [Hash type], --type [Hash type]
                        Choose the checksum that you would like to use: [
                        sha1, sha224, sha256, sha384, sha512, blake2b,
                        blake2s, md5 ]
```
