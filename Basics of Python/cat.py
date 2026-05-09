class Cat:
    def __init__(self,color,name,status):
        self.name = name
        self.color = color 
        self.status=status
    def tell_about_cat(self):
        print(f"{self.name} is {self.status}")
    def change_status(self,new):
        self.status = new



