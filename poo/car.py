from Python.poo.account import Account

class Car:
    id = int
    license = str
    driver = Account("","")
    passenger = int
    def __init__(self,license, driver) -> None:
        self.license = license
        self.driver = driver
        