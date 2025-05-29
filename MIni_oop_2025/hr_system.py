class HRSystem:
    def __init__(self):
        self.employees = []
        self.departments = []
        self.projects = []


    def add_employee(self,employee):
        if employee not in self.employees:
            self.employees.append(employee)


    def add_department(self,department):
        if department not in self.departments:
            self.departments.append(department)



    def add_project(self,project):
        if project not in self.projects:
            self.projects.append(project)


