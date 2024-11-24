import csv 

class Item:
    pay_rate = 0.8
    all =[]
    def __init__(self,name:str,price:float,quantity=0):
        assert price>=0
        assert quantity>=0
        self.name=name
        self.price=price
        self.quantity=quantity
        Item.all.append(self)
    
    def calc_total_price(self):
        return self.price*self.quantity
   
    def apply_discoutn(self):
        self.price = self.price*self.pay_rate
    
    def __repr__(self):
        return f"{self.name},{self.price},{self.quantity}"

    @property 
    #Property Decorator == Read-Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name (self,value):
        if len(value>10):
            raise Exception("This name is too long")
        else:
            self.__name = value


    @classmethod
    def instanciate_form_csv(cls):
        with open('items.csv','r')as f:
            reader = csv.DictReader(f)
            items=list(reader)
        for item in items:
           Item(
               name=item.get('name'),
               price=float(item.get('price')),
               quantity=int(item.get('quantity'))
           )
    # Could be anywhere in the Class
    @staticmethod
    def is_integer(num):
        #We will couit ouit the floats that are point zero
        #For i.e: 5.0 10.0
        if isinstance(num, float):
            #coutn ouit the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
