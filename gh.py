#증명에서 기본적으로 필요한 변수 설정
#특별한 경우를 알려주는 변수
a= 1
#실제로 1에 도달했는지 알려주는 변수
count=0
#몇번만에 1에 도달했는지 알려주는 변수
b=0
#각 수에서 몇번만에 1에 도달했는지 저장하는 list
t=[]
#1~200까지 증명하는 반복문
for i in range(1,201):
    print("시작수:",i,end="\t")
    # i=1이 되는 특별한 경우가 되면 반복을 멈추는 반복문
    while a:
        #짝수일때 2로 나눔
        if i % 2==0:
            i = i/2
            print(i,end="\t")
        #홀수일때 3*i+1을 함
        elif i % 2 != 0:
            if i ==1:
                a =0
                break
            i = 3*i+1
            print(i,end="\t")
        b+=1 
    if a ==0:
        count+=1
    t.append(b)
    print(end="\n")
    a=1
    b=0
if count == 200:
    print("우박수 증명 성공")
    for k in range(len(t)):
        print(t.index(k)+1," 횟수는", max(t),"번이다.")
    print("가장 많은 횟수를 시도한 수는",t.index(max(t))+1,"이고 그 횟수는", max(t),"번이다.")
    
else:
    print("우박수 증명 실패")