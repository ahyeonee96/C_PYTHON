list1=[];
list2=[];

list1.append([1,2,3,4]);
list1.append([5,6,7,8]);
list1.append([9,10,11,12]);

for index in range(0,3):
    print("list_1(%d):" %(index),list1[index])
    list2.append(list1[index])

print("--------------------------");

print("list_2 : ",list2);
print("--------------------------");

for index1 in range(0,3):
    for index2 in range(0,4):
        print("list_2[%d][%d] : %d \t"%(index1,index2,list2[index1][index2]),end='')
    print("")