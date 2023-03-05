import SortingPackage.sorted_or_not
import SortingPackage.BubbleSortPackage.bubble_sort
import SortingPackage.InsertionSortPackage.insertion_sort

arr = [1,3,5,9,11,2,4,6,8,10,55,22,0,11,22,99,555]

is_sorted = SortingPackage.sorted_or_not.sorted_check(arr)
print(is_sorted)

bubble_sorted_arr = SortingPackage.BubbleSortPackage.bubble_sort.bubble_sort(arr)
insertion_sorted_arr = SortingPackage.InsertionSortPackage.insertion_sort.insertion_sort(arr)

print(bubble_sorted_arr)
print(insertion_sorted_arr)

""" 
from SortingPackage import sorted_or_not
from SortingPackage.BubbleSortPackage import bubble_sort
from SortingPackage.InsertionSortPackage import insertion_sort


arr = [1,3,5,9,11,2,4,6,8,10,55,22,0,11,22,99,555]

is_sorted = sorted_or_not.sorted_check(arr)
print(is_sorted)

bubble_sorted_arr = bubble_sort.bubble_sort(arr)
insertion_sorted_arr = insertion_sort.insertion_sort(arr)

print(bubble_sorted_arr)
print(insertion_sorted_arr)
"""