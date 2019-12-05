import random
import time

class person :
    def __init__(self,name,ph):
        self.name = name;
        self.phone = ph;
    def get_name(self):
        return self.name;
    def get_phone(self):
        return self.phone;


class student(person) :
    def __init__(self,major,num,name,ph):
        self.major=major;
        self.num=num;
        super(student,self).__init__(name,ph)
    def get_major(self):
        return self.major;
    def get_num(self):
        return self.num;

class work(person) :
    def __init__(self,dep,c_num,name,ph):
        self.dep=dep;
        self.c_num=c_num;
        super(work, self).__init__(name, ph)

    def get_dep(self):
        return self.dep;
    def get_c_num(self):
        return self.c_num;


nameList= ["홍동현","서상욱","도찬호","이대희","최기태","강동호","김준식","이영석","김승주","김종범"]
majorList= ["컴퓨터학부","기계공학부","통계학과","경영학부"]
departList=["개발연구팀","인사관리팀","전략기획팀"]

A=[];B=[];



count=0
in_file = None
in_str=""
in_list=[]

logfile=open("address.log.txt","w")

in_file = open("address.txt","r")


now_time="["+time.asctime()+"] "
logfile.write(now_time)
logfile.write("open file address.txt")
logfile.write("\n")

in_list=in_file.readlines()



for i in range(len(in_list)) :
    if "학생" in in_list[i] :
        for j in range(len(majorList)) :
            if majorList[j] in in_list[i] :
                major=majorList[j]
        for j in range(len(nameList)) :
            if nameList[j] in in_list[i] :
                name=nameList[j]
        for n in range(len(in_list[i])) :
            if "010" == in_list[i][n:n+3] :
                ph=in_list[i][n:n+14]
        for n in range(len(in_list[i])) :
            if "201" == in_list[i][n:n+3] :
                num=in_list[i][n:n+11]

        A.append(student(major, num, name, ph)); B.append("학생");
        count+=1

    else : #사원
        for j in range(len(departList)) :
            if departList[j] in in_list[i] :
                dep=departList[j]
        for j in range(len(nameList)):
            if nameList[j] in in_list[i]:
                name = nameList[j]
        for n in range(len(in_list[i])) :
            if "010" == in_list[i][n:n+3] :
                ph=in_list[i][n:n+14]
        for n in range(len(in_list[i])) :
            if "201" == in_list[i][n:n+3] :
                c_num=in_list[i][n:n+8]

        A.append(work(dep, c_num, name, ph));B.append("사원");
        count+=1


out_count="total %d persons"%count
now_time="["+time.asctime()+"] "
logfile.write(now_time)
logfile.write(out_count)
logfile.write("\n")

while (True):

    a=input("찾을 사람 이름은? ")
    search="search %s" %a
    now_time = "[" + time.asctime() + "] "
    logfile.write(now_time)
    logfile.write(search)
    logfile.write("\n")


    if a=="끝" :
        logfile.write(now_time)
        logfile.write("exit")
        break;

    for i in range(0,len(A)) :
        if a==A[i].get_name() :
            if B[i]=="학생" :
                print("전화번호 : %s"%A[i].get_phone())
                print("학과 : %s"%A[i].get_major())
                print("학번 : %s"%A[i].get_num())

            elif B[i]=="사원" :
                print("전화번호 : %s" %A[i].get_phone())
                print("부서 : %s"%A[i].get_dep())
                print("사번 : %s"%A[i].get_c_num())