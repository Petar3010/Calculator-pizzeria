print("Today, we are going to choose our new government.")
print("For CDU political formation enter 1 ")
print("For CSU political formation enter 2 ")
print("For SPD political formation enter 3 ")

result_cdu = 0
result_csu = 0
result_spd = 0
all_voted_people = 0

while True:
    user_vote = int(input("Please enter your vote between 1 to 3: "))
    if user_vote == 1 or user_vote == 2 or user_vote == 3:
        all_voted_people += 1
    else:
        print("Invalid vote vote can be only between 1 to 3")
        continue
    if user_vote == 1:
        result_cdu += 1
    elif user_vote == 2:
        result_csu += 1
    elif user_vote == 3:
        result_spd += 1
    if all_voted_people >= 10:
        break


print(f'{result_cdu} people voted for political formation CDU.')
print(f'{result_csu} people voted for political formation CSU.')
print(f'{result_spd} people voted for political formation SPD.')

if result_cdu > result_csu and result_cdu > result_spd:
    print('The winner is political formation CDU.')
    print(f'They have won the elections with {(result_cdu / all_voted_people) * 100}%')
elif result_csu > result_cdu and result_csu > result_spd:
    print('The winner is political formation CSU.')
    print(f'They have won the elections with {(result_csu / all_voted_people) * 100}%')
else:
    print('The winner is political formation SPD.')
    print(f'They have won the elections with {(result_spd / all_voted_people) * 100}%')
