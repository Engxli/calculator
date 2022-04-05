
from ast import operator
from curses.ascii import isdigit


def main():
	#write your code here

	firstNum = input("Enter the first number: ")
	secondNum = input("Enter the seoncd number: ")
	operation = input("Choose the operation (+, -, /, *): ")

	if (operation in "+*-/" and firstNum.isdigit() and secondNum.isdigit() ):
		ans = f"{str(firstNum)}{operation}{str(secondNum)}"
		print("The answer is: ", str(round(eval(ans))))
	else:
		print("the operation is not valid")




if __name__ == '__main__':
	main()
