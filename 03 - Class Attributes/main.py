class Item:
    pay_rate = 0.8
    all =[]
    def __init__(self,name:str,price:float,quantity=0):
        assert price>=0 , f"The price value {price} isn't valid"
        assert quantity >=0, f"The quantity value{quantity} isn't valid" 
        self.name=name
        self.price=price
        self.quantity=quantity

        #Actions to excute
        Item.all.append(self)
    
    def calc_total_price(self):
        return self.price*self.quantity
    
    def apply_discoutn(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item(Name:'{self.name}', Price:{self.price}, Quantity:{self.quantity})\n"
        #return f"Item('{self.name}', {self.price}, {self.quantity})\n"
    

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


print(Item.all)