print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay! Let's play:)")
score = 0

# question 1
answer = input("What does CPU stand for? ") 

if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print('wrong answer!')

# question 2
answer = input("What does GPU stand for? ") 

if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print('wrong answer!')

#  question 3
answer = input("what does RAM stand for? ") 

if answer.lower() == "random access memory":
    print('correct!')
    score += 1
else:
    print('wrong answer!')

# question 4
answer = input("what does PSU stand for? ") 

if answer.lower() == "power supply":
    print('correct!')
    score += 1
else:
    print('wrong answer!')

print("you got " +str(score)+ " questions correct!")
print("you got " +str((score / 4) * 100)+ "%.")