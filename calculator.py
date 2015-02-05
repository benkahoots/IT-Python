#Introduces the user to the simple calculator program
print "Welcome to My Simple Calculator Light!"

print "If you would like to know how the system works type '\?'"

#Decides if the user wants help
operator = raw_input("Enter Operator")
if user == "?":
	print "The way to use My Simple Calculator Light is by first entering your first number that you would like to Divide, Multiply, Add, Subtract and '\to the power of.' If you would like to exit/quit the program type in '\Q' or '\Quit'"

elif user == "pass":
	print "Ok we will continue to My Simple Calculator Lite"
	
#Will define all operators and what they do
def Add(num_1, num_2):
	return num_1 + num_2
	
def Sub(num_1, num_2):
	return num_1 - num_2
	
def Div(num_1, num_2):
	return num_1 / num_2
	
def Mul(num_1, num_2):
	return num_1 * num_2

def Pow(num_1, num_2):
	return num_1**num_2
	
#This is showing the opperators
num_1 = raw_input("Enter First Number: ")
print "First Number Entered"
	
operation = raw_input("Enter operation e.g. '\+, -, /, x, '\^' ")
if operator == "+":
	return Add
	
elif operator == "-":
	return Sub
	
elif operator == "/":
        return Div
	
elif operator == "x":
        return Mul

elif operator == "^":
	return Pow

else:
	return "You did not enter a vaild number"
	
num_2 = raw_input("Enter Second Number: ")
print "First Number Entered"

print operation 
