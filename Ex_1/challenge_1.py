print("Today's date?")
Today_date= str(input())
print("Breakfast_calories?")
Breakfast_calories = int(input())
print("Lunch_calories?")
Lunch_calories =int(input())
print("Dinner_calories?")
Dinner_calories = int(input())
print("Snack_calories?")
Snack_calories= int(input())
sum= Breakfast_calories +Lunch_calories+Snack_calories+Dinner_calories
print('Calorie content for {}: {}'.format(Today_date,sum))