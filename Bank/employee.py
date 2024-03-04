from Bank.person import Person


class Employee(Person):
    def __init__(self, firstname, lastname, employee_id, department):
        super().__init__(firstname, lastname)
        self._employee_id = employee_id
        self._department = department
