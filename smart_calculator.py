# NOTE : simple calculator program ends at line 49
#            : advance calculator program ends at line 201
#            : interactive calculator ends at line 285



#main python program 
from colorama import Fore,Style
import pyfiglet
import random
import math
import time


user_input=("")
while True:
	time.sleep(1.5)
	print(Style.BRIGHT,"\033[31m",pyfiglet.figlet_format('CALCULATOR'),"\033[4m","\n## Enter 33117799 for advanced mode...")
	print("## Enter 22557788 for interactive mode...\n","\033[0m",Style.RESET_ALL)
	print("~~~What you want to do : ")
	print("☆Add                   (type 1)")
	print("☆Subtract              (type 2)")
	print("☆Multiply              (type 3)")
	print("☆Divide                (type 4)")
	print("☆Square of a number    (type 5)")
	print("☆Cube of a number      (type 6)")
	print("☆Modulas               (type 7)")
	user_input=input('\n$ Enter corresponding numbers : ')
	if user_input=="1" or user_input=="add":
		a=int(input("-Enter first number : "))
		b=int(input("-Enter second number : "))
		c=int(input('-Enter third number : '))
		time.sleep(0.8)
		print('--Sum of the numbers are : ',a+b+c)
	elif user_input=="2" or user_input=="sub" or user_input=="subtract":
		a=int(input("-Enter first number : "))
		b=int(input("-Enter second number : "))
		print("--Difference of the numbers are : ",a-b)
	elif user_input=="3" or user_input=="multiply" or user_input=="mul":
		a=int(input("-Enter first number : "))
		b=int(input("-Enter second number : "))
		print("--Product of the numbers are : ",a*b)
	elif user_input=="4" or user_input=="div" or user_input=="division":
		a=int(input("-Enter first number : "))
		b=int(input("-Enter second number : "))
		print("--Quotient of the numbers are : ",a/b)
	elif user_input=="5" or user_input=="square" or user_input=="sqaure root":
		a=int(input("-Enter the number : "))
		print("--Square of the numbers is : ",a**2)
	elif user_input=="6" or user_input=="cube" or user_input=="cube root":
		a=int(input("-Enter the number : "))
		print("--Cube of the number is : ",a**3)
	elif user_input=="7" or user_input=="mod" or user_input=="modulas":
		a=int(input("-Enter first number : "))
		b=int(input("-Enter second number : "))
		print("--Remainder is : ",a%b)
	elif user_input=="33117799" or user_input=="22557788":
		break
	else:
		print("Invalid input !")
#Simple Calculator ends

#Advance Calculator starts
#Advance Calculator function..
def advance_calculator():
	def askForNumInput(textPrompt):
		convertedNum = math.nan
		while True:
			num = input(textPrompt)
			try:
				float(num)
			except ValueError:
				print("ERROR: Syn: Invalid Num")
			else:
				convertedNum = float(num)
				break
		return convertedNum
	def abilitiesList():
		print("+...Addition")
		print("-...Subtraction")
		print("*...Multiplication")
		print("/...Division")
		print("^...Powers")
		print("/-...Square Roots ")
		print("!...Factorials (Input Cannot Be Negetave)")
		print("Abs...Absolute Value")
		print("d/r...Degrees To Radians")
		print("r/d...Radians To Degrees")
		print("pi...Returns PI")
		print("e...Returs 'e'")
		print("tau...Returns TAU (2xPI)")
		print("M+...Save input to memory")
		print("MR...Recall Memory")
		print("M-...Clear Memory")
		print("sin...Sine")
		print("cos...Cosine")
		print("tan...Tangent")
		print("asin...Arc Sine")
		print("acos...Arc Cosine")
		print("atan...Arc Tangent")
		print("log10...Log(10) of Input")
		print("log...Returns The Apropriate Log of the Input (input1 is the log power)")
		print("rand...Returns A Random Number Between 0 and 1")
		print("randint...Returns A Random Number Between The Two Inputs")
		print("/////////////////////////////////////////////////////")
	print("/////////////////////////////////////////////////////")
	time.sleep(0.5)
	print("$ Type 'help' for a list of abilities")
	while True:
		time.sleep(0.9)
		operator = input("\n@ What operation do you want to perform? ")
		if operator == "help":
			abilitiesList()
		elif operator == "pi":
			print(math.pi)
		elif operator == "e":
			print(math.e)
		elif operator == "tau":
			print(math.pi*2)
		elif operator == "MR":
			print(str(memStore))
		elif operator == "M-":
			memStore = "Empty"
			print("Memory Cleared")
		elif operator == "rand":
			print(random.random())
		elif operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "^" or operator == "/-" or operator == "!" or operator == "Abs" or operator == "d/r" or operator == "r/d" or operator == "M+" or operator == "M-" or operator == "MR" or operator == "sin" or operator == "cos" or operator == "tan" or operator == "asin" or operator == "acos" or operator == "atan" or operator == "log10" or operator == "log" or operator == "randint" or operator=="add" or operator=="sum" or operator=="sub" or operator=="subtract" or operator=="mul" or operator=="multiply" or operator=="div" or operator=="divide" or operator=="÷" or operator=="addition" or operator=="substraction" or operator=="multiplication" or operator=="division":
			break
		else:
			print("ERROR: Invalid Operator")
	while True:
		while True:
			num1 = askForNumInput("# First Number? ")
			if (operator == "asin" or operator == "acos") and (num1 > 1 or num1 < -1):
				print("ERROR: Math: 'asin' and 'acos' commands only accept inputs in range -1 to +1")
			elif operator == "!" and num1 < 0:
				print("ERROR: Math: Factorials only accept inputs > 0")
			else:
				break
		if not (operator=="/-" or operator=="!" or operator=="Abs" or operator=="d/r" or operator=="r/d" or operator=="M+" or operator=="sin" or operator=="cos" or operator=="tan" or operator=="asin" or operator=="acos" or operator=="atan" or operator=="log10"):
			while True:
				num2=askForNumInput("# Second Number? ")
				if  operator == "/" and num2 == "0":
					print("ERROR: Math: Cannot divide by 0!")
				else:
					break
		if operator == "+" or operator=="add" or operator=="sum" or operator=="addition":
			output = num1 + num2
			print("\n--Your Answer: "+str(output))
		elif operator == "-" or operator=="sub" or operator=="subtract" or operator=="substraction":
			output = num1 - num2
			print("\n--Your Answer: "+str(output))
		elif operator == "*" or operator=="mul" or operator=="multiply" or operator=="multiplication":
			output = num1 * num2
			print("\n--Your Answer: "+str(output))
		elif operator == "/"or operator=="div" or operator=="divide" or operator=="÷" or operator=="division":
			output = num1 / num2
			print("\n--Your Answer: "+str(output))
		elif operator == "^":
			output = math.pow(num1,num2)
			print("\n--Your Answer: "+str(output))
		elif operator == "/-":
			output = math.sqrt(num1)
			print("\n--Your Answer: "+str(output))
		elif operator == "!":
			output = math.factorial(num1)
			print("\n--Your Answer: "+str(output))
		elif operator == "Abs":
			output = math.fabs(num1)
			print("\n--Your Answer: "+str(output))
		elif operator == "d/r":
			output = math.radians(num1)
			print("\n--Your Answer: "+str(output))
		elif operator == "r/d":
			output = math.degrees(num1)
			print("\n--Your Answer: "+str(output))
		elif operator == "M+":
			memStore = num1
			print("Number Stored")
		elif operator == "sin":
			output = math.sin(num1)
			print("\n--Your Answer: "+str(output))
		elif operator == "cos":
			output = math.cos(num1)
			print("\n--Your Answer: "+str(output))
		elif operator == "tan":
			output = math.tan(num1)
			print("\n--Your Answer: "+str(output))
		elif operator == "asin":
			output = math.asin(num1)
			print("\n--Your Answer: "+str(output))
		elif operator == "acos":
			output = math.acos(num1)
			print("\n--Your Answer: "+str(output))
		elif operator == "atan":
			output = math.atan(num1)
			print("\n--Your Answer: "+str(output))
		elif operator == "log10":
			output = math.log10(num1)
			print("\n--Your Answer: "+str(output))
		elif operator == "log":
			output = math.log(num2, num1)
			print("\n--Your Answer: "+str(output))
		elif operator == "randint":
			output = random.randint(num1, num2)
			print("\n--Your Answer: "+str(output))
#Advance Calculator ends


#Interactive calculator starts
#function for interactive calculator..
def interactive_calculator():
	response=['Hello I am smart calculator','My name is EURO','Thanks for enjoy with me ','']
	def extract_from_text(text):
		l=[]
		for t in text.split(' '):
			try:
				l.append(float(t))
			except ValueError:
				pass
		return l 
	def lcm(a,b):
		L=a if a>b else b
		while L<=a*b:
			if L%a==0 and L%b==0:
				return L
			L+=1
	
	def hcf(a,b):
		H=a if a<b else b
		while H>=1:
			if a%H==0 and b%H==0:
				return H
			H-=1
	def add(a,b):
		return a+b
	
	def sub(a,b):
		return a-b
	
	def mul(a,b):
		return a*b
	
	def div(a,b):
		return a/b
	
	def mod(a,b):
		return a%b
	
	def end():
		print(response[2])
		input('press enter key to exit')
		exit()
	
	def myname():
		print(response[1]) 
	
	def sorry():
		print(response[3])
	
	operations={'ADD':add,'PLUS':add,'SUM':add,'ADDITION':add,'SUB':sub,'SUBTRACT':sub, 'MINUS':sub,'DIFFERENCE':sub,'LCM':lcm,'HCF':hcf,'PRODUCT':mul, 'MULTIPLY':mul,'MULTIPLICATION':mul,'DIVISION':div,'MOD':mod,'REMANDER':mod,'MODULAS':mod}
	
	commands={'NAME':myname,'EXIT':end,'END':end,'CLOSE':end}
	print(("*******Type \'help\' for help\n"))
	print('$ '+response[0])
	time.sleep(0.7)
	print('$ '+response[1]+'')
	
	while True:
		print()
		text=input('enter your queries:  ') .lower()
		if "help" in text:
			print("This smart calculator works on the text statement also. The user need not provide algebraic expression always. It fetches the word form the command (given by the user) and then formulates the expression.")
			continue
		for word in text.split(' '):
			if word.upper() in operations.keys():
				try:
					l = extract_from_text(text)
					r = operations[word.upper()] (l[0],l[1])
					print(r)
				except:
					print('something went wrong going plz enter again !!')
				finally:
					break
			
			elif word.upper() in commands.keys():
				commands[word.upper()]()
				break
			else:
				sorry()
#interactive calculator ends

#calling functions
if user_input=="33117799":
	time.sleep(2)
	print("\nEntering Advance mode....")
	time.sleep(1)
	print("."*53)
	time.sleep(1)
	print("."*53)
	time.sleep(1)
	print("."*53)
	time.sleep(1)
	print("."*53)
	time.sleep(2.7)
	print(Fore.GREEN,pyfiglet.figlet_format("ADVANCE"))
	advance_calculator()

elif user_input=="22557788":
	time.sleep(2)
	print("\nEntering Interactive mode....")
	time.sleep(1)
	print("."*53)
	time.sleep(1)
	print("."*53)
	time.sleep(1)
	print("."*53)
	time.sleep(1)
	print("."*53)
	time.sleep(2.7)
	print(Fore.GREEN,pyfiglet.figlet_format("INTERACTIVE"))
	interactive_calculator()
	
