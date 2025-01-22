from dummyclass import *
dc = Dummyclass()
#Access via properties
print("dc.nv : ID " + str(id(dc.nv)) + " Value : " + dc.nv)
print("dc.v : ID " + str(id(dc.v)) + " Value : " + dc.v)
print()

print("Attempt to change dc.__nv")
dc.__nv = "This cannot be changed"
print("dc.__nv : ID " + str(id(dc.__nv)) + " Value : " + dc.__nv)
print("dc.nv : ID " + str(id(dc.nv)) + " Value : " + dc.nv)
dc._v = "This is visible and already edited"
print("dc.v : ID " + str(id(dc.v)) + " Value : " + dc.v)
print("dc._v : ID " + str(id(dc._v)) + " Value : " + dc._v)