print("Welcome to the Quiz")
print("Each correct answer will get 10 points and there is NO negative marking")

score = 0 

print("Question 1: How many days are there in a week ?")
print("Option a :- 6")
print("Option b :- 7")
print("Option c :- 8")
print("Option d :- 9")

a = (input("Enter the answer: ")).lower()

if a == 'b':
    print("Correct Answer")
    score = score + 10
else :
    print("Wrong Answer")

print("Your current score is:",score)  

print("Question 2: How many seconds are there in a 1 min ?")
print("Option a :- 60")
print("Option b :- 70")
print("Option c :- 80")
print("Option d :- 90")

a = (input("Enter the answer: ")).lower()

if a == 'a':
    print("Correct Answer")
    score = score + 10
else :
    print("Wrong Answer")

print("Your current score is:",score)

print("YOUR QUIZ is COMPLETED")
print(f"Your final score is: {score} out of 20")