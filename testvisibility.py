from dummyclass import *
dc = Dummyclass()
#Access via properties
print(dc.v)
print(dc.nv)

dc._v = "This is visible and already edited"
print(dc.v)

dc.__nv = "This cannot be changed"
print(id(dc.__nv))
print(dc.__nv)
print(id(dc.nv))
print(dc.nv)