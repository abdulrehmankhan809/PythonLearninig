import random
Word_List=["pakistan","karachi","punjab","province"]
Choosen_Word=random.choice(Word_List)
print(Choosen_Word)
Display=[]
Lives=6
for i in range(len(Choosen_Word)):
    Display.insert(i,"_")
print(Display)
End_of_Game=False
while not End_of_Game:

    guess = input("Guess letter ").lower()

    for possition in range(len(Choosen_Word)):
        letter = Choosen_Word[possition]
        if guess==letter:
            Display[possition]=guess
    print(Display)
    if guess not in Choosen_Word:
        Lives-=1
    if Lives==0:
        End_of_Game=True
        print("You Lose The Game")
    if "_" not in Display:
        End_of_Game= True
        print("You Win")

