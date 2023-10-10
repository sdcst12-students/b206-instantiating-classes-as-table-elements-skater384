class customer:
    name = ""
    account = 0

    def __init__(self,name,account):
        self.name = name
        self.account = account


customerDatabase = []

customerDatabase.append( customer("Dash",1))
customerDatabase.append( customer("Kieran",2))
customerDatabase.append( customer("Andrew",3))
customerDatabase.append( customer("Cole",4))

print(len(customerDatabase))
for i in customerDatabase:
    print(i.name)



