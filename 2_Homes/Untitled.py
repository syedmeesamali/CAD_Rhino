#! python 3
import rhinoscriptsyntax as rs
def helloworld():
    rs.MessageBox ("Hello World")

pnt = rs.CreatePoint(1.0, 2.0, 3.0)
pnt = rs.CreatePoint(1.0, 2.0) # This creates a point with the Z coordinate set to 0
rs.AddLine((45,56,32),(56,47,89))