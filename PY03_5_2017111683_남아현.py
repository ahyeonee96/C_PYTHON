i=0;j=1;
l=1;
list1=[];
while(True) :
    while (True):
        a=int(input("입력할 수 : "))
        if(a==0) :
            break;

        list1.append(a);

    print("-----------------------");
    print("입력된 리스트 : ",list1);

    while(j!=len(list1)) :
        if(list1[i]>list1[j]) :
            list1.insert(i,list1[j])
            del(list1[j+1])
            print("%d 단계 : "%(l),list1)
            l+=1;j+=1;i=0;

        else :
            i+=1;

    print("최종 리스트 : ",list1)
    print("-----------------------");