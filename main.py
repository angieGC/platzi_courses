import imp
from lib2to3.pgen2 import driver
from car import Car
from UberX import UberX
from account import Account
if __name__ == "__main__":
    print("hoola")
    car = Car("oon345",Account("adfmasf ASDf","12315145"))
    # print(vars(car))
    # print(vars(car.driver))
    ubercar = UberX("oon345",Account("adfmasf ASDf","12315145"),'sdsdf','asdff')
    print(vars(ubercar))
    print(vars(ubercar.driver))