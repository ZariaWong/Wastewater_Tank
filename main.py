TotalNum=input()
Flow=input().split(' ')
Starting=int(input())
Number=0
Count=0
Remember=[-1]


while Starting not in Remember:
    if Starting!= -1:
        Remember.append(Starting)
        Starting=int(Flow[Starting])
        Number+=1

print(Number)
