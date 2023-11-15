def Bubble_Sort(list):
    n=len(list)
    for i in range(n):
        for j in range(0,n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


input_str = input("Enter a list of numbers separated by spaces: ")
input_list = input_str.split()
my_list = []

for num in input_list:
    my_list.append(int(num))


Bubble_Sort(my_list)


print("Sorted array:", my_list)
