from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create the question bank
question_bank = []
for question in question_data:
    question_text = question["question"]
    answer_text = question["correct_answer"]
    new_question = Question(question_text, answer_text)
    question_bank.append(new_question)

# Initialize the quiz
quiz = QuizBrain(question_bank)

# Game loop
while quiz.still_has_questions():
    quiz.next_question()

# End of the game
print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
