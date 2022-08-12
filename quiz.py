print("Welcome to my computer quiz!")
score = 0

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print ("Okay! Let's Play :)")

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the name of the tallest mountain? ")
if answer.lower() == "mount everest":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which game has reached 1 trillion views on Youtube? ")
if answer.lower() == "minecraft":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which Country has more obese people than bycycles? ")
if answer.lower() == ("usa"):
    print('Correct!')
    score+= 1
else:
    print("Incorrect!")

print("You Got "+ str(score) + " questions correct!")
print("You got" + str((score/4) * 100)+ " %")




