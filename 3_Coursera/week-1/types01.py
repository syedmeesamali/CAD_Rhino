#Data types
import rhinoscriptsyntax as rs

#Integer
intX = rs.GetInteger("Enter number: ", 4)

#Float
num = rs.GetReal("Enter float: ", 5.45)

#String
strVal = "This is some text."

#Boolean
bln1 = True
bln2 = False

#GUID
obj = rs.GetObject("Select a box: ", rs.filter.polysurface)
curve = rs.GetObject("Select a curve: ", rs.filter.curve)

#PRINT Values -------- 
print(intX)
print(num)
print(strVal)
print(bln1)
print(bln2)
print(obj), type(obj)
print(curve)