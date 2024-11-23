class Item: 
    def calc_total_price(self,x,y):
        return x*y
    
#create an instance of an Item 

item1=Item()

item1.name="Phone"
item1.price=90
item1.quantity=5

#calling methods from instances of a class:
print(item1.calc_total_price(item1.price,item1.quantity))


