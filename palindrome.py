inpstr=str(input('Enter a string: '))
inpstr=list(inpstr)
revstr= inpstr[::-1]

for i in range(len(inpstr)):
     if not inpstr[i]==revstr[i]:
       print("Not a palindrome")
       break
else:
       print("yes its a Palindrome")