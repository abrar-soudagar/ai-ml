s1 = {"a", "b", "c", "d", "e"}
print("S1:", s1)

s2 = {"d", "e", "f", "g"}
print("S2:", s2)

# Union
s1ors2 = s1 | s2
print("S1 UNION S2:",s1ors2)

# Intesection
s1ands2 = s1 & s2
print("S1 INTERSECTION S2:",s1ands2)

# Set Difference
s1minuss2 = s1 - s2
print("S1 - S2: ",s1minuss2)
