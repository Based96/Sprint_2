class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email=None):
        hours = (7 - rest_days) * 8
        return cls(name, hours=hours, rest_days=rest_days, email=email)

    @classmethod
    def get_email(cls, name, hours=None, rest_days=None):
        email = f'{name}@email.com'
        return cls(name, hours=hours, rest_days=rest_days, email=email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment


    def salary(self):
        if self.hours is None:
            return 0
        return self.hours * self.hourly_payment