class Item:
    #Constructor
    def __init__(self,name:str,price: float, quantity=0):
        #Run validations to the recived argumants
        assert price >=0, f"Price {price} is not greater than or equal to zero" 
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity= quantity
    
    def calc_total_price(self):
        return self.price * self.quantity
##########################END of Class#########################     

item1=Item("Phone",40,8)
item2=Item("Bag",9,50)

print(item1.calc_total_price())
print(item2.calc_total_price())

