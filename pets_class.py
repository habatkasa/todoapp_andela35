class Dog:
    def __init__ (self,name,age,is_hungry):
        self.name=name
        self.age=age
        self.is_hungry=True
    def eat(self):
        self.is_hungry=False
        return ("My dogs are not hungry")
        

    

class pets(Dog):
    def about_me(self):
        '''
           print the pet name and its age.
        '''
        return("{} is {}" .format(self.name , self.age))
    def hungry_or_not(self):
        '''
           print my dogs are not hungry
        '''
        return ("my dogs are not hungry")    
    #creating instances of the dog class

oneinstance= pets("Tom",6,False)
twoinstance=pets("Fletcher",7,False)
threeinstance=pets("larry",9,False)
fourinstance=pets.hungry_or_not(False)
print(oneinstance.about_me())
print(twoinstance.about_me())
print(threeinstance.about_me())
print("And they are all mammals , of course ")
print(fourinstance)
print(oneinstance.eat())
