# 10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary = int(input("Salary: "))
years = int(input("Years of service: "))
if years > 5:
    bonus = salary * 0.05
    print(f"Bonus: {bonus}")