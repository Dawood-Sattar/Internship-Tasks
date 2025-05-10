def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))


noOfTerms=int(input("Enter No of Terms : "))

if noOfTerms<=0:
    print("Please Enter Positive Integer : ")
else:
    print("Fibonacci sequence : ")

    for i in range(noOfTerms):
        print(recur_fibo(i))
