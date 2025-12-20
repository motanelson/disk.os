import os
k=1024
m=k*k
g=m*k
t=g*k
cc=b"\x00"
print("\033c\033[40;37m\ngive me the output file name ? ")
kk=b""
mm=b""
gg=b""
def retb(c,value,n):
    a=b""
    a=c*value
    f1=open(n,"wb")
    f1.write(a)
    f1.close()
v=b""
n=input()
n=n.strip()
nnn=737280
retb(cc,nnn,n)
os.system("mkfs.fat -F 12 $1".replace("$1",n))
os.system("file $1".replace("$1",n))

        
