# Write a function that takes a list of employee salaries and calculates the average salary.

def calculate_average_salary(salaries):
    if len(salaries) == 0:
        return 0  
    return sum(salaries) / len(salaries)

salaries = [50000, 60000, 55000, 70000, 80000]
average_salary = calculate_average_salary(salaries)
print("Average Salary:", average_salary)
