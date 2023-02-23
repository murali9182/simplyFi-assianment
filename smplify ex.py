n= int(input('enter input: '))
for i in range(n):
    c=0
    n,k=list(map(int,input('enter input: ').split()))
    heights=list(map(int,input('enter input: ').split()))
    for j in heights:
        if i>k:
            c+=1
    print(c)
