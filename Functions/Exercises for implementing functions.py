def get_employee_details():
    name = input ("Enter Employee Name: ")
    emp_id = input("Enter Employee Id: ")
    dpmt = input ("Enter Department: ")
    basic_salary = float(input("Enter Salary: "))
    return name, emp_id, dpmt ,basic_salary

def calc_sal(basic_salary):
    h=basic_salary * 0.20
    da=basic_salary * 0.10
    pf=basic_salary * 0.12

    gross_salary = basic_salary + h + da
    net_salary = gross_salary - pf

    return h,da,pf,gross_salary,net_salary
def print_salary_slip(name,emp_id,dpmt,basic,h,da,pf,gross,net):
    print ("\n==============EMPLOYEE SALARY SLIP=====================")
    print ("Employee Name:",name)
    print ("Employee Id:",emp_id)
    print ("Department;", dpmt)
    print ("-----------------------------------------------")
    print ("Basic Salary : Rs.",basic)
    print ("HRA (20%) : Rs.",h)
    print ("DA(10%) : Rs.", da)
    print ("PF Deduction :Rs.",pf)
    print ("-----------------------------------------------")
    print ("Gross Salary:Rs.",gross)
    print ("Net Salary: Rs.", net)
    print ("=======================================================")


name, emp_id, department, basic = get_employee_details()
h, da, pf, gross, net = calc_sal(basic)
print_salary_slip(name, emp_id, department, basic, h, da, pf, gross, net)


o/p:
Enter Employee Name: Akshaya
Enter Employee Id: 004
Enter Department: Hr
Enter Salary: 150000

==============EMPLOYEE SALARY SLIP=====================
Employee Name: Akshaya
Employee Id: 004
Department; Hr
-----------------------------------------------
Basic Salary : Rs. 150000.0
HRA (20%) : Rs. 30000.0
DA(10%) : Rs. 15000.0
PF Deduction :Rs. 18000.0
-----------------------------------------------
Gross Salary:Rs. 195000.0
Net Salary: Rs. 177000.0
=======================================================
