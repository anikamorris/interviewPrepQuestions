my_list = [23, 15, 17, 21, 15]

def listDuplicates(arr):
	my_dict = {}

	for i in arr:
		if i in my_dict.keys():
			return True
		else:
			my_dict[i] = 1

	return False

# Expected: True
print(listDuplicates(my_list))