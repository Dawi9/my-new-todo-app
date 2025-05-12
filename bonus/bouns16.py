import json

from main import message

with open("files/questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your choice: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        question ["result"] = "Correct"
    else:
        question ["result"] = "Wrong"

for index, question in enumerate (data):
    message = f"{index + 1} {question ["result"]} - Your answer: {question['user_choice']}, " \
               f"Correct answer: {question['correct_answer']}"
    print(message)
print(f"Your score is: {score}", "/", len(data))