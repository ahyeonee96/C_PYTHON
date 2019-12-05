#높은 가격 순으로 출력하기.
j=1;
a=input().split(';');

for i in range(0,len(a)) :
    a[i]=int(a[i])

    if a[i]>999999999 :
        print("Error! it overs the range of number,")
        break;

    i=0;


while (j != len(a)):
    if (a[i] < a[j]):
        a.insert(i, a[j])
        del (a[j + 1])
        j += 1;
        i = 0;
    else:
        i += 1;

for i in range(0, len(a)):
    print(format(a[i], ',').rjust(11))