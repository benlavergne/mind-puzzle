'''
Aristotle Numbers Puzzle
------------------------
With numbers ranging from 1 to 19, create lines equal to 38 (diagonals included)

  - - -            1 18 19
 - - - -          ?  ?  ?  ?
- - - - -   ==>  ?  ?  ?  ?  ?
 - - - -          ?  ?  ?  ?
  - - -            ?  ?  ?

'''

from timeit import default_timer as timer

def init_digit_pool(max_number):
	''' Initialize dictionnary of numbers with their availability (True/False)
	'''
	init_values = {}

	for i in range(1, max_number+1):
		init_values[i] = True

	return init_values

def search_line1(max_number, numbers, line1, line2, line3, line4, line5):
	'''  Search line 1
	'''
	successLine = False

	for i in range(1, max_number+1):
		if numbers[i]:
			line1[0] = i
			numbers[i] = False
			for j in range(1, max_number+1):
				sum_digit = line1[0]+j
				if numbers[j] and (sum_digit >= 19):
					line1[1] = j
					numbers[j] = False
					diff = 38 - sum_digit
					if numbers[diff]:
						line1[2] = diff
						numbers[diff] = False
						# -------------------
						# proceed with line 2
						# -------------------
						successLine = search_line2(max_number, numbers, line1, line2, line3, line4, line5)
						if not successLine:
							numbers[diff] = True
					if not successLine:
						numbers[j] = True
					else:
						break
			if not successLine:
				numbers[i] = True
			else:
				break

	return successLine

def search_line2(max_number, numbers, line1, line2, line3, line4, line5):
	'''  Search line 2
	'''
	successLine = False

	for i in range(1, max_number+1):
		range_constraint = line1[0]+i
		if numbers[i] and (range_constraint >= 19):
			line2[0] = i
			numbers[i] = False
			for j in range(1, max_number+1):
				if numbers[j] and not successLine:
					line2[1] = j
					numbers[j] = False
					for k in range(1, max_number+1):
						sum_digit = line2[0]+line2[1]+k
						if numbers[k] and (sum_digit >= 19) and (sum_digit < 38):
							line2[2] = k
							numbers[k] = False
							diff = 38 - sum_digit
							if numbers[diff] and (line1[2]+diff >= 19):
								line2[3] = diff
								numbers[diff] = False
								# -------------------
								# proceed with line 3
								# -------------------
								successLine = search_line3(max_number, numbers, line1, line2, line3, line4, line5)
								if not successLine:
									numbers[diff] = True
							if not successLine:
								numbers[k] = True
							else:
								break
					if not successLine:
						numbers[j] = True
					else:
						break
			if not successLine:
				numbers[i] = True
			else:
				break

	return successLine

def search_line3(max_number, numbers, line1, line2, line3, line4, line5):
	'''  Search line 3
	'''
	successLine = False

	only_choice = 38 - line1[0] - line2[0]
	if (only_choice >= 1) and (only_choice <= 19):
		if numbers[only_choice]:
			line3[0] = only_choice
			numbers[only_choice] = False
			for j in range(1, max_number+1):
				mid1 = line1[1]+line2[1]+j
				if numbers[j] and (mid1 >= 19) and (mid1 < 38):
					line3[1] = j
					numbers[j] = False
					for k in range(1, max_number+1):
						if numbers[k]:
							line3[2] = k
							numbers[k] = False
							for l in range(1, max_number+1):
								sum_digit = line3[0]+line3[1]+line3[2]+l
								if numbers[l] and (sum_digit >= 19) and (sum_digit < 38):
									line3[3] = l
									numbers[l] = False
									diff = 38 - sum_digit
									if numbers[diff] and (line1[2]+line2[3]+diff == 38):
										line3[4] = diff
										numbers[diff] = False
										# -------------------
										# proceed with line 4
										# -------------------
										successLine = search_line4(max_number, numbers, line1, line2, line3, line4, line5)
										if not successLine:
											numbers[diff] = True
									if not successLine:
										numbers[l] = True
									else:
										break
							if not successLine:
								numbers[k] = True
							else:
								break
					if not successLine:
						numbers[j] = True
					else:
						break
			if not successLine:
				numbers[only_choice] = True

	return successLine

def search_line4(max_number, numbers, line1, line2, line3, line4, line5):
	'''  Search line 4
	'''
	successLine = False

	only_choice = 38 - line1[1] - line2[1] - line3[1]
	if (only_choice >= 1) and (only_choice <= 19):
		if numbers[only_choice]:
			line4[0] = only_choice
			numbers[only_choice] = False
			for j in range(1, max_number+1):
				mid1 = line2[0]+line3[1]+j
				if numbers[j] and (mid1 >= 19) and (mid1 < 38):
					line4[1] = j
					numbers[j] = False
					for k in range(1, max_number+1):
						sum_digit = line4[0]+line4[1]+k
						if numbers[k] and (sum_digit >= 19) and (sum_digit < 38):
							line4[2] = k
							numbers[k] = False
							diff = 38 - sum_digit
							if numbers[diff] and (line1[1]+line2[2]+line3[3]+diff == 38):
								line4[3] = diff
								numbers[diff] = False
								# -------------------
								# proceed with line 5
								# -------------------
								successLine = search_line5(max_number, numbers, line1, line2, line3, line4, line5)
								if not successLine:
									numbers[diff] = True
							if not successLine:
								numbers[k] = True
							else:
								break
					if not successLine:
						numbers[j] = True
					else:
						break
			if not successLine:
				numbers[only_choice] = True

	return successLine


def search_line5(max_number, numbers, line1, line2, line3, line4, line5):
	'''  Search line 5
	'''
	successLine = False

	only_choice = 38 - line3[0] - line4[0]
	if (only_choice >= 1) and (only_choice <= 19):
		if numbers[only_choice] and (line1[2]+line2[2]+line3[2]+line4[1]+only_choice == 38):
			line5[0] = only_choice
			numbers[only_choice] = False

			before_last = 38 - line2[0] - line3[1] - line4[1]
			if (before_last >= 1) and (before_last <= 19):
				if numbers[before_last] and (line2[3]+line3[3]+line4[2]+before_last == 38):
					line5[1] = before_last
					numbers[before_last] = False

					sum_digit = line5[0] + line5[1]
					if (sum_digit >= 19):
						diff = 38 - sum_digit
						if numbers[diff] and (line1[0]+line2[1]+line3[2]+line4[2]+diff == 38) and (line3[4]+line4[3]+diff == 38):
							line5[2] = diff
							numbers[diff] = False
							# -------------------
							# Solution Found !!!!
							# -------------------
							successLine = True

					if not successLine:
						numbers[before_last] = True

			if not successLine:
				numbers[only_choice] = True

	return successLine

def search_puzzle(max_number):
	# start timer
	start = timer()

	# init data structure for all numbers with their availability
	numbers = init_digit_pool(max_number)

	# create 5 target lines
	line1 = [0,0,0]
	line2 = [0,0,0,0]
	line3 = [0,0,0,0,0]
	line4 = [0,0,0,0]
	line5 = [0,0,0]

	success = search_line1(max_number, numbers, line1, line2, line3, line4, line5)

	# end timer
	end = timer()

	if success:
		display_puzzle(line1, line2, line3, line4, line5)
		display_time(end - start)
	else:
		print("Problem...")

def display_puzzle(line1, line2, line3, line4, line5):
	print('\n' + '  ' + ''.join(str(line1[i]).center(3) for i in range(3)) + '\n' \
			+ ' ' + ''.join(str(line2[i]).center(3) for i in range(4)) + '\n' \
			+ ''.join(str(line3[i]).center(3) for i in range(5)) + '\n' \
			+ ' ' + ''.join(str(line4[i]).center(3) for i in range(4)) + '\n' \
			+ '  ' + ''.join(str(line5[i]).center(3) for i in range(3)) + '\n')

def display_time(time_length):
	print(" Time elapsed in seconds :", str(time_length)[:6])


if __name__ == '__main__':
	search_puzzle(19)