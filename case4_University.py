
# Case 4: Employee Payroll and Deduction Analysis

employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))

hra = basic_salary * 0.20
allowance = basic_salary * 0.10

gross_salary = basic_salary + hra + allowance

pf = basic_salary * 0.05
insurance = basic_salary * 0.02

total_deductions = pf + insurance
net_salary = gross_salary - total_deductions

print("\n--- Employee Payroll Report ---")
print("Employee:", employee_name)
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("Allowance:", allowance)
print("Gross Salary:", gross_salary)
print("PF Deduction:", pf)
print("Insurance Deduction:", insurance)
print("Total Deductions:", total_deductions)
print("Net Salary:", net_salary)
