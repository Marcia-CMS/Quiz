print("Welcome to Marcia, Shannon & Paddy's IS quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does IS stand for? ")
if answer.lower() == "Information Systems":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does BI stand for? ")
if answer.lower() == "Business Intelligence":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
