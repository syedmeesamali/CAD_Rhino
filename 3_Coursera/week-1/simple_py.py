import rhinoscriptsyntax as rs
#Code comments with hash

box = rs.GetObject('input a box', rs.filter.polysurface)
print(box)
