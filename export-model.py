cube=bpy.data.objects["Cube"]
cubedata = bpy.data.meshes['Cube']
for v in cubedata.vertices: print(v.co)
triangles=[]
for f in cubedata.polygons:
    # face_verts = f.vertices
    # list(f)					//simply a list of all face vertices printed	
    if len(f.vertices)==3:
	for vi in f.vertices:
            xf=cubedata.vertices[vi].co
            triangles.append((xf[0],xf[1],xf[2]))
    else:
	for vi in f.vertices:				// Second condition as quad comprises of two triangles
	    xf=cubedata.vertices[vi].co
            triangles.append((xf[0],xf[1],xf[2]))
            triangles.append((xf[0],xf[2],xf[3]))

print(triangles)

# Ref: http://brucesutherland.blogspot.com/2012/05/blender-262-writing-export-script_21.html