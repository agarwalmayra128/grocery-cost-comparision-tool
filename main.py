print("===GROCERY COST COMPARISION TOOL===")
rice_price = 12
milk_price = 4
fruit_price = 8
number_of_baskets = 2
family_members = 4
basket_cost_per_person = (rice_price + milk_price + fruit_price) * number_of_baskets / family_numbers
total_items = int(input("enter the total number of grocery items: "))
people = it(input("enter the number of people sharing them: "))
if people == 0:
    print("you cannot share items among 0 people.")
else:
    if items % people == 0:
        print(total_items,"items do not divide equally among", people,"people -", total_items % people, "left over")
recorded_average = 65
total_weeks = 4
wrong_week_cost = 50
correct_week_cost = 80
recorded_total = recorded_average * total_weeks 
corrected_total = recorded_total - wrong_week_cost + correct_week_cost
corrected_average = corrected_total / total_weeks
store_a_average = 70
store_b_average = 75
store_c_average = 80
if corrected_average < store_a_average and corrected_average < store_b_average and corrected_average < store_C_average:
     verdict = "more expensive than all three stores"
     print("===SUMMARY===")
     print("cost per person this week:", basket_cost_per_person)
     print("corrected weekly average:", corrected_average)
     print("verdict:", verdict)