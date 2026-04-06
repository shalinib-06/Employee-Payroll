def calculate_salary(basic_pay):
    hra = 0.2 * basic_pay
    da = 0.1 * basic_pay
    total_salary = basic_pay + hra + da
    tax = 0.05 * total_salary
    net_salary = total_salary - tax
    return net_salary

basic_pay = float(input("Enterthe basic salary: "))
print(f"Net salary: ₹{calculate_salary(basic_pay)}")
