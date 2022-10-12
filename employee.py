"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from abc import abstractmethod,ABC

class Employee:
    def __init__(self, name, contract,commission):
        self.name = name
        self.contract = contract
        self.commission = commission
    def get_pay(self):
        return self.contract.get_pay() + self.commission.get_pay() 
    def __str__(self):
        return  self.name + self.contract.get_str()+ self.commission.get_str() + '. Their total pay is ' + str(self.get_pay()) + "."

#Contract classes
class Contract:
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def get_pay(self):
        pass
    @abstractmethod
    def get_str(self):
        pass
    
class MonthlySalaryContract(Contract):
    def __init__(self,monthly_salary):
        self.monthly_salary=monthly_salary
        
    def get_pay(self):
        return self.monthly_salary
    def get_str(self):
        return " works on a monthly salary of " + str(self.monthly_salary) 

    
class HourlySalaryContract(Contract):
    def __init__(self, hours_worked,hourly_salary):
        self.hours_worked=hours_worked
        self.hourly_salary=hourly_salary
    def get_pay(self):
        return self.hours_worked*self.hourly_salary
    def get_str(self):
        return " works on a contract of " + str(self.hours_worked) + " hours at " + str(self.hourly_salary) + "/hour"

#Commission classes
class Commission:

    def __init__(self):
        pass
    @abstractmethod
    def get_pay(self):
        pass
    @abstractmethod
    def get_str(self):
        pass
    
class BonusCommission(Commission):
    def __init__(self, fixed_bonus):
        self.fixed_bonus=fixed_bonus
    def get_pay(self):
        return self.fixed_bonus
    def get_str(self):
        return " and receives a bonus commission of " + str(self.fixed_bonus)

class ContractCommission(Commission):
    def __init__(self,contract_number,commission_per_contract):
        self.contract_number=contract_number
        self.commission_per_contract = commission_per_contract
    def get_pay(self):
        return self.commission_per_contract*self.contract_number
    def get_str(self):
        return " and receives a commission for " + str(self.contract_number) + " contract(s) at " + str(self.commission_per_contract) + "/contract"
class NoCommission(Commission):
    def get_pay(self):
        return 0
    def get_str(self):
        return ""
        

### Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlySalaryContract(4000),NoCommission())
#print(billie.get_str())
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlySalaryContract(100,25),NoCommission())
#print(charlie.get_str())
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlySalaryContract(3000), ContractCommission(4,200))
#print(renee.get_str())
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',HourlySalaryContract(150,25) , ContractCommission(3,220))
#print(jan.get_str())               

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlySalaryContract(2000), BonusCommission(1500))
#print(robbie.get_str())
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlySalaryContract(120,30), BonusCommission(600))
string = str(ariel)
print(string)
