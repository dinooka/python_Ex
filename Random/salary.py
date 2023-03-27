import math

class Salary:
    def gross(self,gross_salary):
        return int(gross_salary)
    
    def epf(self,gross_salary):
        return math.ceil(int(gross_salary)*0.08)

    def calc_tax(self,gross_salary, rate, k):
        tax = math.ceil(gross_salary * rate) - k
        return tax
		
    def print_salary(self,gross_salary, epf, tax):
        
        netSalary = gross_salary - (epf + tax)
        print(f"EPF deduction \t        = {epf}")
        print(f"Tax deduction \t        = {tax}")
        print(f"\nNet Salary \t        = {netSalary}\n")

    def calc_sal(self,gsalary): 
        gross_salary = self.gross(gsalary)
        epf = self.epf(gross_salary)

        if(gross_salary < 0 ):
            print("Enter a valid number!...")

        elif(gross_salary < 100000):
            tax = 0	
            self.print_salary(gross_salary, epf,tax)	

        elif((gross_salary >= 100000) & (gross_salary < 141667)):
            tax = self.calc_tax(gross_salary, 0.06, 6000)
            self.print_salary(gross_salary, epf,tax)	

        elif((gross_salary >= 141667) & (gross_salary < 183333)):
            tax = self.calc_tax(gross_salary, 0.12, 14500)
            self.print_salary(gross_salary, epf,tax)	

        elif((gross_salary >= 183333) & (gross_salary < 225000)):
            tax = self.calc_tax(gross_salary, 0.18, 25500)
            self.print_salary(gross_salary, epf,tax)	

        elif((gross_salary >= 225000) & (gross_salary < 266667)):
            tax = self.calc_tax(gross_salary, 0.24, 39000)
            self.print_salary(gross_salary, epf,tax)	

        elif((gross_salary >= 266667) & (gross_salary < 308333)):
            tax = self.calc_tax(gross_salary, 0.3, 55000)
            self.print_salary(gross_salary, epf,tax)	

        elif(gross_salary > 308333):
            tax = self.calc_tax(gross_salary, 0.36, 73500)
            self.print_salary(gross_salary, epf,tax)	


