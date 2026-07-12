import rhinoscriptsyntax as rs
#Code comments with hash

box = rs.GetObject('input a box', rs.filter.polysurface)
print(box)
r = rs.GetReal('Input real number')
print(r ** 2)
rs.AddLine((0,0,0), (r,r*2,0))
