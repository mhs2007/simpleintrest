def simple_interest(principal,interest_rate,time):
    return (principal*interest_rate*time)/100

if __name__=="__main__":
    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the interest rate: "))
    t = float(input("Enter the time: "))

    print("The simple interest is: ",simple_interest(p,r,t))
    
    