employee = input("Employee name: ")
rendered_hours = input("Rendered hours: ")
sss = input("SSS Contribution: ")
phil = input("Philhealth: ")
housing = input("Housing loan: ")
rate_perHour = 500

print("\n")
print("=======PAYSLIP======")
print("=========EMPLOYEE INFO========")
print("Employee Name: %s"%(employee))
print("Rendered Hours: %s"%(rendered_hours))
print("Rate per hour: %s"%(rate_perHour))

#calculation for Gross Salary
gross_salary = float(rate_perHour) * float(rendered_hours)

print("Gross Salary: {}".format(gross_salary))
print("==========DEDUCTIONS========")
print("SSS: %s"%(sss))
print("Philhealth: %s"%(phil))
print("Housing: %s"%(housing))

#calculation for Tax
tax = gross_salary * .10
tax_update = int(tax)
print("Tax: %s"%(tax_update))

#calculation for total deduction
amount_toDeduct = int(sss) + int(phil) + int(housing) + tax_update
print("Total Deductions: {}".format(amount_toDeduct))

#Calculation for Net Salary 
total_deduct = gross_salary - amount_toDeduct

print("Net Salary: PHP {}".format(total_deduct))


