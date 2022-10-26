class QuizBrain:
	def __init__(self,q_list):
		self.number = 0
		self.question = q_list
		self.score = 0
	
	def still_has_questions(self):
		return self.number < len(self.question)
		
	def nextQuestion(self):
		current_q = self.question[self.number]
		self.number += 1
		user_answer = input(f"Q.{self.number}: {current_q.text} (True/False)?: ")
		self.checkAnswer(user_answer, current_q.answer)

	def checkAnswer(self,user_answer,current_answer):
		if user_answer.lower() == current_answer.lower():
			print("You got it right!")
			self.score += 1	
		else:
			print("That's Wrong.")
		print(f"The currect answer is {current_answer}")
		print(f"Your current score is: {self.score}/{self.number}\n.")
		
		