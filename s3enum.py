#!/bin/python3

__title__ = 's3enum'
__version__ = '1.0'
__author__ = 'xiosec'
__license__ = 'MIT'
__copyright__ = 'Copyright 2022 by xiosec'


import os
import argparse
import requests
from http import HTTPStatus
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed


def make_request(url:str, suffix:str, name:str):

    urlString = "http://s3.amazonaws.com/{}{}{}".format(
        url,
        suffix,
        name
    )
    
    code = requests.get(url=urlString).status_code
    return [suffix+name, code]

def main(values:dict):
    threadNumber = int(values["thread"]) if values["thread"] != None else 10

    if values["suffixlist"] != None:
        with open(values["suffixlist"],"r") as suffixfile:
             suffixlist = suffixfile.readlines()
    else:
        suffixlist = [
            '-',
            '_', 
        ]
    
    url = values["url"]

    status = {
        HTTPStatus.OK: "--[200] http://s3.amazonaws.com/{} OK",
        HTTPStatus.FORBIDDEN: "-[403] http://s3.amazonaws.com/{} Secure",
        HTTPStatus.MOVED_PERMANENTLY: "-[301] http://s3.amazonaws.com/{} Redirect",
        HTTPStatus.NOT_FOUND: "-[404] http://s3.amazonaws.com/{} Not Found",
    }

    if values["url"][-1] == '/':
        url = url[:-1]

    if "://" in values["url"]:
        url = url.split("://")[1]

    check = requests.get("http://s3.amazonaws.com/{}".format(url)).status_code
    print("Check site availability :", check)

    if check not in status:
        print("This address is not available")
        os.exit(1)
    
    with open(values["wordlist"]) as wordlistfile:
        wordlist = wordlistfile.readlines()
    
    tasks = []

    with ThreadPoolExecutor(max_workers=threadNumber) as executor:
        for word in wordlist:
            for suffix in suffixlist:
                tasks.append(executor.submit(make_request, url, suffix, word.strip()))
        
        for future in as_completed(tasks):
            try:
                result = future.result()
                if result[1] in status:
                    if result[1] == 404 and values['wildcard'] == True:
                        print(status[result[1]].format(url + result[0]))
                    elif result[1] != 404:
                        print(status[result[1]].format(url + result[0]))

            except Exception as exc:
                if values["debug"] == True:
                    print(exc)
        
    print("="*50)
    print("Finished in : {}".format(datetime.now()))

if __name__ == "__main__":
    parser = argparse.ArgumentParser( 
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Amazon S3 bucket enumeration \n"\
        "github : https://github.com/xiosec/s3enum \n"\
        "twitter: xiosec"
    )

    parser.add_argument("--url", type=str, help="example.com")
    parser.add_argument("--wordlist", type=str, help="Wordlist based on most common aws s3 bucket names")
    parser.add_argument("--suffixlist", type=str, help="List of Suffix")
    parser.add_argument("--thread", type=str, help="Number of threads (The default is 10)")
    parser.add_argument("--wildcard", action=argparse.BooleanOptionalAction)

    args = parser.parse_args()
    check = list(filter(lambda x: x[1] != None , args._get_kwargs()))
    if len(check) < 2:
        print("[*] Fields are not set correctly")
        parser.print_help()
    else:
        args = dict(args._get_kwargs())
        print("="*50)
        print("Amazon S3 bucket enumeration\n"\
              "github : https://github.com/xiosec/s3enum\n"
        )
        print("URL        | {}".format(args["url"]))
        print("wordlist   | {}".format(args["wordlist"]))
        print("workers    | {}".format(args["thread"] if args["thread"] != None else 10))
        print("start time | {}".format(datetime.now()))
        print("="*50)
        main(args)
