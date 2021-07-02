class QuizBrain:
    def __init__(self,q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_a_question(self):
        if self.q_number >= len(self.q_list):
            return False
        return True

    def next_q(self):
        answer = input(f"Q{self.q_number+1}:{self.q_list[self.q_number].text}(true/false)? : ").lower()
        self.q_number+=1
        return answer
    def check_ans(self):
        if self.next_q()==self.q_list[self.q_number-1].ans.lower():
             self.score+=1
             print("you are right 😎")

        else:
            print("that's wrong.")
        print(f"correct answer is {self.q_list[self.q_number-1].ans}")
        print(f"your current score is {self.score} / {self.q_number}")
        print("\n")



