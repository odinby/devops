up=0
x=input("Enter: ")
for num in x:
    if num.isupper():
        up+=1
print(up)


#import pyping 
#response = pyping.ping('google.com') 
#print(response)
#if response.ret_code == 0: 
#    print("reachable") 
#else: print("unreachable")


import os
response = os.system("ping -c 1 google.com > /dev/null")
if response == 0:
    print("Network Active")
else:
    print("Network Error")


import datetime
#datetime.now()
print(datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0))

from datetime import datetime
print(datetime.now())
