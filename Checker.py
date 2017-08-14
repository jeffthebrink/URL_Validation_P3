import urllib.request
import urllib.parse
import ssl

if __name__ == '__main__':
    while True:
        url = input("Enter an address to check: ")
        if url[0: 7] != "http://":
            url = "http://" + url
        try:
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            if response.status == 200:
                print("URL IS GOOD")
            else:
                print("Status: " + response.status)
        except urllib.request.URLError:
            sslContext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
            try:
                sslRequest = urllib.request.Request(url)
                sslResponse = urllib.request.urlopen(url, context=sslContext)
                print("Site uses SSL. Bypassing SSL verification.")
                if sslResponse.status == 200:
                    print("URL IS GOOD")
            except:
                print("URL IS NOT GOOD")
