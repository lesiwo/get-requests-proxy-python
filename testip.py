import requests,json,time,threading

class testip():
    lock=threading.Lock()
    head = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding":"gzip, deflate, br"}
    testing=[]
    testnum=0                                           #加self
    testOverNum=0
    goodips=[]

    def test(self,ip):
        global goodips,testnum,testOverNum,all
        proxy={"http":ip["IP"]}
        try:
            t1=time.time()
            html = requests.head("http://www.baidu.com",headers=self.head,proxies=proxy,timeout=10)
            t2=time.time()
            t=t2-t1
            if not html.status_code == 200:
                raise Error
            
        except Exception as e:
            lock.acquire()
            testOverNum += 1
            percentage =int((testOverNum / all)*100)
            print("  ["+"▉"*percentage+"-"*(100-percentage)+"]"+str(percentage)+"% "+"已完成"+str(testOverNum)+"/"+str(all)+"个 已开始"+str(testnum),end="\r")
            # print(percentage,testOverNum,testnum,len(goodips))
            lock.release()
        else:
            lock.acquire()
            goodips.append(ip)
            
            testOverNum += 1
            percentage =int((testOverNum / all)*100)
            print("  ["+"▉"*percentage+"-"*(100-percentage)+"]"+str(percentage)+"% "+"已完成"+str(testOverNum)+"/"+str(all)+"个 已开始"+str(testnum),end="\r")
            # print(percentage,testOverNum,testnum,len(goodips))
            lock.release()

    def main(self,inPut="d:/python/爬虫/ips.json",outPut="d:/python/爬虫/goodips.json"):
        with open(inPut,"r")as file:
            js=json.load(file)
        all=len(js)
        print("共",len(js),"个")

        for data in js:
            self.testing.append(threading.Thread(target=test, args=(data,)))

        for i in self.testing:
            i.setDaemon(True)

        while True:
            if testnum ==len(self.testing)-1:
                break
            if threading.active_count() < 257:
                self.testing[testnum].start()
                testnum += 1
        while not threading.active_count()==1:
            pass

        with open(outPut,"w")as file:
            json.dump(goodips,fp=file)

        print("done"+" "*125)
        print("共",len(goodips),"个可用")

if __name__ == "__mian__":
    testip().main()