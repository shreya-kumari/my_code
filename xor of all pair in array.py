Write your code here
if __name__ == "__main__":
    n = int(input())
    total =0
    m =1000000007
    i= 0
    cycle = pow(2, i+1)
    while(pow(2, i) <= n):
        if((n+1)%cycle == 0):
            count1 = (n+1)//2
        else:
            count1 = ((n+1)//cycle) * cycle//2
            rem = max(0, (n+1)%cycle - cycle//2)
            count1 += rem
        count0 = (n+1) - count1
        count = count0 * count1
        total += pow(2, i) * count

        #print(i, count0,count1,count, carry, total)
        i += 1
        cycle = pow(2, i+1)
        
    
    print(total%m)