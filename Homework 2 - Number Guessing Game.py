print("********** Number Guessing Game **********\n")
print("""This is a number guessing game.
You will try to guess the 4-digit number with no 0(zero) in it and all the numbers are different.
If the value(s) and digit(s) of one or all of the digits of the number you entered are correct, you will see "+1" on the screen.
If the value(s) of one or all of the number you entered is correct but the digits are incorrect, you will see "-1" on the screen.
In other cases, Nothing will be seen on the screen.
\n\n""")
import random
digit=["1","2","3","4","5","6","7","8","9"]
number=random.sample(digit,4)
while True:
 guess=input("Please enter 4 digits number in accordance with the instructions.\n")
 positive=0
 negative=0
 if guess.isdigit()==False or len(guess)!=4 or "0" in guess:
     print("""The guess you entered must be only a 4-digit number and it cannot contain 0 (zero).
Please read the instructions and enter suitable number!!!
""")
     continue
 for i in guess:
  if guess.count(i)>1:
     print("""The digits of the number you entered must be different each other.
Please read the instructions and enter suitable number!!!
""")
     guess=""
 guess=list(guess)
 if number==list(guess):
     print("You win. Congratulations!!!")
     break
 for i in number:
    for k in guess:
        if i == k and number.index(i)==guess.index(k):
            positive+=1
        elif i == k and number.index(i)!=guess.index(k):
            negative+=1
 if guess!=[]:
  print("+",positive,"-",negative,"\n")
