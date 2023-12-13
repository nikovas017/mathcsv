import csv 

import random 

  

def create_question(): 

    num1 = random.randint(1, 10) 

    num2 = random.randint(1, 10) 

    operation = random.choice(['+', '-', '*', '/']) 

    question = "{} {} {}".format(num1, operation, num2) 

    answer = eval(question) 

    return question, answer 

  

def take_quiz(): 

    name = input("Enter your name: ") 

    correct_answers = 0 

  

    for _ in range(5): 

        question, answer = create_question() 

        user_answer = float(input("What is " + question + "? ")) 

        

        if user_answer == answer: 

            correct_answers += 1 

  

    percentage = (correct_answers / 5) * 100 

    print("\n" + name + " got " + str(correct_answers) + " out of 5 questions right\nPercentage = " + str(percentage) + "%\n") 

  

    file = open("check_answers.csv",'a')

    output =([name,answer,"out of",correct_answers, '/5', percentage,"%"])
    file.write(output)
    file.close()


  

def check_answer(): 

    try: 

        file=open('check_answers.csv','r')
        for row in file:
            print(row)

            

    except FileNotFoundError: 

        print("\nNo quiz results found.\n") 

  

def main(): 

    while True: 

        print("Menu:\n1) Take the Quiz\n2) View Results (from CSV)\n3) Exit") 

        choice = input("Enter your choice (1/2/3): ") 

  

        if choice == '1': 

            take_quiz() 

        elif choice == '2': 

            check_answer() 

        elif choice == '3': 

            break 

        else: 

            print("Invalid choice. Please enter 1, 2, or 3.") 

  

if __name__ == "__main__": 

    main() 

 