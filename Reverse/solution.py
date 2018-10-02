#tested in python2
#to install pwn library : http://docs.pwntools.com/en/stable/install.html
#You can also use pip to install this.
from pwn import *
q="aXat9r45UtyMjw4i5Wh8swVWmEg3vAbW" #this is the string 
flag=0
while(flag==0):
	t='printf '+ str(q)+'
	d='ltrace /home/vaibhav/Downloads/./lock' #your directory where lock is located
	t=t+"|"+d   #pipelining printf into ltrace
	r= process(t, shell=True)
	s=r.recvuntil("free")
	s=s.split() 
	if(int(s[-2])!=0):#checking if it's 2nd last var is 0
		q+=chr(abs(int(s[-2])))
	else:
		flag=1

print("PASSWORD :" ,q)
