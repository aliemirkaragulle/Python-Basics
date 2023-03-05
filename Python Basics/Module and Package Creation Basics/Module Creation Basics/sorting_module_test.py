import sorting_module

arr = [1,3,5,9,11,2,4,6,8,10,55,22,0,11,22,99,555]

bubble_sorted_arr = sorting_module.bubble_sort(arr)
insertion_sorted_arr = sorting_module.insertion_sort(arr)

# from sorting_module import bubble_sort, insertion_sort

# bubble_sorted_arr = bubble_sort(arr)
# insertion_sorted_arr = insertion_sort(arr)

print(bubble_sorted_arr)
print(insertion_sorted_arr)