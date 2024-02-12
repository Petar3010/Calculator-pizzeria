print("Hello, today we are going to choose our new government.")
print("gerb = 1, pp = 2, bsp = 3, dps = 4, vuzrajdane = 5, itn = 6")

gerb = float(2)
pp = float(1.8)
bsp = float(1.4)
dps = float(1.9)
vuzrajdane = float(1.2)
itn = float(1.7)

vote_choose = float(1)

while True:
    try:
        user_vote = float(input("Enter your vote:"))
        if 1 <= user_vote <= 6:
            if user_vote == 1:
                result_vote = vote_choose * gerb
                print(f"You gave {result_vote} vote for gerb")
            elif user_vote == 2:
                result_vote = vote_choose * pp
                print(f"You gave {result_vote} vote for pp")
            elif user_vote == 3:
                result_vote = vote_choose * bsp
                print(f"You gave {result_vote} vote for bsp")
            elif user_vote == 4:
                 result_vote = vote_choose * dps
                 print(f"You gave {result_vote} vote for dps")
            elif user_vote == 5:
                 result_vote = vote_choose * vuzrajdane
                 print(f"You gave {result_vote} vote for vuzrajdane")
            elif user_vote == 6:
                 result_vote = vote_choose * itn
                 print(f"You gave {result_vote} vote for itn")
            break

        else:
            print("You must chose number between 1 to 6")
    except ValueError:
        print("You can enter only number between 1 to 6. You can't enter letter.")
