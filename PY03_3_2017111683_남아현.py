list1=[];
b='';

while(True):
    a=input("문자열 입력 : ")
    if(a=="exit"):
        break;

    for i in range(0,len(a)) :
        if(ord(a[i])<91 and ord(a[i])>64) :
            list1.append(a[i].lower())
        elif(ord(a[i])>96 and ord(a[i])<123) :
            list1.append(a[i].upper())
        elif(a[i]==' ') :
            list1.append(a[i]);
    for i in range(0,len(list1)):
        b+=list1[i];

    print("대소문자 변환 결과 => "+b)
    list1=[];b='';
