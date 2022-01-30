def individual_score(l):
    p1=0;p2=0;flag=0;
    for i in range(len(l)):
        if flag==0:
            if l[i]%2==0:
                p1+=l[i]
            else:
                p1+=l[i]
                flag=1
        else:
            if l[i]%2==0:
                p2+=l[i]
            else:
                p2+=l[i]
                flag=0
    print("p1:"+str(p1)+",p2:"+str(p2))

if __name__=="__main__":
    l=list(map(int,input().strip().split()))
    individual_score(l)

        

