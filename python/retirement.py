
investments = 798000
ror = .03
salary = 100000
invest_per_year = .21
SLU_match = .10
salary_increase_per_year = .02
retire_age = 67
age = 54

print("age", '\t', "Salary", '\t', "Investments")
print("----------------------------------------")

for i in range(age,retire_age + 1):
    print(i, '\t\t', int(salary), '\t\t', int(investments))

    # investment return
    investments = investments * (1 + ror)

    # add in new contributions
    investments = investments + salary*invest_per_year + salary*SLU_match

    # update new salary
    salary = salary * (1 + salary_increase_per_year)


# retirement spending

spend_rate = .04  # spend 4% per year
inflation = .02   # rate of inflation
age = 67          # retirement age
spend = investments * spend_rate   # initial amount to spend

print('\n\n', 'age', '\t', 'Spend', '\t\t', 'Investments')
print('-------------------------------------------------------------------')
while investments > 0:
    print(age, '\t\t', int(spend), '\t\t', int(investments))

    # portfolio after yearly withdrawal
    investments = investments - spend

    # portfolio should still be gaining interest
    investments = investments * (1.02)

    # need to increase spending by rate of inflation
    spend = spend * (1 + inflation)
    age = age + 1

