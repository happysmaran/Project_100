import time

class atm(object):
    def _init_(self):
        self.cardNo=0
        self.pinNo=''
        self.verifyPin=''
        self.howMuchMoneyWant=0

    def CashWithDrawl(self, cardNo, pinNo, verifyPin, howMuchMoneyWant, howMuchMoneyHave):
        if(verifyPin==pinNo):
            print()
            question=input("Would you like to cash withdrawl? (Y/N): ")
            if question=="Y" or question=="y":
                verifyPin=input("Please verify pin to continue: ")
                if(verifyPin==pinNo):
                    howMuchMoneyWant=int(input("Enter amount in ₹ : "))
                    if(howMuchMoneyHave>howMuchMoneyWant):
                        print("Wait...")
                        time.sleep(5)
                        print("Withdrawl of ₹"+str(howMuchMoneyWant)+" is done.")
                        nowCurrent=howMuchMoneyHave-howMuchMoneyWant
                        print("You now currently have ₹"+str(nowCurrent))
                    else:
                        print("The amount of money you want will exceed the amount you have, select a smaller amount.")
                else:
                    print("Verification failed; denied.")
            else:
                print("done.")
        else:
            print()
            print('Verification failed; denied.')


me=atm()

howMuchMoneyHave=int(input("first, set a starting value of amount in account: "))
print()
print()
print()
cardNo=int(input("Please enter card number(No spaces please!): "))
pinNo=input("Please enter pin: ")
verifyPin=input("Verify pin: ")
print()
print("Welcome, card id "+str(cardNo))
howMuchMoneyWant=0

me._init_()
me.CashWithDrawl(cardNo, pinNo, verifyPin, howMuchMoneyWant, howMuchMoneyHave)
