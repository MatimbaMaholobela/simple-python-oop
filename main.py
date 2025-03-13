from user import Person

class Main:
    """
        handle user inputs

    """
    def userInput(self):
        print("------------WELCOME TO X'S Banking System-----------------")
        
        self.name = input("Enter Name: ")
        self.lastName = input("Enter Last Name: ")
        self.accountType = input("Enter Account Type:\n(S)avings/ (C)urrent: ")

        return {"name":self.name,"lastName":self.lastName,"accountType":self.accountType}
        
if __name__== "__main__":

    # create instance of main and collect user inputs
    user  = Main()
    userData = user.userInput()

    #create person instance
    createAccount = Person(userData["name"],userData["lastName"])
    createAccount.setAccountType(userData["accountType"])

    print("User has been created Succcessfully.\n",createAccount)

