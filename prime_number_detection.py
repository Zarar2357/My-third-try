x=input("input any number")
x=int(x)
i=2
while i < x:
    if x%i==0:
        print("it is not a prime number")
        break
    else:
        i=i+1
    if i==x-1:
        print('it is a prime number')
        break

    

