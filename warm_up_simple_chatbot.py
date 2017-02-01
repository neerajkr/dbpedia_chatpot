from collections import OrderedDict

def Welcome_Msg():
    print("I am a simple chatbot, designed to translate Arabic to Roman number. Thanks, for checking it out!!")

def ConvertToRoman(num):

    Roman = OrderedDict()
    Roman[1000] = "M"
    Roman[900] = "CM"
    Roman[500] = "D"
    Roman[400] = "CD"
    Roman[100] = "C"
    Roman[90] = "XC"
    Roman[50] = "L"
    Roman[40] = "XL"
    Roman[10] = "X"
    Roman[9] = "IX"
    Roman[5] = "V"
    Roman[4] = "IV"
    Roman[1] = "I"

    def RomanNum(num):
        for r in Roman.keys():
            x, y = divmod(num, r)
            yield Roman[r] * x
            num -= (r * x)
            if num > 0:
                RomanNum(num)
            else:
                break

    return "".join([a for a in RomanNum(num)])

def Input():
    for x in xrange(1,10):
        if x==9:
            print("You have tried enough number of times !!")
            quit()
        try:
            num=input("Enter a number to convert to Roman Number: ")
            return num
            break
        except:
            print("Dude! I accept only Arabic Number, Try Again !! ")

Welcome_Msg()    

num= Input()


while True:
    print "Roman Number: ",ConvertToRoman(num)
    response = raw_input("If you would like to convert more number, please press y else n: ")
    if response=="y" or response=="Y":
        num=Input()
    else:
        quit()

