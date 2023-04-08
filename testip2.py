import requests,json,time,threading


lock=threading.Lock()
head = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding":"gzip, deflate, br"}

goodips=[]
testbot=[]
botnum=0
overnum=0
js=[]

def test():
    global js,head,botnum,overnum
    while not len(js)==0:
        testing = js.pop(0)
        proxy={testing["http"]:testing["IP"]}
        try:
            t1=time.time()
            html = requests.head("http://www.baidu.com",headers=head,proxies=proxy,timeout=10)
            t2=time.time()
            t=t2-t1
            if not html.status_code == 200:
                raise TimeoutError
        except Exception:
            pass
        else:
            goodips.append(testing)
        finally:
            overnum+=1
        # time.sleep(1)
    botnum-=1


def main(inPut="./ips.json",outPut="./goodips.json"):
    global testing,js,botnum,overnum
    with open(inPut,"r")as file:
        js=json.load(file)
    ipnum = len(js)
    print("共",len(js),"个")

    for i in range(256):
        testbot.append(threading.Thread(target=test))
        botnum+=1

    for i in testbot:
        i.setDaemon(True)
    
    for i in testbot:
        i.start()

    while not botnum==0:
        percentage =int((overnum / ipnum)*100)
        print(" ["+"▉"*percentage+"-"*(100-percentage)+"]"+str(percentage)+"% "\
            +"已完成"+str(overnum)+"/"+str(ipnum)+"个,"\
                +str(len(goodips))+"个可用",end="\r")
    
    with open(outPut,"w")as file:
        json.dump(goodips,fp=file)

    print("\ndone")
    print("共",len(goodips),"个可用")

if __name__ == "__main__":
    main()