class company:

    def __init__(self, company_name):
        self.company_name = company_name

    def info(self):
        print('Company Name: '+ self.company_name)
        return self.company_name

class employee(company):

    def __init__(self, company_name, employee_name):
        self.employee_name = employee_name
        self.company_name = company_name

    def employee_info(self):
        response = company.info(self)
        print('The employee: ' + self.employee_name + ' works at the Company ' + response)


class contractor(company):

    def __init__(self, parent_company_name, company_name, employee_name):
        self.contractor_name = employee_name
        self.company_name = company_name
        self.parent_company_name = parent_company_name

    def contrator_info(self):
        print('The employee: ' + self.contractor_name + ' works at the Company ' + self.company_name + ' and the parent company is ' + self.parent_company_name)

cont_obj = contractor('UST','Amadeus','Sushant')
cont_obj.contrator_info()