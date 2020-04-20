my_list = [24, 15, 17, 21, 15]

def find_duplicate(arr):
	arr.sort()
	prev = 0
	for i in arr:
		if prev == i:
			return i
		prev = i

#Expected: 15
print(find_duplicate(my_list))