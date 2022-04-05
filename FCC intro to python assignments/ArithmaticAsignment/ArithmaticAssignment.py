# Input = ([["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True])
#


# region Defined Project
#Two inputs, problems and calculation
def arithmetic_arranger(problems, Calculation = False):
    NumProb = len(problems)
    if NumProb > 5:
        arranged_problems = 'Error: Too many problems.'
        return arranged_problems
        quit()

    FirstNumb = []
    Operand = []
    SecondNumb = []
    LongestNumb = []
    RefForUnderscore = []

    for equation in problems:
        TempNumb = equation.split()
        FirstNumb.append(TempNumb[0])
        Operand.append(TempNumb[1])
        SecondNumb.append(TempNumb[2])

    # check for issues
    for i in range(0, NumProb):
        if Operand[i] != '-' and Operand[i] != '+':
            arranged_problems = 'Error: Operator must be \'+\' or \'-\'.'
            return arranged_problems
            quit()

        try:
            int(FirstNumb[i]) + int(SecondNumb[i])
        except:
            arranged_problems = 'Error: Numbers must only contain digits.'
            return arranged_problems
            quit()

        if len(FirstNumb[i]) > 4 or len(SecondNumb[i]) > 4:
            arranged_problems = 'Error: Numbers cannot be more than four digits.'
            return arranged_problems
            quit()

    # For loop for inserting spaces and creating the code
    AppendedText = ""
    for i in range(0, NumProb):
        LongestNumb.append(max(len(FirstNumb[i]), len(SecondNumb[i])))

        # see how far the first number in the equation needs to be indented in reference to the second then add the opperand (needs an extra 2)
        FL_Dif = len(SecondNumb[i])-len(FirstNumb[i])
        if FL_Dif < 0:
            FL_Dif = 0
        for ii in range(0, FL_Dif + 2):
            AppendedText += " "
        AppendedText += FirstNumb[i]
        if i != NumProb-1:
            AppendedText += "    "
        else:
          # RefForUnderscore = len(AppendedText)  #for later adding the underscores for the 3rd line.
          AppendedText += '\n'

    #For second line
    for i in range(0, NumProb):
        AppendedText += Operand[i]
        FL_Dif = len(FirstNumb[i])-len(SecondNumb[i])   #see how many spaces we need in reference to the second number
        if FL_Dif < 0:
            FL_Dif = 0
        for ii in range(0, FL_Dif + 1):
            AppendedText += " "
        AppendedText += SecondNumb[i]
        RefForUnderscore.append(2+LongestNumb[i])
        if i != NumProb-1:
            AppendedText += "    "
            RefForUnderscore.append(-4)
        else:
          AppendedText += '\n'

    #For Third line
    for Dashes in RefForUnderscore:
        if Dashes > 0:
            for i in range(0,Dashes):
                AppendedText += '-'
        elif Dashes < 0:
            for i in range(0,abs(Dashes)):
                AppendedText += ' '
        else:
            arranged_problems = 'Error: Missing variable'



if problems[1] == True:
    SumNumb = []
    AppendedText += '\n'
    for i in range(0, NumProb):
        if Operand[i] == '+':
            SumNumb.append(int(FirstNumb[i]) + int(SecondNumb[i]))
        else:
            SumNumb.append(int(FirstNumb[i]) - int(SecondNumb[i]))

        for ii in range(0, (2+LongestNumb[i])-len(str(SumNumb[i]))):
            AppendedText += ' '

        AppendedText += str(SumNumb[i])

        if i != NumProb - 1:
            AppendedText += "    "
            RefForUnderscore.append(-4)

    arranged_problems = AppendedText
    return arranged_problems
#endregion

