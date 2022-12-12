#Câu 1
x = 'khong the tin duoc'
ten_tap_tin =input("Nhap ten tap tin: ")

path_w = 'C:/Intel/tuanpython.txt'
with open(path_w, mode='w' ) as f:
    f.write(x)

#Câu 2
ten_tap_tin =input("Nhap ten tap tin: ")
f = open('C:/Intel/tuanpython.txt')
print(f.read())

#Câu 3
ten_tap_tin =input("Nhap ten tap tin: ")
y = ' minh rat dep trai'
f = open('C:/Intel/tuanpython.txt','a')
f.write(y)

#Câu 4
f = open('C:/Intel/tuanpython.txt','r')
print(f.read())

#Câu 5
import random as r
def cau_5():
    x=r.choices(range(-1000,1001),k=1000)
    print('danh sách: ',x)
    ten_tap_tin =input("Nhap ten tap tin: ")
    f=open(ten_tap_tin,"w")
    a=[]
    for i in range(10):
        a.append(i)
    for i in range(100):
        for j in range(10):
            a[j]=str(x[i*10+j])
        f.write(','.join(a)+"\n")
    f.close()
    with open(ten_tap_tin,"r+") as f:
        tep=f.read()
        tep=tep.replace(",", "  ")
        print(tep)
cau_5()











