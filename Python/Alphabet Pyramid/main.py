
#def pattern(mid_letter):
Letters = "abcdefghijklmnopqrstuvwxyz"
reverse_letter=""
for k in range(26):
    reverse_letter=reverse_letter+Letters[25-k]
for i in range(26):
    space=""
    for j in range(26-i):
        space=space+" "
    x=space+Letters[:i]+reverse_letter[27-i:26]
    print(x.upper())

for k in range(26, 0, -1):
    reverse_letter=reverse_letter+Letters[25-k]
for i in range(26, 0, -1):
    for j in range(26-i):
        space=space-" "
    x=space+Letters[:i]+reverse_letter[27-i:26]
    print(x.upper())