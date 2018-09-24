class Dog:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    

class pets(Dog):
    def about_me(self):
        '''
           print the pet name and its age.
        '''
        return("{} is {}" .format(self.name , self.age))
    
    #creating instances of the dog class
print('\ni have 3 dogs')
oneinstance= pets("Tom",6)
twoinstance=pets("Fletcher",7)
threeinstance=pets("larry",9)
print(oneinstance.about_me())
print(twoinstance.about_me())
print(threeinstance.about_me())
print("And they are all mammals , of course ")

