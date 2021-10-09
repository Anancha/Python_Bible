class Promotion:
    def __init__(self, promotion_name, month):
        self.promotion_name = promotion_name
        self.month = month
        self.__display()
    def __display(self):
        print("##############################################")
        print("# Promotion of ",self.month,"is",self.promotion_name,"#")
        print("##############################################")

ofc = Promotion("Strawberry Lover", "December")
#ofc.__display()