import rhinoscriptsyntax as rs

ptGUID = rs.GetObject('Select a point', rs.filter.point)
print(ptGUID)

pt_Coord = rs.PointCoordinates(ptGUID)
print(pt_Coord)