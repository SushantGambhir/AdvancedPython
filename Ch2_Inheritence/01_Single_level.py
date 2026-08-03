class company:

    def __init__(self, company_name):
        self.company_name = company_name

    def info(self):
        print('Company Name: '+ self.company_name)
        return self.company_name

comp_obj = company('Tech Solution')
comp_obj.info()

class employee(company):

    def __init__(self, company_name, employee_name):
        self.employee_name = employee_name
        self.company_name = company_name

    def employee_info(self):
        response = company.info(self)
        print('The employee: ' + self.employee_name + ' works at the Company ' + response)

emp_obj = employee('Amadeus','Sushant')
emp_obj.employee_info()