from salary import Salary

while True:
	gsalary= input("Enter your gross salary = ")  

	# i/p validation & quit
	if (gsalary == 'q'):
		break
	# try:
	if gsalary.isnumeric():
		# 	grossSalary = Salary.gross(gsalary)
		# 	epf = Salary.epf()
		sal = Salary()
		sal.calc_sal(gsalary)
	# except:
		# print("Enter a valid number!")

