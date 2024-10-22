# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму дробей.

a=input()
b=input()
ai=a.find("/")
ac=1
az=1
if ai == -1:
    ac=int(a)
else:
    ac=int(a[0:ai])
    az=int(a[ai+1:])
bi=b.find("/")
bc=1
bz=1
if bi == -1:
    bc=int(b)
else:
    bc=int(b[0:bi])
    bz=int(b[bi+1:])
res=((ac * bz) + (bc * az)) / (az * bz)
print(res)
