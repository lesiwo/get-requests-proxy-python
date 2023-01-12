import getip,testip,requests,json

goodIpNum = 0
ips = "d:/python/爬虫/ips.json"
goodIps = "d:/python/爬虫/goodips.json"
def setIpfile(ip,goodip):
    global ips,goodips
    ips = ip
    goodIps = goodip

def ipGet(webpage=None,page=1):
    global ips
    if webpage==None:
        for i in range(1,page+1):
            getip.getIp(i,ips)
    else:
        getip.getIpRe(webpage,ips)

def ipTest():
    global goodIpNum,ips,goodIps
    test = testip.testip()
    test.main(ips,goodIps)
    with open(goodIps,"r") as f:
        goodIpNum = len(json.load(fp=f))
if __name__ =="__main__":
    ipGet(page=1)
    ipTest()
    
    
