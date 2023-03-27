import math

    

def gross(grossSalary):
        return int(grossSalary)
    
def epf(grossSalary):
        return math.ceil(int(grossSalary)*0.08)

def calc_tax(grossSalary, rate, k):
        tax = math.ceil(grossSalary * rate) - k
        return tax
		
def print_salary(grossSalary, epf, tax):
        netSalary = grossSalary - (epf + tax)
        print(f"EPF deduction \t        = {epf}")
        print(f"Tax deduction \t        = {tax}")
        print(f"\nNet Salary \t        = {netSalary}\n")

def calc_sal(grossSalary):
    if(grossSalary < 100000):
        tax = 0	
        print_salary(grossSalary, epf,tax)	

    elif((grossSalary >= 100000) & (grossSalary < 141667)):
        tax = calc_tax(grossSalary, 0.06, 6000)
        print_salary(grossSalary, epf,tax)	

    elif((grossSalary >= 141667) & (grossSalary < 183333)):
        tax = calc_tax(grossSalary, 0.12, 14500)
        print_salary(grossSalary, epf,tax)	

    elif((grossSalary >= 183333) & (grossSalary < 225000)):
        tax = calc_tax(grossSalary, 0.18, 25500)
        print_salary(grossSalary, epf,tax)	

    elif((grossSalary >= 225000) & (grossSalary < 266667)):
        tax = calc_tax(grossSalary, 0.24, 39000)
        print_salary(grossSalary, epf,tax)	

    elif((grossSalary >= 266667) & (grossSalary < 308333)):
        tax = calc_tax(grossSalary, 0.3, 55000)
        print_salary(grossSalary, epf,tax)	

    elif(grossSalary > 308333):
        tax = calc_tax(grossSalary, 0.36, 73500)
        print_salary(grossSalary, epf,tax)	