#HW1 #3
#Due Date: 07/13/2018, 11:59PM EST
# - First, read the file "HW3.pdf" posted on CANVAS 
### Use the Python debugger and the unittest module to assit you to achieve the goal of the assigment 
##*************************************

#Name: Viet Pham

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

class Stack:
# ----    Copy your Stack code from LAB8 here ---------


    def __init__(self):
        self.top = None
        self.count=0
    
    def __str__(self):
        temp=self.top
        out=''
        while temp:
            out+=str(temp.value)+ '\n'
            temp=temp.next
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        #write your code here
        return self.top==None

    def size(self):
        #write your code here
        return self.count
    
    def peek(self):
        #write your code here
        if self.top==None:
            return "Stack is empty"
        return self.top.value

    def push(self,value):
        #write your code here
        #special case, when stack is empty
        new_node=Node(value)
        if self.top==None:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.count+=1

    def pop(self):
        #write your code here
        #special case, when stack is empty
        if self.top==None:
            return "Stack is empty"
        #saves current top value in a variable called poppednum
        poppednum = self.top.value
        self.top = self.top.next
        self.count-=1
        return poppednum



# ----    Stack code ends here here ---------




def findNextOpr(txt):
    #--- Copy your function code from HW2 here ----#
    if len(txt)<=0 or not isinstance(txt,str):
        print("type error: findNextOpr")
        return "type error: findNextOpr"
    #In this exercise +, -, *, / are all the 4 operators
    #The function returns -1 if there is no operator in txt,
    #otherwise returns the position of the leftmost operator
    #--- continue the rest of the code here ----#

    #txt is a str input, check each character in string until an operator (*/+-) is found
    #store the operator's position, else return -1
    for charpos in range(len(txt)):
        if any(c in "^*/+-" for c in txt[charpos]):
            return charpos
    else:
        return -1
    #--- function code ends -----#


def isNumber(txt):
    #--- Copy your function code from HW2 here ----#
    if len(txt)==0 or not isinstance(txt, str):
        print("type error: isNumber")
        return "type error: isNumber"
    #--- continue the rest of the code here ---#

    #txt is a string input, tries to convert each string into a float, unless it is a decimal or 0
    #returns True for decimal and 0 since numbers can contain 0 and decimals
    #returns true for " " to help with program conditions
    #returns false if its not any of those, which indicates that txt is not a number
    else:
        try:
            if float(txt) or txt == "0":
                return True
        except:
            if txt == "." or txt == " " or txt == "(" or txt == ")":
                return True
            else:
                return False
    #--- function code ends -----#

def getNextNumber(expr, pos):
    #--- Copy your function code from HW2 here ----#
    #expr is a given arithmetic formula of type string
    #pos = start position in expr
    #1st returned value = the next number (None if N/A)
    #2nd returned value = the next operator (None if N/A)
    #3rd retruned value = the next operator position (None if N/A)
    if len(expr)==0 or not isinstance(expr, str) or pos<0 or pos>=len(expr) or not isinstance(pos, int):
        print("type error: getNextNumber")
        return None, None, "type error: getNextNumber"

   #--- continue the rest of the code here ---#

   #takes in the string expr, and beginning pos (0 for + numbers, 1 for - numbers)


    #check for special case where the expression is incomplete (i.e. "555 -", "2123 /")
    for characterpos in range(len(expr)):
        if any(d in "^*/+-" for d in expr[characterpos]):
            if not any(n in "0123456789." for n in expr[characterpos:]):
                return None, None, None


   #creates a while loop to check each char in the mathematical expression
   #checks to see if each character is a digit or a decimal, if so add it to the variable Number
   #the variable Number will become the actual whole number 
   #increment pos(position in expression) each time to go through whole expression
    negativesign = 0
    Number = ""
    for i in range(3):
        if expr[pos] == "-":
            Number += expr[pos]
            negativesign += 1
            pos += 1
    while isNumber(expr[pos]):
        Number += expr[pos]
        if expr[pos] == "(" and expr[pos+1] == "-":
            Number += expr[pos+1]
            pos += 1
        #this condition checks the special case where an invalid expression has a space seperating two digits
        #Example - "4 3", "2    9", returns None for all paramaters to get error output
        if expr[pos] == " " and expr[pos+1].isnumeric() and expr[pos-1].isnumeric():
            return None, None, None
        pos += 1

    #checks to see if the current character in the expression is an operator
    #if true, assign that operator and its position to the variable, Opr, and oprPos, respectively
    if any(c in "^*/+-" for c in expr[pos]):
        Opr = expr[pos]
        oprPos = pos
    #if the current character in the expression is not an operator
    #then use the findNextOpr function to find the next very next operator's position
    elif not any(c in "^*/+-" for c in expr[pos]):
        oprPos = findNextOpr(expr[pos:])
        Opr = expr[oprPos]

    #checks the special case where there are two identical operators next to each other, returns error
    if (expr[oprPos-1] != "-") and (Opr != "-"):
        if (expr[oprPos-1] == Opr):
            return "doubleoperror", "doubleoperror", 'doubleoperror'
    #tries to convert Number found to a float, if not then it is not a number therefore, return an error output
    #also checks for other special cases such as two different operators next to each other, returns error
    try:
        Number = Number.replace("(", "")
        Number = Number.replace(")", "")
        if any(c in "-" for c in Number):
            Number = Number.replace(" ", "")
        if negativesign == 2:
            Number = Number.replace("--","")
        return float(Number), Opr, oprPos
    except:
        return None, None, None
    #--- function code ends -----#
    

def exeOpr(num1, opr, num2):
    #This funtion is just an utility function. It is skipping type check
    if opr=="+":
        return num1+num2
    elif opr=="-":
        return num1-num2
    elif opr=="*":
        return num1*num2
    elif opr=="/":
        if num2==0:
            print("Zero division error")
            return "Zero division error"
        else:
            return num1/num2
    elif opr=="^":
        return num1 ** num2
    else:
        print("error in exeOpr")
        return "error in exeOpr"

    
def _calculator(expr):
    #--- Copy the body of your calculator(expr) function from HW2 here ----#

    #expr: nonempty string that is an arithmetic expression
    #the fuction returns the calculated result
    expr = expr.strip()
    tempExpr = ""
    for q in range(len(expr)):
        if expr[q] == " " and (not expr[q+1].isnumeric() and not expr[q-1].isnumeric()):
            tempExpr = tempExpr + ""
        elif expr[q] == " " and (expr[q+1].isnumeric() and not expr[q-1].isnumeric()):
            tempExpr = tempExpr + ""
        elif expr[q] == " " and (not expr[q+1].isnumeric() and expr[q-1].isnumeric()):
            tempExpr = tempExpr + ""
        else:
            tempExpr = tempExpr + expr[q]
    expr = tempExpr

    if len(expr)<=0 or not isinstance(expr,str):
        print("error")        #Line A
        return "error"
    #print(expr)
    #Hold two modes for operator precedence: "addition" and "multiplication"
    #Initialization: get the first number
    #checks for special cases in expressions such as letters, symbols, and single numbers
    for z in expr:
        if z.isalpha() or (isNumber(z) is False and any(d not in "^*/+-()" for d in z)):
            return "error"

    if any(l in "^*/+()" for l in expr[0]):
        if expr[1].isnumeric() is False:
            return "error"
    if expr[0] == "-" and any(l not in " -(0123456789" for l in expr[1]):
            return "error"


    #if expression is a single number, return that number
    try:
        if float(expr):
            return float(expr)
    except:
        pass

    ## Think why the next 6 lines are necessary... 
    ## Is there another way to achieve the same result? 
    expr = expr.strip()
    if expr[0]!="-":
        newNumber, newOpr, oprPos = getNextNumber(expr, 0)
    else:
        newNumber, newOpr, oprPos = getNextNumber(expr, 1)
        newNumber *= -1
    #####

    if newNumber is None:   
        return "error"
    elif newOpr is None:
        return newNumber
    elif newOpr=="+" or newOpr=="-":
        mode="add"
        addResult=newNumber     #value so far in the addition mode
        mulResult=None          #value so far in the mulplication mode
        expResult=0
    elif newOpr=="*" or newOpr=="/":
        mode="mul"
        addResult=0
        mulResult=newNumber
        expResult=0
    elif newOpr == "^":
        mode = "exp"
        addResult = 0
        mulResult = 0
        expResult = newNumber
    pos=oprPos+1                #the new current position
    opr=newOpr                  #the new current operator

    #Calculation starts here. 
    #Use the above completed functions effectively!

    #Creates lists to store addition and subtraction operators to use in function
    #This is so the function can follow order of operations
    #creates i and c counter so calcutor can calcute the operators in order
    addsubOprlist = ["+"]
    addsubOprlist2 = ["+"]
    specialmode = ""
    i = 0
    c = 0
    addsubchecker = 0
    negativesign = 0
    while True:
        #--- continue the rest of the while loop code here ---#

        #loops run until the end of the expression
        while pos < (len(expr)):
            #creates arbitrary initial operator so logic can work
            addsubOpr = "+"

            #if the first operator (or next operator) is + or -, add mode is activator
            #used for performing addition and subtraction operations
            if mode == "add":
                #store add/sub operators into the list created to be used for later
                if opr == "+" or opr == "-":
                    addsubOprlist2.append(opr)
                    addsubOprlist.append(opr)
                    i += 1
                    c += 1

                #gets next number and next operator
                try:
                    newNumber, nextOpr, nextOprPos = getNextNumber(expr, pos)
                #this try/except is to used so the it avoids the error while getting the last number
                #last calculation is done here
                except: 
                    lastnumber = ""
                    #pos should be right before the last number in expression, so last number is obtained
                    for digit in range(pos, len(expr)):
                        lastnumber += expr[digit]
                    lastnumber = lastnumber.replace("(", "")
                    lastnumber = lastnumber.replace(")", "")
                    for p in lastnumber:
                        if p == "-":
                            negativesign += 1
                    if negativesign == 2:
                        lastnumber = lastnumber.replace("--","")
                    if negativesign > 2:
                        return "error"

                    if pos == (len(expr)-1):
                        finalvalue = exeOpr(float(addResult), opr, float(lastnumber))
                        return finalvalue
                    finalvalue = exeOpr(float(addResult), opr, float(lastnumber))
                    return finalvalue

                #these conditions are to account for the special cases found in the above functions
                if newNumber is None:  
                    return "error"
                if newNumber is "doubleoperror" and nextOpr is "doubleoperror" and nextOprPos is "doubleoperror":
                    return "error"

                #always increment the position to move along in the expression
                pos = nextOprPos+1

                if nextOpr == "^":
                    mode = "exp"
                    expResult = newNumber
                    break
                #these conditions enable calculator function to switch to and from different modes
                if nextOpr == "*" or nextOpr == "/":
                    #switching to mulmode
                    #when switching, the newnumber, or current calculated number is stored until needed 
                    mulResult = newNumber
                    opr = nextOpr
                    mode = "mul"
                    break
                if nextOpr == "+" or nextOpr == "-":
                    #switching to add mode
                    #performs calculation
                    addResult = exeOpr(float(addResult), opr, float(newNumber))
                    opr = nextOpr
                    #stores the add sub operator in the list to be used lator at the correct order
                    addsubOprlist2.append(nextOpr)
                    c += 1
                    addsubchecker += 1



            #if the first operator (or next future operators) is * or /, multiplication mode is activated
            #used to perform multiplication and division operations
            if mode == "mul":
                #gets the next number, next operator its position
                try:
                    newNumber, nextOpr, nextOprPos = getNextNumber(expr, pos)
                except:
                    #if the try gets an error, it means that pos cannot be incremented anymore, therefore, its
                    #at the last number, so last number is found and use to calculate the final value
                    lastnumber = ""
                    for digit in range(pos, len(expr)):
                        lastnumber += expr[digit]   
                    lastnumber = lastnumber.replace("(", "")
                    lastnumber = lastnumber.replace(")", "")
                    for p in lastnumber:
                        if p == "-":
                            negativesign += 1
                    if negativesign == 2:
                        lastnumber = lastnumber.replace("--","")
                    if negativesign > 2:
                        return "error"
                    if pos == (len(expr)-1) and len(addsubOprlist2) == 1:
                        finalvalue = exeOpr(float(mulResult), opr, float(lastnumber))
                        return finalvalue
                    lastopr = exeOpr(float(mulResult), opr, float(lastnumber))
                    finalvalue = exeOpr(float(addResult), addsubOprlist2[c], float(lastopr))
                    #addsubchecker checks to see if there are any add/sub operations that have not been performed yet
                    #if there are, then it has to perform it in this if statement
                    if addsubchecker != c and ("^" in expr) and ((addsubOprlist2[c] == "+") or (addsubOprlist2[c] == "-")) and ((opr == "+") or (opr == "-")):
                        lastopr = exeOpr(float(addResult), addsubOprlist2[c], float(mulResult))
                        finalvalue = exeOpr(float(lastopr), opr, float(lastnumber))
                        return finalvalue
                    return finalvalue
                #use to account for special cases and the errors found in the above functions
                if newNumber is None:
                    return "error"
                if newNumber is "doubleoperror" and nextOpr is "doubleoperror" and nextOprPos is "doubleoperror":
                    return "error"
                #increments position by one to go through whole expression
                pos = nextOprPos+1

                #so if an expression is currently in mul mode, it will perform all the necessary and correct
                #calculations before switching to add mode, and checking the next operations needed to be done
                if nextOpr == "+" or nextOpr == "-":
                    #switching to addmode
                    addsubOpr = nextOpr
                    #performs the calculation before moving on
                    #Example - in "4 * 5 - 10 * 2 / 4", it will calculate "4 * 5", first then move onto next
                    #needed operations such as "10 * 2 / 4"
                    #it will store that result and the add/sub operator for future uses
                    mulResult = exeOpr(float(mulResult), opr, float(newNumber))
                    addResult = exeOpr(float(addResult), addsubOprlist[i], float(mulResult))
                    if len(addsubOprlist)>1:
                        addsubchecker += 1
                    addsubOprlist.append(nextOpr)
                    i += 1
                    mode = "add"
                    opr = nextOpr
                    break
                #if the next operators are just * or /, then it will calculate incremently, moving forward in
                #the expression each time until nextOpr = + or - (until add/sub operator is found)
                #then it will begin to switch to add move and performs all the operations described above ^^
                if nextOpr == "^":
                    mode = "exp"
                    expResult = newNumber
                    break

                elif (nextOpr == "*" or "/"):
                    mulResult = exeOpr(float(mulResult), opr, float(newNumber))
                    opr = nextOpr



            if mode == "exp":
                #tries to next number to perform exponential function
                try:
                    newNumber, nextOpr, nextOprPos = getNextNumber(expr, pos)
                #if function get next number, then it is the last number so it performs the last
                #operations
                except:
                    lastnumber = ""
                    for digit in range(pos, len(expr)):
                        lastnumber += expr[digit]
                    lastnumber = lastnumber.replace("(", "")
                    lastnumber = lastnumber.replace(")", "")
                    for p in lastnumber:
                        if p == "-":
                            negativesign += 1
                    if negativesign == 2:
                        lastnumber = lastnumber.replace("--","")
                    if negativesign > 2:
                        return "error"
                    if opr == "^":
                        return exeOpr(float(expResult), "^", float(lastnumber))
                    elif (opr == "+") or (opr == "-"):
                        expResult = exeOpr(float(newNumber), "^", float(lastnumber))
                        return exeOpr(float(addResult), opr, float(expResult))
                    elif (opr == "*") or (opr == "/"):
                        expResult = exeOpr(float(newNumber), "^", float(lastnumber))
                        if addsubchecker != c:
                            mulResult = exeOpr(float(mulResult), opr, float(expResult))
                            return exeOpr(float(addResult), addsubOprlist2[c], float(mulResult))
                        return exeOpr(float(mulResult), opr, float(expResult))
                #accounts for errors found in the input
                if newNumber is None:  
                    return "error"

                #if there are still operations needed to be performed than it will meet
                #these conditions below
                pos = nextOprPos+1
                expResult = exeOpr(float(expResult), "^", float(newNumber))
                if mulResult != 0 and (opr == "*" or opr == "/"):
                    mode = "mul"
                    newNumber = expResult
                    mulResult = exeOpr(float(mulResult), opr, float(newNumber))
                    opr = nextOpr
                    break

                if mulResult != 0 and (opr == "+" or opr == "-") and ((nextOpr != "*") and (nextOpr != "/")):
                    mode = "add"
                    newNumber = expResult
                    addResult = exeOpr(float(addResult), opr, float(newNumber))
                    opr = nextOpr
                    break

                opr = nextOpr
                if (nextOpr == "*") or (nextOpr == "/"):
                    mulResult = expResult
                    mode = "mul"
                    break
                if (nextOpr == "+") or (nextOpr == "-"):
                    addResult = expResult
                    mode = "add"
                    break

    return False
    #--- function code ends -----#

def calculator(expr):
    # Required: calculator must create and use a Stack for parenthesis matching
    # Call _calculator to compute the inside 

    tempExpr = ""

    if expr[0] == "-" and (expr[1] == '-'):
        expr = expr[2:]   
    if len(expr)<=0 or not isinstance(expr,str): 
        print("argument error: calculator")
        return "argument error: calculator"
    expr = expr.strip()
    s = Stack()        # You must use the Stack s
    pos = expr.find("(")
    #openParCount counts how many paranthetical operations will be needed to execute
    openParCount = 0
    #calcTop is the calculated answer of the current parenthetical expression, which is the top node value
    calcTop = 0
    #counts how many parenthetical groups in the whole expression
    numofParGroups = 0
    #counts how many parenthetical groups have been evaluated so far to see if loop will stop
    numofParOperations = 0

    #Checks to see if parentheses are balanced, initial check
    for charpos in range(len(expr)):
        if expr[charpos] == "(":
            s.push(expr[charpos])
            #openParCount += 1
            
        if expr[charpos] == ")":
            if s.isEmpty():
                return "error"
            else:
                s.pop()
                if s.isEmpty():
                    numofParGroups += 1
        if charpos == len(expr)-1 and s.isEmpty() == False:
            return "error"

    while True:
    #--- function code starts here -----#

        #loop will run while there are still parenthetical groups to be evaluated
        while "(" in expr:

            #loops through the whole expression
            for cpos in range(len(expr)):

                #this part checks to see when the first parenthetical group evaluation will start
                if expr[cpos] == "(":
                    s.push(expr[cpos])
                elif expr[cpos] == ")":
                    s.pop()
                #it will start when Stack S is empty, meaning it has identified the first parenthetical group
                if s.isEmpty() and expr[cpos]==")":
                    #creates a temporary expression until the correct evaluated values will be subsituted in
                    tempExpr = expr[:cpos+1]
                    #it will create a temporary expression of that closed parenthesis group
                    parExpr = tempExpr[tempExpr.find('('):tempExpr.rfind(')')+1]
                    #creates a temporary expression until the correct evaluated values will be subsituted in
                    #counts how many times it will need to evaluate a parenthetical expression inside a parenthetical group
                    for parcount in range(len(parExpr)):
                        if parExpr[parcount] == "(":
                            openParCount += 1

                    #pushes the position of the open parenthesis in and will evaluate the expression in the parenthesis when the paired closed parenthesis has been found
                    #repeat until there are no more parenthesis in the parenthentical group
                    while "(" in parExpr:
                        for j in range(len(parExpr)):
                            if parExpr[j] == "(":
                                s.push(j)
                            elif parExpr[j] == ")":
                                calcTop = _calculator(parExpr[s.top.value+1:j])
                                parExpr = parExpr.replace(parExpr[s.top.value:j+1],str(calcTop))
                                s.pop()
                                break

                    #Verifies to reset the stack
                    while not s.isEmpty():
                        s.pop()
                    #replaces the expression up until the end of the current parenthetical group with the evaluated values
                    tempExpr = tempExpr.replace("("+tempExpr[tempExpr.find('(')+1:tempExpr.rfind(')')]+")", str(parExpr))
                    #tempExpr = tempExpr.replace("--", "")
                    #tempCalc = _calculator(tempExpr)
                    expr = expr.replace(expr[:cpos+1], str(tempExpr))
                    #resets the openParCount until the next parenthetical group is to be evaluated
                    numofParOperations += 1
                    openParCount = 0
                    #resets the cpos counter
                    break
        
        return _calculator(expr)

    #--- function code ends here-----#