my_list = [24, 15, 17, 21, 15]

def listDuplicates(arr):
	my_dict = { }

	for i in arr:
		if arr[i] in my_dict:
			return true
		else:
			my_dict[arr[i]] += 1

	return false

# Expected: true
print(listDuplicates(my_list))