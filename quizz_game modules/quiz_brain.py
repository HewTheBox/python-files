class QuizBrain:
    def __init__(self,q_list):
        self.number = 0
        self.question_list = q_list
        self.score = 0
        
        
    def still_has_questions(self):
        """Returns True if there are still quenstions in the question bank"""
        return self.number < len(self.question_list)
        
        
        
    def nextQuestion(self):
        """Prints the next question to the user"""
    
        current_question = self.question_list[self.number]
        self.number +=1
        user_answer = input(f"Q{self.number}: {current_question.text}? (True/False): ")
        self.check_answer(user_answer,current_question.answer)
        
        
        
    def check_answer(self,user_answer,correct_answer):
        """validates the answer provided by the user
            Keep track of the current score 
        """
        if user_answer.lower() == correct_answer.lower():
            print("You got right!")
            self.score +=1
            
        else: 
            print("That's wrong.")
            
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.number}")
        print("\n")
        
    
    

