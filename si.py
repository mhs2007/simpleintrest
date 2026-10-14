def simple_interest(principal,interest_rate,time):
    return (principal*interest_rate*time)/100

if __name__=="__main__":
    p = float(sys.argv[1])
    r = float(sys.argv[2])
    t = int(sys.argv[3])

    print("The simple interest is: ",simple_interest(p,r,t))
    
    