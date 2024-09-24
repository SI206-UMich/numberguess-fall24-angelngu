# Your name: Angel Nguyen
# Your student id:62543280
# Your email: angelngu@umich.edu 
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.  
# e.g.:
#i asked chat GPT to help me structure the format for the sections especialy with check_get_answer and help me with debugging when there were errors or when the index was out of range  
#i also asked it to help check my test codes and extra credit 

import random 
# create a Digital Book of Answers
class DigitalBookofAnswers():
    # create the constructor (__init__) method 
    # ARGUMENTS: 
    #       self: the current object
    #       answers: a list of potential answers
    # RETURNS: None
    def __init__(self, answers):
        self.book_answer_list= answers
        self.questions_asked_list = []
        self.answered_list=[] #sets empty list 

        pass

    # Create the __str__ method
    # ARGUMENTS: 
    #       self: the curent object
    # RETURNS: a string
    def __str__(self):
        if not self.book_answer_list:
            return ""
        return " - ".join(self.book_answer_list)

        pass

    # Creates the check_get_answer method
    # ARGUMENTS:
    #       self: the current object
    #       question: the question the user wants to ask the digital book of answers
    # RETURNS: a string
    def check_get_answer(self, question): #i used chatgpt on this section becasue i coild not figure out why my lsit was out of range 
        if question in self.questions_asked_list: #find index of question in questions_aksed_list
            index = self.questions_asked_list.index(question) #find the index of the question and return index
            if index <len(self.answered_list):
                answer_index= self.answered_list[index]
                return f"I've already answered this question. The answer is: {answer_index}" 
        answer_index= random.randint(0,len(self.book_answer_list) - 1) #if its a new question
        self.questions_asked_list.append(question)
        self.answered_list.append(answer_index)
        return self.book_answer_list[answer_index]
    
    # Creates open_book method
    # ARGUMENTS:
    #   self: the current object
    # RETURNS: None
    def open_book(self): #for loop for books
        while True: 
            turn_number=len(self.questions_asked_list) +1
            question =input(f"Turn {turn_number} - Please enter your question: ")
            if question == "Done":
                print ("Goodbye! See you soon.")
                break
            else:
                answer = self.check_get_answer(question)
                print(answer)

        pass


    # Create the answer_log method
    # ARGUMENTS: 
    #       self: the curent object
    # RETURNS: a list
    def answer_log(self):
        answer_counts = {}
        for index in self.answered_list:
            answer = self.book_answer_list[index].lower()
            if answer in answer_counts:
                answer_counts[answer] +=1
            else:
                answer_counts[answer] =1
        result = [f"{count} - {answer}" for answer, count in answer_counts.items()]
        #return the frequency list
        return result 

        pass


def test():
    answers_list = ['Believe in Yourself', 'Stay Open to the Future', 'Enjoy It']
    book = DigitalBookofAnswers(answers_list)

    print("Test __init__:")
    print(f"Answer History List: Expected: {[]}, Actual: {book.answered_list}")
    print(f"Question History List: Expected: {[]}, Actual: {book.questions_asked_list}")
    print(" ")

    print("Test __str__:")
    expected = "Belive in Yourself - Stay Open to the Future - Enjoy It"
    print(f"Expected: {expected}, Actual: {str(book)}")
    print(" ")
    
    empty_book = DigitalBookofAnswers([])
    print("Test __str__: when it's an empty book without possible answers")
    expected = ""
    print(f"Expected: {expected}, Actual: {str(empty_book)}")
    print(" ")

    print("Testing return value of check_get_answer:")
    res = book.check_get_answer('test question')
    print(f"Expected: {str}, Actual: {type(res)}")
    print(" ")

    print("Testing check_get_answer")
    book.book_answer_list = ['Go For It']
    res = book.check_get_answer('test question 2')
    print(f"Expected: {'Go For It'}, Actual: {res}")
    print(" ")

    print("Testing that check_get_answer adds answer index to answered_list:")
    book.book_answer_list = ['Go For It']
    book.answered_list = []
    book.check_get_answer('test question 2')
    expected = [0]
    res = book.answered_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing that check_get_answer does not add 'I've already answered this question' part to answered_list:")
    book.book_answer_list = ['Believe In Yourself']
    book.answered_list = [0]
    book.questions_asked_list = ['test question 3']
    book.check_get_answer('test question 3')
    expected = [0]
    res = book.answered_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")


    print("Testing return value answer_log")
    book.book_answer_list = ['Follow Your Inner Voice', 'Stay Positive', 'Go For It']
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = type(book.answer_log())
    print(f"Expected: {list}, Actual: {res}")
    print(" ")

    print("Testing return value answer_log elements")
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = type(book.answer_log()[0])
    print(f"Expected: {str}, Actual: {res}")
    print(" ")

    print("Testing answer_log")
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = book.answer_log()
    expected = ['3 - follow your inner voice', '2 - stay positive', '1 - go for it']
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing empty answer_log")
    book.answered_list = []
    res = book.answer_log()
    expected = []
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")



# Extra Credit
def my_test():
    # Put your test code here
    answers_list = ['Stay Positive', 'Go For It', 'Enjoy It']
    book = DigitalBookofAnswers(answers_list)

    assert book.answer_log() == [], "Expected empty log"

    book.answered_list = [2, 1, 2]
    expected_log = ['2 - enjoy it', '1 - go for it']
    assert book.answer_log() == expected_log, f"Expected: {expected_log}, got: {book.answer_log()}"

    question= "is this a test" #correct output when new question is asked in check_get_answer
    response = book.check_get_answer(question) 
    assert "I've already answered this question" not in response, "Expected new question response"

     #correct output when same question is asked in check_get_answer
    repeat_response = book.check_get_answer(question) 
    assert "I've already answered this question" in repeat_response, "Expected repeated question response"
    print ("All tests passed")

    pass



def main():
    pass
    answers_list= [
        'Follow Your Inner Voice',
        'Stay Positive',
        'Go For It',
        'Believe in Yourself',
        'Stay Open to the Future',
        'Enjoy It'
    ]

    book= DigitalBookofAnswers(answers_list)

    book.open_book()

    log_output =book.answer_log()
    print("Answer Log Output:")
    for entry in log_output:
        print(entry)

# Only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    test() 
    my_test() #TODO: Uncomment if you do the extra credit
    