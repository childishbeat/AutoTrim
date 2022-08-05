import sys
import os
import binascii
a=sys.argv[1]
b=2
with open(a,'rb')as f:content=f.read().hex()
while True:
    if content[-b]!=content[-2]and content[-b-1]!=content[-1]:break
    b=b+2
os.rename(a,a+'.bak')
with open(a,'wb')as f:f.write(binascii.unhexlify(content[:len(content)-len(content[-b+2:])]))
