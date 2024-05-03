import random


def game(user_choice, computer_user_choice, user_score,computer_score):
    if user_choice==1 and computer_user_choice==2:
        computer_score+=1
    elif user_choice==1 and computer_user_choice==3:
        user_score+=1
    elif user_choice==2 and computer_user_choice==1:
        computer_score+=1
    elif user_choice==2 and computer_user_choice==3:
        user_score+=1
    elif user_choice==3 and computer_user_choice==1:
        computer_score+=1
    else:
        user_score+=1
    return user_score,computer_score



def main():
    user_score = 0
    computer_score = 0
    while True:
        try:


            user_choice = int(input("Enter \n1. rock \n2. paper\n3.scissor\n4. Quit\n"))
            if user_choice not in [1,2,3,4]:
                raise ValueError("Invalid user_choice")
            computer_user_choice = random.randrange(1,4)
            if user_choice==4:
                if(user_score>computer_score):
                    print("User wins")
                else:
                    print("Computer wins")
                exit()

            user_score,computer_score= game(user_choice,computer_user_choice,user_score,computer_score)
            game_dict ={
                1:"rock",
                2:"paper",
                3:"scissor"
            }

            print(f"You choose: {game_dict[user_choice]}, Computer choose : {game_dict[computer_user_choice]}")
            print(f"User : {user_score} , Computer : {computer_score}")


        except ValueError:
            print("Enter appropriate user_choice")


if __name__== "__main__":
    main()