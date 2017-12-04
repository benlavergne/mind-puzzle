# ---------------------------
#
# Aristotle digital mind game
#
# ---------------------------

import sys
import numpy as np
from collections import Counter

# dictionnary with all numbers and their availability (true, false)
numbers = {}
max_n = 19


def init_digit_pool(max_number):
	init_values = {}

	for i in range(max_number):
		init_values[i+1] = True

	return init_values


def search_line2(max_number, successLine, numbers, line1, line2, line3, line4, line5):
	for i in range(max_number):
		if numbers[i+1] and not successLine[1]:
			line2[0] = i+1
			numbers[i+1] = False
			for j in range(max_number):
				if numbers[j+1] and not successLine[1]:
					line2[1] = j+1
					numbers[j+1] = False
					for k in range(max_number):
						if numbers[k+1] and not successLine[1]:
							line2[2] = k+1
							numbers[k+1] = False
							for l in range(max_number):
								if numbers[l+1] and not successLine[1]:
									line2[3] = l+1
									numbers[l+1] = False
									if (line2[0]+line2[1]+line2[2]+line2[3] == 38):
										# -------------------
										# proceed with line 3
										# -------------------
										successLine[1] = search_line3(max_number, successLine, numbers, line1, line2, line3, line4, line5)
									else:
										numbers[l+1] = True
									if not successLine[1]:
										numbers[l+1] = True
							if not successLine[1]:
								numbers[k+1] = True
					if not successLine[1]:
						numbers[j+1] = True
			if not successLine[1]:
				numbers[i+1] = True

	return successLine[1]


def search_line3(max_number, successLine, numbers, line1, line2, line3, line4, line5):
	for i in range(max_number):
		if numbers[i+1] and not successLine[2]:
			line3[0] = i+1
			numbers[i+1] = False
			if (line1[0]+line2[0]+line3[0] == 38):
				for j in range(max_number):
					if numbers[j+1] and not successLine[2]:
						line3[1] = j+1
						numbers[j+1] = False
						for k in range(max_number):
							if numbers[k+1] and not successLine[2]:
								line3[2] = k+1
								numbers[k+1] = False
								for l in range(max_number):
									if numbers[l+1] and not successLine[2]:
										line3[3] = l+1
										numbers[l+1] = False
										for m in range(max_number):
											if numbers[m+1] and not successLine[2]:
												line3[4] = m+1
												numbers[m+1] = False
												if (line3[0]+line3[1]+line3[2]+line3[3]+line3[4] == 38) and (line1[2]+line2[3]+line3[4] == 38):
													# -------------------
													# proceed with line 4
													# -------------------
													successLine[2] = search_line4(max_number, successLine, numbers, line1, line2, line3, line4, line5)
												else:
													numbers[m+1] = True
												if not successLine[2]:
													numbers[m+1] = True
										if not successLine[2]:
											numbers[l+1] = True
								if not successLine[2]:
									numbers[k+1] = True
						if not successLine[2]:
							numbers[j+1] = True
			else:
				numbers[i+1] = True
			if not successLine[2]:
				numbers[i+1] = True

	return successLine[2]


def search_line4(max_number, successLine, numbers, line1, line2, line3, line4, line5):
	for i in range(max_number):
		if numbers[i+1] and not successLine[3]:
			line4[0] = i+1
			numbers[i+1] = False
			if (line1[1]+line2[1]+line3[1]+line4[0] == 38):
				for j in range(max_number):
					if numbers[j+1] and not successLine[3]:
						line4[1] = j+1
						numbers[j+1] = False
						for k in range(max_number):
							if numbers[k+1] and not successLine[3]:
								line4[2] = k+1
								numbers[k+1] = False
								for l in range(max_number):
									if numbers[l+1] and not successLine[3]:
										line4[3] = l+1
										numbers[l+1] = False
										if (line4[0]+line4[1]+line4[2]+line4[3] == 38) and (line1[1]+line2[2]+line3[3]+line4[3] == 38):
											# -------------------
											# proceed with line 5
											# -------------------
											successLine[3] = search_line5(max_number, successLine, numbers, line1, line2, line3, line4, line5)
										else:
											numbers[l+1] = True
										if not successLine[3]:
											numbers[l+1] = True
								if not successLine[3]:
									numbers[k+1] = True
						if not successLine[3]:
							numbers[j+1] = True
			else:
				numbers[i+1] = True
			if not successLine[3]:
				numbers[i+1] = True

	return successLine[3]

def search_line5(max_number, successLine, numbers, line1, line2, line3, line4, line5):
	for i in range(max_number):
		if numbers[i+1] and not successLine[4]:
			line5[0] = i+1
			numbers[i+1] = False
			if (line3[0]+line4[0]+line5[0] == 38) and (line1[2]+line2[2]+line3[2]+line4[1]+line5[0] == 38):
				for j in range(max_number):
					if numbers[j+1] and not successLine[4]:
						line5[1] = j+1
						numbers[j+1] = False
						if (line2[0]+line3[1]+line4[1]+line5[1] == 38) and (line2[3]+line3[3]+line4[2]+line5[1] == 38):
							for k in range(max_number):
								if numbers[k+1] and not successLine[4]:
									line5[2] = k+1
									numbers[k+1] = False
									if (line5[0]+line5[1]+line5[2] == 38) and (line1[0]+line2[1]+line3[2]+line4[2]+line5[2] == 38) and (line3[4]+line4[3]+line5[2] == 38):
										# -------------------
										# Solution Found !!!!
										# -------------------
										successLine[4] = True
									else:
										numbers[k+1] = True
									if not successLine[4]:
										numbers[k+1] = True
						else:
							numbers[j+1] = True
						if not successLine[4]:
							numbers[j+1] = True
			else:
				numbers[i+1] = True
			if not successLine[4]:
				numbers[i+1] = True

	return successLine[4]



def search_puzzle(max_number):
	numbers = init_digit_pool(max_number)

	# create 5 target lines
	line1 = [0,0,0]
	line2 = [0,0,0,0]
	line3 = [0,0,0,0,0]
	line4 = [0,0,0,0]
	line5 = [0,0,0]

	successLine = [False, False, False, False, False]

	for i in range(max_number):
		if numbers[i+1] and not successLine[0]:
			line1[0] = i+1
			numbers[i+1] = False
			for j in range(max_number):
				if numbers[j+1] and not successLine[0]:
					line1[1] = j+1
					numbers[j+1] = False
					for k in range(max_number):
						if numbers[k+1] and not successLine[0]:
							line1[2] = k+1
							numbers[k+1] = False
							if (line1[0]+line1[1]+line1[2] == 38):
								# -------------------
								# proceed with line 2
								# -------------------
								successLine[0] = search_line2(max_number, successLine, numbers, line1, line2, line3, line4, line5)
							else:
								numbers[k+1] = True
							if not successLine[0]:
								numbers[k+1] = True
					if not successLine[0]:
						numbers[j+1] = True
			if not successLine[0]:
				numbers[i+1] = True

	if successLine[0]:
		display_puzzle(line1, line2, line3, line4, line5)
	else:
		print("Problem...")

def display_puzzle(line1, line2, line3, line4, line5):
	# display the result
	# ------------------
	#sys.stdout.flush()
	sys.stdout.write('\r\n' + '   ' + ''.join(str(line1[i]).center(3) for i in range(3)) + '\n' \
					+ '  ' + ''.join(str(line2[i]).center(3) for i in range(4)) + '\n' \
					+ ''.join(str(line3[i]).center(3) for i in range(5)) + '\n' \
					+ '  ' + ''.join(str(line4[i]).center(3) for i in range(4)) + '\n' \
					+ '   ' + ''.join(str(line5[i]).center(3) for i in range(3)) + '\n\n')
	sys.stdout.flush()


if __name__ == '__main__':
	# input interface
	# ---------------
	search_puzzle(19)