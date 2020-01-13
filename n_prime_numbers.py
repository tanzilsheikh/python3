print("FIND PRIME NUMBERS BETWEEN LOWER AND UPPER LIMIT.")
l_limit=int(input("lower limit: "))
if l_limit ==0 or l_limit==1:
    l_limit=2
u_limit=int(input("upper limit: "))
flag=False
for i in range (l_limit,u_limit+1):
    flag=0
    for j in range (2,i):
        if(i%j)==0:
            flag=1
            break
    if(flag==0):
        print(i, end =" ")
