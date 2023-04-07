import requests,json,time,threading


lock=threading.Lock()
head = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding":"gzip, deflate, br"}

goodips=[]
testbot=[]
js=[]

def test():
    global js,head
    while not len(js)==0:
        testing = js.pop(0)
        proxy={testing["http"]:testing["IP"]}
        try:
            t1=time.time()
            html = requests.head("http://www.baidu.com",headers=head,proxies=proxy,timeout=20)
            t2=time.time()
            t=t2-t1
            if not html.status_code == 200:
                raise TimeoutError
        except Exception:
            pass
        else:
            goodips.append(testing)
        time.sleep(1)


def main(inPut="./ips.json",outPut="./goodips.json"):
    global testing,js
    with open(inPut,"r")as file:
        js=json.load(file)
    ipnum = len(js)
    print("共",len(js),"个")

    for i in range(8):
        testbot.append(threading.Thread(target=test))

    for i in testbot:
        i.setDaemon(True)
    
    for i in testbot:
        i.start()

    while not len(js)==0:
        percentage =int(((ipnum - len(js)) / ipnum)*100)
        print("  ["+"▉"*percentage+"-"*(100-percentage)+"]"+str(percentage)+"% "+"已完成"+str(ipnum - len(js))+"/"+str(ipnum)+"个",end="\r")
    
    print("done"+" "*125)
    print("共",len(goodips),"个可用")

if __name__ == "__main__":
    main()