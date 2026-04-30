
class BankAccount:
    def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
        self.first_name   = first_name
        self.last_name    = last_name
        self.account_id   = account_id
        self.account_type = account_type
        self.pin          = pin
        self.balance      = balance

    def deposit(self, deposit):
        self.balance = self.balance + deposit
        print(f'Su nuevo balance es: ${self.balance}')
    
    def withdraw(self, retire):
     self.balance = self.balance - retire
     print(f'El importe retirado es: ${retire}')
    def display_balance(self):
     return self.balance 


my_account_bank = BankAccount('Breiner', 'Abello', '5151611', 'Premium', '6516516', 100)

my_account_bank.deposit(96)
my_account_bank.withdraw(25)

