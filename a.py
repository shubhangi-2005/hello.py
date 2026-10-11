class Employee:
    company_name="technova"
    
    def __init__(self,employee_name,employee_id,salary):
        self.employee_name=employee_name
        self.employee_id=employee_id
        self.salary= salary
    def display_details(self):
        print("employee Name:",self.employee_Name)
        print("employee ID:",self.employee_id)
        print("salary:",self.salary)
        print("company name:",self.company_name)

    @classmethod
    def change_company_name(cls,new_name):
        cls.company_name    

