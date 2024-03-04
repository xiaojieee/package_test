from Bank.person import Person

class Customer(Person):
    def __init__(self, firstname, lastname, customer_id):
        super().__init__(firstname, lastname)
        self._balance = customer_id
