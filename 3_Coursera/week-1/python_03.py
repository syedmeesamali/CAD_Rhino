import rhinoscriptsyntax as rs
x = 5
n = 5*(x-2)
crvId = rs.GetObject("select a curve: ", rs.filter.curve)
endPt = rs.CurveEndPoint(crvId)
line = rs.AddLine((0,0,0), endPt)

#output
print(x)
print(n)
print(crvId)
print(endPt)
print(line)