import rhinoscriptsyntax as rs
#Code comments with hash

x = rs.GetInteger('Input integer')
if (x % 2 == 0):
    print("Your number is even")
else:
    print("Odd number")
print(x * 2)