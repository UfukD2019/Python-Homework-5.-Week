import random
print("********** HangMan Game **********\n")
print("""This is a hangman game program.
You have only 6 incorrect guesses.
Please enter only letter or word.
The letter cannot be entered twice.
Special chracter or number will not be allowed.
\n\n""")
word_list=["abroad","accident","achievement","acknowledge","administration","agile","behavior","behind","belong","below","belt","bench","capacity","capital","captain","capture","debt","decade","decide","economics","education","efficiency","facility","fair","formidable","generation","gesture","handle","headline","headquarters","immigration","independence","justice","justify","knowledge","landscape","language","miracle","modest","network","nowhere","overall","outcome","passion","phenomenon","quick","reasonable","satisfaction","scenario","schedule","technique","technology","temporary","universe","vehicle","venture","whatever","whisper","yield","zone"]
word1=str(random.sample(word_list,1))
word2=word1.lstrip("['")
word=word2.rstrip("']")
empty=['_' for i in range(len(word))]
count=0
trial=""
entered_letter=""
game=[["------"],
      ["|    |"],
      ["|     "],
      ["|        "],
      ["|        "],
      ["|         "],
      ["|         "],
      ["|    "],
      ["---"]]
for i in game:
 print("\t".expandtabs(20),*i,end="\n")
while True:
    if "_" not in empty:
        print("You win!!! Congratulations!!!")
        print("The word you are trying to guess is:",word)
        break 
    guess=input("Please enter a letter or word\n")
    guess=guess.lower()
    if guess in str(empty) or guess in entered_letter:
        print("You have entered this letter before. Please check!!!")
        continue
    elif guess == word:
        print("You win!!! Congratulations!!!")
        print("The word you are trying to guess is:",word)
        break
    elif guess.isalpha():
        entered_letter+=guess
        list(entered_letter)
        print("The letter(s) you entered is(are):",*entered_letter,sep=" ")
        if guess in word:
            for i in game:
                print("\t".expandtabs(20),*i,end="\n")
            for i in range(len(word)):   
                if word[i]==guess:  
                  empty[i]=[guess]
            for i in empty:
                print(*i,end=" ")
            print("\n")
        elif count ==0 and guess not in word:
            game[2]=["|    O"]
            game[4]=["|        ", "Your remaining attemps is: 5" ]
            for i in game:
             print("\t".expandtabs(20),*i,end="\n")
            count+=1
            trial+=guess
            for i in empty:
                print(*i,end=" ")
            print("\n")
        elif count ==1 and guess not in word:
            game[3]=["|    |   "]
            game[4]=["|    |   ","Your remaining attemps is: 4"]
            for i in game:
             print("\t".expandtabs(20),*i,end="\n")
            count+=1
            for i in empty:
                print(*i,end=" ")
            print("\n")
        elif count ==2 and guess not in word:
            game[3]=["|  / |   "]
            game[4]=["|    |   ","Your remaining attemps is: 3"]
            for i in game:
             print("\t".expandtabs(20),*i,end="\n")
            count+=1
            for i in empty:
                print(*i,end=" ")
            print("\n")
        elif count == 3 and guess not in word:
            game[3]=["|  / | \ "]
            game[4]=["|    |   ","Your remaining attemps is: 2"]
            for i in game:
             print("\t".expandtabs(20),*i,end="\n")
            count+=1
            for i in empty:
                print(*i,end=" ")
            print("\n")
        elif count == 4 and guess not in word:
            game[5]=["|   /     "]
            game[6]=["|  /      "]
            game[4]=["|    |   ","Your remaining attemps is: 1"]
            for i in game:
             print("\t".expandtabs(20),*i,end="\n")
            count+=1
            for i in empty:
                print(*i,end=" ")
            print("\n")
        elif count == 5 and guess not in word:
            game[5]=["|   / \  "]
            game[6]=["|  /   \ "]
            game[4]=["|    |   "]
            for i in game:
             print("\t".expandtabs(20),*i,end="\n")
            count+=1
            print("You lost")
            print("The word you are trying to guess is:",word)
            break
    elif guess.isalpha()== False:
        print("You can only enter a letter or word. Please check and enter a letter or word!!!")
        
        

 
