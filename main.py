import random
import time

OPERATORS = ["+","-","/","*"]
Min_operand = 2
Max_operand = 9
Total_rounds = 5

def generate():
    left = random.randint(2, 9)
    right = random.randint(2, 9)
    oper = random.choice(OPERATORS)
    expr = str(left) + " "+oper+" "+str(right)
    answer = eval(expr)

    return expr,answer

def main():
    input("Press enter to start ")
    print("----------------------")
    start_time = time.time()

    correct_answer=0
    for i in range(Total_rounds):
        expr,answer = generate()
        print("Problem #"+str(i+1)+" "+expr+" : ")
        try:
            user_answer= int(input())
            if (user_answer == answer):
                correct_answer+=1


        except ValueError as ve:
            print("Invalid number",ve)
            break
    accuracy  = (correct_answer/Total_rounds)*100
    end_time = time.time()
    print("You completed the quiz in "+str(round(end_time-start_time,2))+" seconds with "+str(accuracy)+"% accuracy." )




if __name__=="__main__":
    main()
