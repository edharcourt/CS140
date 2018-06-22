#Simulation of the birthday paradox
import random
birthdays = []

# initialize a calendar with 366 zeros
for i in range(366):
    birthdays.append(0)

# generate 23 random birthdays
# and count the number of birthdays
# that are the same.
for i in range(100):
    bday = random.randrange(366)
    birthdays[bday] = birthdays[bday] + 1

# see if anyone has the same birthday
i = 0
for count in birthdays:
    if count > 1:
        print(count, "birthdays on day", i)
    i = i + 1

# alternative way to write the above loop
#for i in range(len(birthdays)):
#    if birthdays[i] > 1:
#        print(birthdays[i], 'birthdays on day', i)