from day_17_start.data import question_data
from day_17_start.question_model import Question
from day_17_start.quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

#print(question_bank)
Q = QuizBrain(question_bank)
while Q.still_has_a_question():
    Q.check_ans()

print("you have completed quize!!")
print(f"your final score is {Q.score} / {Q.q_number}")