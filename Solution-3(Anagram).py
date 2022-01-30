def anagram_check(s1,s2):
    if(sorted(s1.lower())==sorted(s2.lower())):
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    c=0
    while c==0:
        try:
            s1, s2 = input("Enter two Strings: ").split()
            anagram_check(s1,s2)
            c=1
        except ValueError:
            print("Please Enter only two Strings")
    

