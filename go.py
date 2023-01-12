import time

all=100
gone=0
for gone in range(1,101):

    percentage =int((gone / all)*100)
    print("  ["+"▉"*percentage+"-"*(100-percentage)+"]"+str(percentage)+"%",end="\r")
    time.sleep(0.05)
print(" "*108+"\r",end="")
