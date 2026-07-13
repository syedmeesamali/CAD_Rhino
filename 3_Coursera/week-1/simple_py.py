import rhinoscriptsyntax as rs

r = rs.GetReal('Input real number')
print(r ** 2)
rs.AddLine((0,0,0), (r,r*2,0))
rs.AddArc((0,0,0), r * 1.5, 50)
