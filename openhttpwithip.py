import requests

pr = {'http':'113.194.135.122:9999','https':'113.194.135.122:9999'}
html = requests.get(input("url"),proxies=pr).text
print(html)
