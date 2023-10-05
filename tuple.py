tuple=(1,2,3,4,5)

print(f"Tuple={tuple}") #Print Whole Tuple
print(f"Access 0 index of Tuple={tuple[0]}")
print(f"Access -1 index of Tuple={tuple[-1]}")
print(f"Range of tuple from 0 to 2={tuple[0:2]}") #Note: The search will start at index 0 (included) and end at index 2 (not included).
print(f"Access -1 index of Tuple={tuple[-1]}")
print(f"Tuple from index 2 to last={tuple[2:]}")
print(f"Tuple from -3 to -1={tuple[-3:-1]}")
print(f"5 in tuple?={5 in tuple}")
print(f"100 in tuple?={100 in tuple}")
list=list(tuple)
print(f"Convert tuple into list={list}")
print(f"Count 5={tuple.count(5)}")
print(f"Index of 5={tuple.index(5)}")






