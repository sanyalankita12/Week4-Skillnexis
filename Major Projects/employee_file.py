import pandas as pd

data=pd.read_csv(r"C:\Users\Ishit\PycharmProjects\PythonProject8\Major Projects\employee_salary_dataset.csv")

def average_salary():
    avg_salary = data['Monthly_Salary'].mean()
    print(f"Average Salary : {avg_salary}")

def department_counting():
    department_count=data['Department'].value_counts()
    print(f"Department count : {department_count}")

def highest_salary_filter():
    filtering_employees=data[data['Monthly_Salary']>65000]
    filtering_employees.to_csv(r"C:\Users\Ishit\PycharmProjects\PythonProject8\Major Projects\output.csv")
    print("Highest Salary Employees added successfully to output.csv")

def main():
        print("=" * 35)
        print("       Employee Data Analysis Project")
        print("=" * 35)
        average_salary()
        print("=" * 35)
        department_counting()
        print("=" * 35)
        highest_salary_filter()



main()