list=[1,2,3,4,5,5,5,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(f"List before removing duplicates->{list}")
newList=[]
[newList.append(i) for i in list if i not in newList]
print(f"After removing duplicates->{newList}")