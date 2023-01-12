import requests,bs4,re,json

head = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding":"gzip, deflate, br"}

def getIpRe(webside="http://api.89ip.cn/tqdl.html?api=1&num=2921&port=&address=&isp=",ipfile="d:/python/爬虫/ips.json"):

    global head
    html = requests.get(webside,headers=head).text
    IP = re.findall(
        r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]{2,5}",
        html
    )
    with open(ipfile,"r")as file:
        js=json.load(file)
    for i in IP:
        js.append({"IP":i,"http":"http"})
    with open(ipfile,"w")as file:
        json.dump(js,fp=file)
