a=int(input("enter the no of keys in dictionary : "))
d=dict()
for i in range(a):
    c=int(input("enter the key : "))
    e=(input("enter the value : "))
    d[c]=e
d1={}
l=list(d.items())
for key ,value  in l:
    if value not in d1.values():
        d1[key]=value
print(d1)
