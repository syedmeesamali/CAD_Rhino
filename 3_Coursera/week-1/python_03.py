import rhinoscriptsyntax as rs
#Points in the rhino space

#ptGUID = rs.GetObject('Select a point', rs.filter.point)
#print(ptGUID)

#pt_Coord = rs.PointCoordinates(ptGUID)
#print(pt_Coord)

#Add line with the coordinates
new_point = (0, 2, 0)
rs.AddLine(new_point, (5, 10, 0))

startpt = rs.GetObject('select point 1', rs.filter.point)
endpt = rs.GetObject('select point 2', rs.filter.point)

start1 = rs.PointCoordinates(startpt)
end1 = rs.PointCoordinates(endpt)

objRect = rs.GetObject('select object', rs.filter.curve)
rs.MoveObject(objRect, end1 - start1)