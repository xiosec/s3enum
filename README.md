# s3enum

<p align="center">
<img src="resources/images/amazon-s3.jpg">
<br/>
<i>Amazon S3 bucket enumeration</i>
</p>

[![xiosec - s3enum](https://img.shields.io/static/v1?label=xiosec&message=s3enum&color=blue&logo=github)](https://github.com/xiosec/s3enum)
[![stars - s3enum](https://img.shields.io/github/stars/xiosec/s3enum?style=social)](https://github.com/xiosec/s3enum)
[![forks - s3enum](https://img.shields.io/github/forks/xiosec/s3enum?style=social)](https://github.com/xiosec/s3enum) [![GitHub release](https://img.shields.io/github/release/xiosec/s3enum?include_prereleases=&sort=semver)](https://github.com/xiosec/s3enum/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)
[![issues - s3enum](https://img.shields.io/github/issues/xiosec/s3enum)](https://github.com/xiosec/s3enum/)

## Usage

```
$ python3 s3enum.py --help
```
```
usage: s3enum.py [-h] [--url URL] [--wordlist WORDLIST] [--suffixlist SUFFIXLIST] [--thread THREAD] [--wildcard | --no-wildcard]

Amazon S3 bucket enumeration
github : https://github.com/xiosec/s3enum
twitter: xiosec

optional arguments:
  -h, --help            show this help message and exit
  --url URL             example.com
  --wordlist WORDLIST   Wordlist based on most common aws s3 bucket names
  --suffixlist SUFFIXLIST
                        List of Suffix
  --thread THREAD       Number of threads (The default is 10)
  --wildcard, --no-wildcard
```

## Example
```
$ python3 s3enum.py --url example.com --wordlist wordlist/BucketNames.txt --wildcard
```
```
==================================================
Amazon S3 bucket enumeration
github : https://github.com/xiosec/s3enum

URL        | example.com
wordlist   | wordlist/BucketNames.txt
workers    | 10
start time | 2022-02-23 21:56:31.171768
==================================================

-[404] http://s3.amazonaws.com/example.com-org Not Found
--[200] http://s3.amazonaws.com/example.com-bucket OK
-[403] http://s3.amazonaws.com/example.com-staging Secure

==================================================
Finished in : 2022-02-23 21:56:32.605953
```

## License

Released under [MIT](/LICENSE) by [@xiosec](https://github.com/xiosec).
