def pattern(middle_num):
    for i in range(middle_num):
        x=0
        for j in range(i+1):
            x=x+(j+1)*10**j
        for k in range(i):
            x=x+(i-k)*10**(k+i+1)
        print(x)
    for i in range(middle_num - 2, -1, -1):
        x = 0
        for j in range(i + 1):
            x = x + (j + 1) * 10 ** j  
        for k in range(i):
            x = x + (i - k) * 10 ** (k + i + 1)
        
        print(x)

mid_num = int(input("Enter middle number:"))   
pattern(mid_num)
