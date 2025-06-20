while True:
    n = int(input("Enter the number: "))
    for i in range(1,11):
#i+=1
        print(f"{n} × {i} = {n*i}")
    choice=input("use again it?(y/n) : ")
    if choice.lower()!='y':
        print ("thank you & tata👋")
        break
        