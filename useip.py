import getip,testip2,requests,json,os,time
# print(os.getcwd())
goodIpNum = 0
ips = "./ips.json"
goodIps = "./goodips.json"
def setIpfile(ip,goodip):
    global ips,goodips
    ips = ip
    goodIps = goodip
    

def ipGet(webpage=None,page=1):
    global ips
    if not os.path.exists(ips):
        f = open(ips,"w")
        f.write("[]")
        f.close()
    if webpage==None:
        for i in range(1,page+1):
            getip.getIp(i,ips)
            time.sleep(0.7)
            print("page:",i,end="\r")
    else:
        getip.getIpRe(webpage,ips)

def ipTest():
    global goodIpNum,ips,goodIps
    testip2.main(ips,goodIps)
    with open(goodIps,"r") as f:
        goodIpNum = len(json.load(fp=f))
if __name__ =="__main__":
    ipGet(webpage="http://api.89ip.cn/tqdl.html?api=1&num=100&port=&address=&isp=",page=30)
    ipTest()
    
    
