from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
	question = Question(q["question"],q["correct_answer"])
	question_bank.append(question)
quiz = QuizBrain(question_bank)
while(quiz.still_has_questions()):
	quiz.nextQuestion()

print("\nYou completed the Quiz")
print(f"Your final score was: {quiz.score}/{quiz.number}")