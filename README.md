# Assignment-Solution
This is the assignment code in python  for Cipher Schools 
for _ in range(int(input())):
    x=input()
    arr=[]
    a1,a2=["(","{","["],[")","}","]"]
    flag=False
    for j in x:
        if j in a1:arr.append(a2[a1.index(j)])
        else:
            if len(arr)==0 or arr[-1]!=j:
                flag=False
                break
            else:
                flag=True
                arr.pop()
    if flag and len(arr)==0:print("YES") 
    else: print("NO")        

