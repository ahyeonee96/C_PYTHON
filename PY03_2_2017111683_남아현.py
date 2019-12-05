a=["alpha","beta","gamma","delta","epsilon","zeta"];
c=[];

b=int(input("문자열의 길이 : "));


for i in range(0,len(a)) :
    if len(a[i])==b :
        c.append(a[i])


print(c)