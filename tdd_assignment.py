class registration:
    def __init__ (self,name,age,gender,username,password,email):
        self.name = name 
        self.age = age
        self.gender = gender
        self.username = username
        self.password = password
        self.email = email

   
    
    
capital_letters =['A','B','C','D','E','F','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small_letters=['a','b','c','d','e','f','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

special_chars = ['!','@','#','$','%','^','&','*','?','>']
class verify(registration):
    
    #special_chars = ['!','@','#','$','%','^','&','*','?','>']
    def check_age(self):
        # if self.age is not int:
        #     return (False,"age must be a number")
        if self.age < 0:
            return (False,"age must be a positive interger")

    def check_password(self,password):
        ''' this checks if a password satisfies the conditions, returns true if it satisfies
        '''
        if len(self.password) <= 4:
            return (False,'password must be atleast 5 characters\n')
        for letter in capital_letters:
            if letter in self.password:
                return True
            return (False , "password must have atleast a capital letter\n")  #changed some thing here
        
        for char in special_chars:
            if char  in self.password:
                return True
            return (False,"password must have atleast one special character\n")
        for later in small_letters:
            if later in self.password:
                return True
            return "password must have atleast one small letter\n"
        
            
    
    def check_username(self,username):
        '''this checks if the user name is not the name, returns true if true
        '''
        self.username = username
        if self.username is self.name:
            return False, "user name should not be same as your name\n"
        if len(self.username) <= 4 :
            return (False,"user name must be atleast 5 characters\n")
        else:
            return True
    
    def check_email(self):
        ''' 
           this checks if email has @,.,and com to validate it.
        '''
        list=['@','.','com']
        for i in list:
            if i not in self.email:
                #print( "invalid Email address\n")
                break
            return (False,"invalid email address\n")

                
                

class change_details(verify):# initially has been inherriting fom registration

    def change_password(self,validate_change):
        #validate_change = input('enter your current password\n')
        if validate_change is not self.password:
            return "Failed to validate that this is your account."
        if validate_change is self.password: 
            new_password1 = input('enter new password')
            #some code missing here
            new_password2 = input('Re enter newpassword')
        if new_password1 is not new_password2:
            return "your passwords dont match"
        if new_password1 is new_password2:    
            self.password = new_password1
            return "password has been changed"
      
            

    def change_email(self,new_email):
        '''checks if user knows the password of this account,
           and then changes email addres if correct password is given,
           rejects if password is not given correctly.
           '''
        validate_password = input('enter your current password')
        if validate_password is not self.password:
            return "Failed to validate this is your account"
            #new_email = input('Enter your new email address\n')
        while validate_password is True:
            valid_email = change_details.check_email(new_email)
            if valid_email is True:
                self.email = new_email
                return "email successfully changed"
            
# class User_information(registration):
#     user_name = User_information.Request_details(self.name) 
#     user_age = age
#     user_gender = gender
#     user_username = username
#     user_password = password
#     user_email = email


if __name__== "__main__":
#    egistration.request_details('')r
   #registration.request_more_details(password)
    def request_details():
        name=input("enter your name\n")  
        age = input('enter your age.\n') 
        gender = input('enter your gender\n')
        return name ,age, gender

    def request_username():
        username = input('enter your username\n')
        return username
    def request_password():
        password = input('Enter your password\n')
        return password
    def request_email():
        email = input('Enter email here\n')
        return(email)
    request_details()
    request_username()

    #make an instance of the verify class
    #checking_username = verify(request_details(),)



 