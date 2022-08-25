a1 = {1,2,3,4}
a1 |= {5} # a1 = a1 | {5}
print(a1)

a2 = {1,2,3,4}
a2.update({5})
print(a2)
# ---------------
a3 = {1,2,3,4}
a3 &= {0,1,2,3,4}
print(a3)
a3.intersection_update({0,1,2,3,4,5})
print(a3)
a3.remove(3)
print(a3)