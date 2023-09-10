# Checksum
Simple python script to verify and check checksums

Call the script with python:

```python3 checksum.py```

There are 2 positional arguments:

1.) File: The file you would like to run a checksum against
2.) Expected Result: *Optional* If none is given, then the script will simply return the checksum hash of the file supplied in the first argument. Otherwise the script will check to see if the resulting checksum from the provided file matches the expected result. 

**NOTE** *The expected result argument can accept either a string or a file with a single checksum result inside.*

You can specify the checksum that you would like to use by using the -t / --type flag. If none are given, then the default sha256 will be used. 

**NOTE**
The pyproject.toml has not been tested. I expect to update this in the near future to allow the tool to be built using pip install. 

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
