import os
print("\033[40;37m\ngive me a file list to cat separete by ,\n")
i=input().strip()
ii=i.split(",")
for n in ii:
    f1=open(n,"r")
    r=f1.read()
    f1.close()
    print(r)