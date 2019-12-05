n=int(input("0 ~ 99 사이 숫자 입력 : "))
a=1;b=n;
while True :
    i=b%10; j=b//10; k=i+j; k%=10;
    b=10*i+k
    print("%d번째 숫자 : %02d"%(a,b))
    if (b == n): break
    a+=1


print("최종 연산 횟수 : %d 번 "%a)
