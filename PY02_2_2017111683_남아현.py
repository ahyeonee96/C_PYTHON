#윤년
a=int(input("연도를 입력하세요 :"))

if((a%4)==0) :
    if((a%100)!=0) :
        print("%d년은 윤년입니다." % a)

    else :
        if ((a % 400) == 0) : print("%d년은 윤년입니다."%a)
        else : print("%d년은 윤년이 아닙니다."%a)
