def prime_check(y):
    result = True
    if y==1:
        return False
    for j in range(2, y//2+1):
        if y%j == 0:
            result = False
            break
    return result
Prime_count = 0
Start_num = int(input("Enter starting number:"))

if Start_num %2==0 and Start_num !=2:
    Start_num=Start_num+1

if Start_num ==2 or Start_num == 1:
    Prime_count = 1
    Start_num = 3
End_num = int(input("Enter last number:"))

for i in range(Start_num,End_num+1,2):
    if prime_check(i) == True:
        Prime_count = Prime_count+1
print(Prime_count)