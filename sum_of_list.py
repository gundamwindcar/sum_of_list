def sum_of_list(lists):
	return sum(lists)

numbers =[]
count = input('How many numbers are you going to enter:')
count = int(count)

for i in range(count):
	n = input('Please enter the number:')
	n = int(n)
	numbers.append(n)

print(sum_of_list(numbers))