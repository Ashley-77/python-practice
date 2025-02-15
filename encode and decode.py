#there are two types of coding and decoding
from 初学.chapter4.string import score

A='merry christmas'
b="谢谢你"
scode=A.encode(errors='replace')
print(scode)
scode=A.encode(errors='ignore')
print(scode)
scode=b.encode(errors='strict')
print(scode)
scode_gbk=b.encode('gbk',errors="ignore")#default:utf_8,replace\strict\ignore
print(scode_gbk)#one chinese character occupy two charaCTER
c="🙃上课❤"
#scode2=c.encode('gbk',errors="strict")
scode2=c.encode('gbk',errors="replace")#display question mark
print(scode2)#gbk error but utf_8 won't
#decode
print(bytes.decode(scode2,'gbk',errors='ignore'))#use the corresponding method as coding
print(bytes.decode(scode,errors='replace'))#use intermedia quantity scode ect
