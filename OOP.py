import json
import os
from random import shuffle

amount_of_points = 0

class Question():

    def __init__(self, question, complexity, correct_answer):
        self.question = question
        self.complexity = complexity
        self.correct_answer = correct_answer
        self.correct = False
        self.answer_of_user = None
        self.question_points = self.complexity * 10

    def get_points(self):
        return self.question_points

    def is_true(self):
        return self.answer_of_user.lower() == self.correct_answer.lower()

    def build_question(self):
        print(f"{self.question}\nDifficulty {self.complexity}/5")

    def build_feedback(self):
        global amount_of_points
        if self.is_true():
            amount_of_points += self.get_points()
            self.correct = True
            print(f"The answer is correct! You got +{self.get_points()} points")
        else:
            print(f"The answer is wrong! The correct answer is : {self.correct_answer}")


def load_questions():
    questions = []
    with open("questions.json", encoding='utf-8') as file:
        data = json.load(file)
        for question in data:
            difficult = int(question["difficult"])
            temp_object = Question(question["question"], difficult, question["answer"])
            questions.append(temp_object)
    return questions


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def display_statistics(questions):
    print("That's all ^_^")
    correct_user_answer = 0
    for task in questions:
        if task.correct == True:
            correct_user_answer += 1
    print(f"The correct answer was given to {correct_user_answer}/{len(questions)}")
    print(f"Total points scored : {amount_of_points}")


questions = load_questions()
shuffle(questions)

print("Hello!\nI propose to play a game)\nPress Enter if you are ready ... ", end="")
input()

for task in questions:
    clear_console()
    task.build_question()
    task.answer_of_user = input("Your answer = ")
    task.build_feedback()
    print("Press Enter to continue ...", end = "")
    input()

clear_console()
display_statistics(questions)