def remove_outliers(data, n):
    if len(data) < 2 * n:
        raise ValueError("List must contain at least 2*n elements")
    
    sorted_data = sorted(data)
    return sorted_data[n:-n]

data_input = input("Enter a list of numbers separated by spaces: ")
data_list = [float(x) for x in data_input.split()]
    
if len(data_list) < 4:
    print("The list must contain at least 4 numbers.")

else:       
    result = remove_outliers(data_list, 2)
    print("Original list:", data_list)
    print("List with outliers removed:", result)






