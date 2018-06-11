
investments = 798000
ror = .04
salary = 100000
invest_per_year = .21
SLU_match = .10
salary_increase_per_year = .02
retire_age = 67
age = 54

print("age", '\t', "Salary", '\t', "Investments")
print("----------------------------------------")

for i in range(age,retire_age + 1):
    investments = investments * (1 + ror)
    investments = investments + salary*invest_per_year + salary*SLU_match
    salary = salary * (1 + salary_increase_per_year)
    print(i, '\t\t', int(salary), '\t\t', int(investments))


# retirement spending

spend_rate = .04
inflation = .02
age = 67
spend = investments * spend_rate

print('\n\n', 'age', '\t', 'Spend', '\t\t', 'Investments')
print('-------------------------------------------------------------------')
while investments > 0:
    print(age, '\t\t', int(spend), '\t\t', int(investments))
    investments = investments - spend
    investments = investments * (1.02)
    spend = spend * (1 + inflation)
    age = age + 1

