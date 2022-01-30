def occurance_check(l):
    temp=[]
    for i in range(len(l)):
        if l[i] in temp:
            return l[i]
        else:
            temp.append(l[i])
if __name__=="__main__":
    l=list(map(int,input().strip().split()))
    print(occurance_check(l))

