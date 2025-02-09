a='1234'
b='一二三四'
c='001b1'
d='one'
print(a.isdigit())#only Arabic number
print(b.isdigit())
print(c.isdigit())
print(d.isdigit())
print(a.isnumeric())
print(d.isnumeric())#Rome\Chinese is ok
print("---------------"*20)
print('123nihao'.isalpha())
print('123你好'.isalpha())#alpha,including chinese and letter
print('hello你好nihao'.isalpha())
print('hello你好nihao1234'.isalnum())#number and alpha are ok
print("---------------"*20)
print('hds手动阀fi'.islower())
print('KJ海外的DJS'.isupper())#Chinese is both capital and lower case
print('Spark'.istitle(),'dsaf'.istitle(),'PsiKsf'.istitle())#the first letter is capital,only
print('Hello sea'.istitle())#after blank should use the upper
print('\n'.isspace(),'\t'.isspace(),'  '.isspace())
print('me \n you')#n is another line
print('\t')#as a space key