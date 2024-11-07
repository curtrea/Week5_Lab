def employee_pay(): 1 usage*
    hourly_rate = float(input(f'Please enter your hourly rate, e.g. 10.59: ')
    num_hours_worked = input(f'Please enter your number of hours worked, e.g. 21.5'))
    emp_pay = hourly_rate * num_hours_worked
    emp_pay = f'£ {emp_pay}'
    return emp_pay

"""
list_of_ages = [20,21.24,13,15,19,22]
1. Add all ages together
1. Get number of ages
3. Take the sum from 1, and divide it by 2:
4. Return the outpyt value in 3

"""
def average_age(ages_list:list): 1 usage
    """"
:param ages_list: should a list of ages, expecting the data type
    :return: average age in float
"""

sum_ages =sum(ages_list) # This will give us the sum of the ages
num_ages =len(ages_list) # Get number of ages in the list
avg_list = sum_ages / num_ages # This is the average age
    return avg_list

list_ages_1 = [20,21.24,13,15,19,22]
avg_age = average_age(list_ages_1)
print(f'The average age is {abg_age} years')

#Test employee_pay code
empy_pay = employee_pay()
print(f'Employee Pay is {empy_pay}')



