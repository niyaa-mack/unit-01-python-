total_payroll = 0 
employees = 12
for i in range(employees):
    print(f"Employee {i+1}")
    company_name = input("Enter company name: ")
    num_employees = int(input("Enter number of employees: "))
    hourly_py = int(input("how much you get paid an hour:"))
    num_hours = int(input("Hours that you work:"))
    num_overtime = int(input("Overtime hours:"))
if num_hours > 40: 
    print("The max of hours you can work is 40")

    payroll = hourly_py * num_hours
    overtime_hours = num_overtime * hourly_py * 1.5 
    total_pay = payroll + overtime_hours

    print(f"{num_employees}'s total pay: ${total_payroll:.2f}")
    total_payroll += total_pay



    