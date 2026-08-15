"""SET OPERATIONS METHODS"""
# 1.union()
# 2.intersection()
# 3.differnce_update()
# 4.difference()
# 5.symmetric_difference()

"""SET COMPARISON METHODS"""
# 1.issubset()
# 2.issuperset()
# 3.isdisjoint()
# 4.intersection_update()

"""SET MANIPULATION"""
# 1.len(set)
# 2.max(set)
# 3.min(set)
# 4.set()



A={1,2,3}
B={3,4,5}

print(A | B)  # | This symbol represent the union method. Uninon means its combbins two set and create a set but not print duplicate value in double print only one time.
print(A.union(B))  #It is also a  technique to create union method

print(A&B) # & This symbol means intersection method, Intersection means its print commom values of the two sets.
print(A.intersection(B)) #It is also a technique to create intersection method.

print(A-B) # - This symbol represent the difference.Its means its print those element whoes are not present in B but present in A.
print(B.difference(A)) #It's also a tecnique to print differnce.Its print those element whose present in B but not ptresent in A.

print(A ^ B) # ^ This symbol represnt the symmetric_difference.Its means its print those values/elements those are not common in two sets.
print(A.symmetric_difference(B))  #Its  also a technique to print symmtric_difference.

C={6,7}
D={6,7,8,9}

print(C.issubset(D))  # is subset check that all elements of first set is present in the second set.If set A all elements are present in B then its print B.
print(D.issubset(C)) #If not present then its print False.

