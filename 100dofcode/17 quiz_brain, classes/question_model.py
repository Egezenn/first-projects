class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuestionExpanded:
    def __init__(self, category, difficulty, question, correct_answer):
        self.category = category
        self.difficulty = difficulty
        self.question = question
        self.answer = correct_answer
