import random

class person :
    def __init__(self,name,p1,p2):
        self.name = name;
        self.phone = "010-"+p1+"-"+p2
        self.type = type;
    def get_name(self):
        return self.name;
    def get_phone(self):
        return self.phone;


class student(person) :
    def __init__(self,major,num,name,p1,p2):
        self.major=major;
        self.num=2010000000+num;
        super(student,self).__init__(name,p1,p2)
    def get_major(self):
        return self.major;
    def get_num(self):
        return self.num;

class work(person) :
    def __init__(self,dep,c_num,name,p1,p2):
        self.dep=dep;
        self.c_num=2019000+c_num;
        super(work, self).__init__(name, p1, p2)

    def get_dep(self):
        return self.dep;
    def get_c_num(self):
        return self.c_num;



nameList= ["홍동현","서상욱","도찬호","이대희","최기태","강동호","김준식","이영석","김승주","김종범"]
majorList= ["컴퓨터학부","기계공학부","통계학과","경영학부"]
departList=["개발연구팀","인사관리팀","전략기획팀"]
idList=["학생","사원"]
A=[];B=[];


print("----- 주소록 프로그램 -----")

for i in range(0,len(nameList)) :
    p1 = str(random.randint(1000, 9999))
    p2 = str(random.randint(1000, 9999))
    s_id = random.randint(1000000, 9999999)
    c_id = random.randint(100, 999)

    major1 = majorList[random.randint(0, len(majorList) - 1)]
    depart1 = departList[random.randint(0, len(departList) - 1)]

    id = idList[random.randint(0, 1)]
    if id=="학생" :
        A.append(student(major1,s_id,nameList[i],p1,p2)); B.append(id)
    elif id=="사원" :
        A.append(work(depart1, c_id, nameList[i], p1, p2)); B.append(id)


for i in range(0,10) :
    if B[i]=="학생" :
        print("[%s] 이름 : %s\t 전화번호 : %s 학과 : %s\t 학번 : %d" % (B[i], A[i].get_name(), A[i].get_phone(), A[i].get_major(), A[i].get_num()))
    elif B[i]=="사원" :
        print("[%s] 이름 : %s\t 전화번호 : %s 학과 : %s\t 학번 : %d" % (B[i], A[i].get_name(), A[i].get_phone(), A[i].get_dep(), A[i].get_c_num()))

while (True):

    a=input("찾을 사람 이름은? ")
    if a=="끝" :
        break;

    for i in range(0,10) :
        if a==A[i].get_name() :
            if B[i]=="학생" :
                print("전화번호 : %s"%A[i].get_phone())
                print("학과 : %s"%A[i].get_major())
                print("학번 : %d"%A[i].get_num())

            elif B[i]=="사원" :
                print("전화번호 : %s" %A[i].get_phone())
                print("부서 : %s"%A[i].get_dep())
                print("사번 : %d"%A[i].get_c_num())