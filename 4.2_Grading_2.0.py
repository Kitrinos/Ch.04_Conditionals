'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

sg = float(input("Hey whats your current Semester Grade?"))

fg = float(input("Hey whats your final exam grade?"))

ew = float(input("How much does the exam weigh?"))
ew/= 100

o = (sg * (1 - ew) + fg * (ew))

if o >= 90:
  print("Your grade is an A")
elif o >=80:
  print("Your grade is a B")
elif o >= 70:
  print("Your grade is a C")
elif o >=60:
  print("Your grade is a D")
else:
  print ("Flee to Johnston")

print("This is your grade percentage! : ", o)