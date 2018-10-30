import sys

# state 0 - both are variables
class stateZero():

	# lowerBound = -sys.maxint
	# upperBound = sys.maxint

	lowerBound = 0
	upperBound = 5

	def __init__(self):
		return

	def add(self, total, minn=0, maxx=sys.maxint):
		for a in range(minn, total):
			for b in range(minn, total):
				result = a + b
				if result > total:
					break
				if result == total:
					print('A: ', a, '. B: ', b)
					break

		return total - curr

	def subtract(self, curr, total, min=0, maxx=sys.maxint):
		return

	def multiply(self, curr, total):
		return

	def divide(self, curr, total):
		return		


# state 1 and 2 functions

class stateOne():
	def __init__(self):
		return

	def add(self, curr, total, min=0, maxx=sys.maxint):
		return total - curr

	def subtract(self, curr, total, min=0, maxx=sys.maxint):
		return curr - total

	def multiply(self, curr, total):
		return total / curr

	def divide(self, curr, total):
		return curr * total		



class Parser():

	def __init__(self):
		self.stateOne = stateOne()
		return

	def __init__(self, term_input):
		self.stateOne = stateOne()
		self.parseInput(term_input)

	def parseInput(self, term_input):
		# check function call
		pieces = term_input.split('(', 1)
		# print("Function call: ", pieces[0])


		# get constraints
		constraints = pieces[1].split('[')[1][:-2].split(', ')
		# print(constraints)

		# get arguments
		args = pieces[1].split('[')[0].split(', ')
		# print(args)

		# get operator
		operator_map = {
			 '+': self.stateOne.add,
			 '-': self.stateOne.subtract,
			 '*': self.stateOne.multiply,
			 '/': self.stateOne.divide,
			 'F': 'function'
		}
		operation = operator_map[args[0]]

		# get first number
		a = args[1]

		# get second number
		b = args[2]

		# wanted total (converted to int) 	# check to make sure total is an int
		total = int(float(args[3]))

		# print('Operation: ', operation)
		# print('A: ', a)
		# print('B: ', b)
		# print('Total: ', total)

		# determine if a and b are numbers or variables
			# state = 0: both ints
			# state = 1: A is int, B is var
			# state = 2: A is var, B is int
			# state = 3: both are var

		state = 0

		a_is_var = False
		b_is_var = False

		try:
			int(a)
			a = int(float(a))
		except ValueError:
			a_is_var = True

		try:
			int(b)
			b = int(float(b))
		except ValueError:
			b_is_var = True

		# what to do with each option
		if b_is_var and a_is_var:
			state = 0
		
		elif b_is_var and not a_is_var:
			print(operation(a, total))
		
		elif not b_is_var and a_is_var:
			print(operation(b, total))
		
		elif not b_is_var and not a_is_var:
			state = 3




# mock_input = 'satisfy(+, A, 1, 2, [])'

# mock_input_with_constraints = 'satisfy(+, A, 1, 2, [A <= 2, B <= 2])'

# p = Parser(mock_input)

# p.parseInput(mock_input)


