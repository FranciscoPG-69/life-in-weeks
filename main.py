# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_num = int(age)
days_life = int(365 * 90)
week_life = int(52)
month_life = int(12)

result_dayslife = int((days_life) - age_num * 365 )
result_weeklife = int((week_life * 90) - (week_life * age_num))
result_monthlife = int((month_life * 90) - (month_life * age_num)) 

print(f"You have {result_dayslife} days, {result_weeklife} weeks, and {result_monthlife} months left.")