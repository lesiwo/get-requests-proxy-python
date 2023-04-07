import requests,bs4,json,re
head = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding":"gzip, deflate, br"}

def getIp(page="1",ipfile="./ips.json"):
    global head
    html = requests.get("https://www.kuaidaili.com/free/inha/"+str(page),headers=head).text
    find = bs4.BeautifulSoup(html,"lxml")
    find1 = find.find(name = "table",class_='table table-bordered table-striped')
    if find1 == None:
        find = find.find(name = "tbody")
    else:
        find=find1
    ip = find.find_all(name = "td",attrs={"data-title":"IP"})
    port = find.find_all(name = "td",attrs={"data-title":"PORT"})
    ips =[]
    httpOrHttpS = find.find_all(name = "td",attrs={"data-title":"类型"})
    for i in ip:
        ips.append(str(i.string))
    ports =[]
    for i in port:
        ports.append(str(i.string))
    httpOrHttpSList=[]
    for i in httpOrHttpS:
        httpOrHttpSList.append(str(i.string))

    with open(ipfile,"r")as file:
        js=json.load(file)


    for i in range(len(ips)):
        js.append({"IP":ips[i]+":"+ports[i],"http":httpOrHttpSList[i]})
    with open(ipfile,"w")as file:
        json.dump(js,fp=file)

def getIpRe(webpage="http://api.89ip.cn/tqdl.html?api=1&num=2921&port=&address=&isp=",ipfile="./ips.json"):

    global head
    html = requests.get(webpage,headers=head).text
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

if __name__ == "__main__":
    getIp()