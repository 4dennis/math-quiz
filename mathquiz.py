import random

iDifficulty = 10

iUser = 0
iAnswer = 0
iCorrect = 0
iTotal = 0
i = 0

while i < 20:

    i += 1

    #operation for quiz ex + / * -
    iOperator = random.randint(0,5) 
    #iOperator = 0 

    #random numbers
    iValue1 = random.randint(1,iDifficulty)
    iValue2 = random.randint(1,iDifficulty)
    iValue3 = random.randint(1,iDifficulty)


    #to check operator if needed
    #print(iOperator)

    #find operator and give equation
    if iOperator == 0:
    #addition
        iAnswer = iValue1 + iValue2
        print(iValue1, " + ", iValue2, " = ")
        iUser = input()

    elif iOperator == 1:
        #substraction
        iAnswer = iValue1 - iValue2
        print(iValue1, " - ", iValue2, " = ")
        iUser = input()

    elif iOperator == 2:
        #divition
        iAnswer = (iValue1 * iValue2) / iValue2
        print((iValue1 * iValue2) , " / ", iValue2, " = ")
        iUser = input()

    elif iOperator == 3:
        #multiplication
        iAnswer = iValue1 * iValue2
        print(iValue1, " x ", iValue2, " = ")
        iUser = input()

    elif iOperator == 4:
        #square root
        iAnswer = iValue1
        print("√", (iValue1 * iValue1))
        iUser = input()

    elif iOperator == 5:
        #exponent
        iAnswer = iValue1 * iValue1
        print(iValue1,"²")
        iUser = input()
  

    if int(iUser) == iAnswer:
        iDifficulty += 1
        iCorrect += 1
        iTotal += 1
        print ("Correct! Your score is ", iCorrect, "/", iTotal)

    else:
        iTotal += 1
        print ("Incorrect. Your score is ", iCorrect, "/", iTotal, ". The correct value was ", iAnswer, ".")

print("\nThanks for trying. Your final score was ", iCorrect, "/", iTotal,"\n")