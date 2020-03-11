n = input()
for x in range(0,int(n)):
     aj1= input()
     aj2 = input()
     if aj1 in aj2 or "".join(reversed(aj1)) in aj2:
         print("YES")
     else:
         print("NO")