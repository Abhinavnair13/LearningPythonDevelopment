
questions = [
    {
        "prompt": "What is the capital of france",
        "options": ["A. Paris","B. Tokyo","C. Pittsburg","D. Delhi"],
        "answer": "A"
    } ,{
        "prompt": "What is the language spoken in brazil",
        "options": ["A. Spanish","B. Portuguese","C. English","D. hindi"],
        "answer": "B"
    }
]
def run_quiz(questions):
    score =0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer A,B,C or D : ").upper()
        if(answer==question["answer"]):
            score+=1
    print(f"your score is {score} out of {len(questions)}")


run_quiz(questions)