# calculador de vida 
age = input("What is your current age? ")


#age_num = int(age)
#days_life = int(365 * 90)
#week_life = int(52)
#month_life = int(12)

#result_dayslife = int((days_life) - age_num * 365 )
#result_weeklife = int((week_life * 90) - (week_life * age_num))
#result_monthlife = int((month_life * 90) - (month_life * age_num)) 
age_num = int(age)
years_remaining = 90 - age_num
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12


message= (f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
print(message)