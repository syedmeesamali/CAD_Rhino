import rhinoscriptsyntax as rs

ptGUID = rs.GetObject('Select a point', rs.filter.point)
print(ptGUID)

pt_Coord = rs.PointCoordinates(ptGUID)
print(pt_Coord)

rs.AddLine((0,0,0), pt_Coord * 2)