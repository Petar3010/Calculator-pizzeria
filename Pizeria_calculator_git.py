print("Welcome")

fizzy_drink = float(2.0)
little_milk = float(1.2)
big_milk = float(1.7)
little_pad = float(6.0)
big_pad = float(7.0)
little_box = float(6.5)
big_box = float(7.5)
accessory = float(0.5)
asorty = float(1.0)


y_f_d = input("Write how many fizzy drinks did you have yesterday:")
f_d_v = input("Write how many fizzy drinks do you have today:")
t_f_d = float(y_f_d) - float(f_d_v)
t_l_fd = float(t_f_d) * float(fizzy_drink)
print(f"{t_l_fd}")

y_l_m = input("How many little bottles of milks did you have yesterday:")
l_m_v = input("Ho many little bottles of milk do you have today:")
t_l_m = float(y_l_m) - float(l_m_v)
t_l_lm = float(t_l_m) * float(little_milk)
print(f"{t_l_lm}")

y_b_m = input("How many bottles of big milk did you have yesterday:")
b_m_v = input("How many bottles of big milk do you have today:")
t_b_m = float(y_b_m) - float(b_m_v)
t_l_bm = float(t_b_m) * float(big_milk)
print(f"{t_l_bm}")

y_l_p = input("How many little pads did you have yesterday:")
l_p_v = input("How many little pads do you have today:")
t_l_p = float(y_l_p) - float(l_p_v)
t_l_lp = float(t_l_p) * float(little_pad)
print(f"{t_l_lp}")

y_b_p = input("How many big pads did you have yesterday:")
b_p_v = input("How many big pads do you have today:")
t_b_p = float(y_b_p) - float(b_p_v)
t_l_bp = float(t_b_p) * float(big_pad)
print(f"{t_l_bp}")

y_l_b = input("How many little boxes did you have yesterday:")
l_b_v = input("How many little boxes do you have today:")
t_l_b = float(y_l_b) - float(l_b_v)
t_l_lb = float(t_l_b) * float(little_box)
print(f"{t_l_lb}")

y_b_b = input("How many big boxes did you have yesterday:")
t_b_b = input("How many big boxes do you have today:")
tot_b_b = float(y_b_b) - float(t_b_b)
t_l_bb = float(tot_b_b) * float(big_box)
print(f"{t_l_bb}")


a_v = input("How many pizzas assorti have you sold today:")
t_l_a = float(a_v) * float(asorty)
print(f"{t_l_a}")

ac_v = input("How many accessories have you sold today:")
t_l_ac = float(ac_v) * float(accessory)
print(f"{t_l_ac}")

cash_desk = input("How much money did you have yesterday in cash desk:")
c_d_l = float(cash_desk)

first_turnover = float(t_l_fd) + float(t_l_lm) + float(t_l_bm) + float(t_l_lp)

second_turnover = float(t_l_bp) + float(t_l_lb) + float(t_l_bb)

third_turnover = float(t_l_a) + float(t_l_ac) + float(c_d_l)

Total_turnover = float(first_turnover) + float(second_turnover) + float(third_turnover)
print(f" your turnover is {Total_turnover}")

expenses = input("Write your expenses:")

money_on_hand = float(Total_turnover) - float(expenses)
print(f"You should have {money_on_hand} money on hand")