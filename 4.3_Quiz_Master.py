'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
print("\nHello and welcome to my Quiz!!!")
print("lets Begin!!\n")

print("1. What inspired that game Pac Man?\n")

print("Space Invaders")
print("Pizza")
print("Comic Book")

answer = input("\nWhich is true?? : ")
end_score = 0
wr_score = 0

if answer.lower() == "pizza":
    end_score+= 1
    print("Good job!")
else:
    wr_score+= 1
    print("Oops Better luck next time! The answer was Pizza\n")

print("\n2. What is considered very rude and insulting in japanese restaurants\n")

print("Farting")
print("Tipping")
print("Coughing\n")

answer = input("Whats your answer? : ")

if answer.upper() == "Tipping" or answer.lower() == "tipping" :
    end_score+=1
    print("Good job!")
else:
    wr_score += 1
    print("Oops Better luck next time! The answer was Tipping\n")

print("\n3. What do Fifteen percent of Women do during Valentines day?\n")

print("A. Eat chocolate")
print("B. hang out with their significant other")
print("C. Send themselves flowers\n")

answer = input("What is your answer? A, B or C?? : ")

if answer.upper() == "C" or answer.lower() == "c" :
    end_score+=1
    print("Good job!")
else:
    wr_score += 1
    print("Oops Better luck next time! The answer was C\n")

print("\n4. What is the square root of 25?\n")

print("2")
print("6")
print("5\n")

answer = input("What is your answer? :\n ")

if answer.upper() == "5" or answer.upper() == "FIVE":
    end_score+=1
    print("Good job!")
else:
    wr_score += 1
    print("Oops Better luck next time! The answer was 5\n")

print("\n5. What cypher shifts the alphabet one forward?\n")

print("Ceaser cypher")
print("ROT13 Cypher")
print("Affine Cypher\n")

answer = input("What is the correct cypher? : ")

if answer.upper() == "Ceaser Cypher" or answer.lower() == "ceaser cypher" :
    end_score+=1
    print("Good job! Thats the correct answer")
else:
    wr_score += 1
    print("Oops Better luck next time! The answer was Ceaser Cypher\n")

print("\n6. What was Dr. Strange's profession before he became Sorcerer Supreme? ")

print("A. Professor")
print("B. Dermatologist")
print("C. Neurosurgeon\n")

answer = input("Which job is right? : ")

if answer.upper() == "C" or answer.lower() == "c" :
    end_score+=1
    print("Good job! That's the correct answer\n")
else:
    wr_score += 1
    print("Oops Better luck next time! The answer was Neurosurgeon\n")

print("7. Pirates wear eye patches so they could see better in the dark ")

print("True")
print("False\n")

answer = input("Is this true or false? : ")

if answer.upper() == "True" or answer.lower() == "true" :
    end_score+=1
    print("\nGood job! That's the correct answer\n")
else:
    wr_score += 1
    print("\nOops Better luck next time! The answer was True\n")

v1 = (end_score + wr_score)
perc = ((end_score/v1)* 100//1)

print("\nHave a fun time playing! Well this is your end score!\n")

if perc >= 90:
  print("Your grade is an A")
elif perc >=80:
  print("Your grade is a B")
elif perc >= 70:
  print("Your grade is a C")
elif perc >=60:
  print("Your grade is a D")
else:
  print ("Flee to Johnston")

print("\nEnd Score : ", end_score)

print("\n This is your percentage you got right! : ", perc)

