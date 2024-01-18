import random

print("""Welcome to the game of hand cricket
Rules:
1) The winner of the toss chooses to bat.
2) For batting or bowling you have to choose any number form 1 to 6.
3) If you choose same number its an out otherwise the number which the batsman which will choose will add to the run.""")

toss=["heads","tails"]

while True:
    n=input("Choose heads or tails: ").lower()
    if n=="heads":
        d="tails"
        print("Computer choice is ",d)
        break
    elif n=="tails":
        d="heads"
        print("computer choice is ",d)
        break
    else:
        print("Wrong choice!! Try again.")
    

s=random.choice(toss)
l1=[1,2,3,4,5,6]

while True:
    if s==n:
        print(f"""The toss outcome is {s}.
You win and will bat first""")
        
        run1=0
        while True:
            r1=int(input("Choose any number from 1 to 6: "))
            if r1>6:
                print("try again!!")
                continue
            r2=random.choice(l1)
            print(f"Computer choice is {r2}.")
            print(f"{r1} runs")
            run1=run1+r1
            if r1==r2:
                break
        print(f"""Out!! Now computer will bat.
Your score is {run1} runs.""")

        run2=0
        while True:
            r1=int(input("Choose any number from 1 to 6: "))
            if r1>6:
                print("try again!!")
                continue
            r2=random.choice(l1)
            print(f"Computer choice is {r2}.")
            print(f"{r2} runs")
            run2+=r2
            if run2>run1:
                break
            if r1==r2:
                print("Out!!")
                break
        print(f"""Game over!!
Computer scores {run2} runs.""")
        
            
    elif s==d:
        print(f"""The toss outcome is {s}.
Computer wins and chooses to bat first""")
        run2=0
        while True:
            r1=int(input("Choose any number from 1 to 6: "))
            if r1>6:
                print("try again!!")
                continue
            r2=random.choice(l1)
            print(f"Computer choice is {r2}.")
            print(f"{r2} runs")
            run2+=r2
            if r1==r2:
                break
        print(f"""Out!! Now you will bat.
Computer score is {run2} runs.""")

        run1=0
        while True:
            r1=int(input("Choose any number from 1 to 6: "))
            if r1>6:
                print("try again!!")
                continue
            r2=random.choice(l1)
            print(f"Computer choice is {r2}.")
            print(f"{r1} runs")
            run1=run1+r1
            if run1>run2:
                break
            if r1==r2:
                print("Out!!")
                break
        print(f"""Game over!!
You score {run1} runs.""")
        

    if run1>run2:
        print("You win!!")
    elif run1<run2:
        print("Computer wins!!")
    elif run1==run2:
        print("Match tie")

    q=input("Do you want to play again(Y/N)?: ").upper()
    if q=="N":
        break
