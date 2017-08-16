# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from shapely.geometry import Point, LineString, Polygon, MultiLineString
import matplotlib.pyplot as plt

import sqlite3
import pandas as pd
import geopandas as gpd

from shapely.ops import split, linemerge, unary_union
import shapely.wkt

line = LineString([(0, 0), (1, 1), (2, 2)])
point = Point(0.3, 0.7)
point

line = LineString([(0,0),(5,7),(12,6)])
list(line.coords)
p = Point(4,8)
list(p.coords)[0][0]

print(line.project(p))
np = line.interpolate(line.project(p))
print(np)

## lat lon coordinates
fon = Point(50.1074499,14.4296656)


# google map

gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)

gmap.scatter(50.1074499, 14.4296656, 'cornflowerblue', edge_width=10)
gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
gmap.heatmap(heat_lats, heat_lngs)

gmap.draw("mymap.html")

gmap = gmplot.from_geocode("Prague")

print(gmap)

plt.plot(p)

# plotting on matplotlib

poly = Polygon([(0, 0), (0, 2), (1, 1),
    (2, 2), (2, 0), (1, 0.8), (0, 0)])
x,y = poly.exterior.xy

ring = LinearRing([(0, 0), (0, 2), (1, 1),
    (2, 2), (2, 0), (1, 0.8), (0, 0)])
x, y = ring.xy

#ax = fig.add_subplot(111)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, color='#6699cc', alpha=0.7,
    linewidth=3, solid_capstyle='round', zorder=2)
ax.scatter(x, y, color='#6699cc', alpha=0.7)
ax.set_title('Polygon')
print(ax)
fig.show()
plt.show()

line1 = [4.5, 7.5]
line2 = [1.5, 9.5]

line = LineString([(0,0),(5,7),(12,6)])
list(line.coords)
p = Point(2,4)
np = line.interpolate(line.project(p))
print(np)
resp = split(line, np)
print(resp)
line.distance(np)

# x y of line
xl, yl = line.xy
xp, yp = p.xy

# test files

print(np)
np.y

line.distance(p)
np.distance(p)

line2 = LineString([(0, 6), (6, 5)])
np2 = line2.interpolate(line2.project(p))
line2.distance(p)

# matplotlib plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(xl, yl, color='#6699cc', alpha=0.7,
    linewidth=3, solid_capstyle='round', zorder=2)
ax.plot([0, 6], [6, 5], color='#6699cc', alpha=0.7,
    linewidth=3, solid_capstyle='round', zorder=2, label='streets')
ax.plot([2, np2.x], [4, np2.y], color='green', alpha=0.7, marker='o', label='node to street')
ax.plot([2, np.x], [4, np.y], color='red', alpha=0.7, marker='o', label='node to street')
plt.title('Connecting terminal nodes to streets with shortest path')
plt.legend(loc='lower right')
fig





ms = (df['WKT_GEOMETRY'][0])
sms = MultiLineString(ms.replace('MULTILINESTRING ', ''))

MultiLineString([((-747456.38 -1046097.94,-747372.44 -1046156.49),
                 (-747636.25 -1046039.89,-747523.15 -1046066.44,-747491.98 -1046073.85),
                 (-747491.98 -1046073.85,-747482.4 -1046080.33,-747456.38 -1046097.94),
                 (-747833.99 -1045992.11,-747636.25 -1046039.89))])

gdf = gpd.GeoDataFrame(df)
gdf.describe()


testp = Point(14.3620367370686, 50.0540745240015)
testml = geometry[0]

gg = testml.interpolate(testml.project(testp))
print(gg)
testml.distance(testp)

x, y = testml[0].xy
px, py = 

# Since the geometries often come in the WKT format, 
# I thought I'd include an example for that case as well:


# importing data from sqlite3
conn = sqlite3.connect('Prague_Streets_Subset_5514.sqlite')
prag_streets = pd.read_sql_query('SELECT * FROM prague_streets_subset_5514', conn)

conn = sqlite3.connect('Prague_Points_Subset_5514.sqlite')
prag_points = pd.read_sql_query('SELECT * FROM prague_points_subset_5514', conn)

prag_streets['street_geometry'] = prag_streets['WKT_GEOMETRY'].map(shapely.wkt.loads)
print(prag_streets['street_geometry'][0])

prag_points['point_geometry'] = prag_points['WKT_GEOMETRY'].map(shapely.wkt.loads)
print(prag_points['point_geometry'][0])

# calculation in a loop of closest points to lines
type(testml)

for i in range(len(testml)):
    print(testml[i].distance(testp))
            
# 
How to add new point to original multiline so it will be divided correctly?
1. transform multiline to linestring with from shapely.ops import linemerge
geo_linemerge = linemerge(geometry[0])
print(geo_linemerge)

# visualise the new line and added point to line
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, color='#6699cc', alpha=0.7,
    linewidth=3, solid_capstyle='round', zorder=2)
ax.scatter(x, y, color='#6699cc', alpha=0.7)
ax.set_title('Polygon')
print(ax)
fig.show()
plt.show()

# union point with linestring
union_line = geo_linemerge.union

from shapely.ops import split
np = line.interpolate(line.project(p))
# to split, point needs to be on line
result = split(line, np)
result.wkt

'GEOMETRYCOLLECTION (LINESTRING (1 2, 2 4), LINESTRING (2 4, 4 5))'

linka = LineString([(0,0), (1,1), (2,2)])
pinka = Point(0.5, 0.5)
res = split(linka, pinka)
print(res)

2. after finding the closest multistring from all, split the multistring at point
to create one more line in multistring
add the new result to new column of the same row.
Original - OriginalMultiLine
New - NewMultiLine (pointEnriched)
https://gis.stackexchange.com/questions/203048/split-lines-at-points-using-shapely

this way it looks like I won't have to break multiline into lines, 
but I can do it from high level functions - just find the closest multistring
and split the multistring at point of intersection + create new linestring
betweeen household and the closest point in multistring.

# split function is present from shapely version 1.62+ and is present only for Linux

# my version is 1.57 which doesn't have this function

3. Distance of every line will be calculated at the end after everything is split



# sometimes the intersect point doesn't lie on the 

print(intersect_point.coords[:][0])
print(new_line[0].coords[-1])

print(new_line)
print(intersect_point)

closest_line.distance(intersect_point)

new_line[0][0].within(new_line)

Point(new_line[0].xy[0], new_line[0].xy[1])

x, y = new_line[0].xy
ppp = Point(x[0], y[0])
ppp.within(new_line)
new_line[0].contains(ppp)
print(new_line, ppp)

print (linemerge(new_line.union(intersect_point)))
print(closest_line)
closest_line.append(intersect_point)

intersect_point in line
print(line)
isit = Point(14.3558151670632, 50.0571842880476)
isit in line

point.xy[0]

for i in range(len(line)):
    for j in range(len(line[i])):
        if line[i][j] == intersect_point:
            print('simsalabim')

len(split(line, intersect_point))
len(line)

print(intersect_point)

for i in range(len(closest_line))




points = [Point(x[i], y[i]) for i in range(len(closest_line[5].xy[0]))]
x, y = closest_line[5].xy
points = [Point(x[i], y[i]) for i in range(len(x))]
print(points[1])

for i, point in enumerate(points):
    print(point.distance(intersect_point), point)
print(intersect_point)

print(closest_line[5].intersection(intersect_point))






# snapping line to line
# https://gis.stackexchange.com/questions/203058/why-is-shapelys-snapping-geo-snaps-not-working-as-expected

# https://gis.stackexchange.com/questions/203048/split-lines-at-points-using-shapely

from shapely.geometry import Point,LineString    
def split_d(line_string, point):
    coords = line_string.coords
    j = None    
    for i in range(len(coords) - 1):
        if LineString(coords[i:i + 2]).intersects(point):
           j = i
           break    
    assert j is not None    
    # Make sure to always include the point in the first group
    if Point(coords[j + 1:j + 2]).equals(point):
        return coords[:j + 2], coords[j + 1:]
    else:
        return coords[:j + 1], coords[j:]

line = LineString([(1,2),(2,4),(4,5)])
point = Point(2,4)

linda = new_line[0]

line1,line2 = split_d(linda,intersect_point)
line1 = LineString(line1)
line2 = LineString(line2)
print (line1, line2)
LINESTRING (1 2, 2 4) LINESTRING (2 4, 4 5)


line = closest_line[5]
point = intersect_point
coords = [line.coords[0], line.coords[-1]] 
# Add the coords from the points
coords += point.coords
# Calculate the distance along the line for each point
dists = [line.project(Point(p)) for p in coords]
# sort the coordinates
coords = [p for (d, p) in sorted(zip(dists, coords))]
lines = [LineString([coords[i], coords[i+1]]) for i in range(len(coords)-1)]
for lin in lines:
   print(lin)

closest_line[4] = closest_line[5]

closest_line[0].xy

new_mls = MultiLineString([x for i,x in enumerate(closest_line) if i!=3])
new_mls = MultiLineString([linemerge(closest_line[0:i]), closest_line[i]])
MultiLineString([linemerge(closest_line[0:i]), closest_line[i]])

MultiLineString([linemerge(closest_line[0:i]), closest_line[i]]) == closest_line[0:i+1]

print(MultiLineString([linemerge(closest_line[0:i]), closest_line[i]]))

def add_point_to_linestring(linestring, closest_point=0):
    lx, ly = linestring.xy
    lines_list = []
    distance = 100000
    for i in range(len(lx)-1):
        simple_line = LineString([Point(lx[i], ly[i]), Point(lx[i+1], ly[i+1])])
        lines_list.append(simple_line)
        if simple_line.distance(closest_point) < distance:
            distance = simple_line.distance(closest_point)
            print(distance)
            closest_line_index = i
    extend_line = lines_list.pop(closest_line_index)
    xe, ye = extend_line.xy
    lines_list.insert(closest_line_index, LineString([Point(xe[0], ye[0]),
                                                 closest_point,
                                                 Point(xe[1], ye[1])]))
    return linemerge(lines_list)

def split_MultiLineString_to_LineStrings(multilinestring_df,
                                         id_col='id',
                                         mls_col='mls'):
    """
    """
    id_col_list = []
    mls_col_list = []
    for i in range(len(multilinestring_df)):
        for j in range(len(multilinestring_df.loc[i, mls_col])):
            #mls_df = mls_df.append({id_col: multilinestring_df.loc[i, id_col], 
            #           mls_col: multilinestring_df.loc[i, mls_col][j]},
            #            ignore_index=True)
            #mls_dict.setdefault(multilinestring_df.loc[i, id_col], []).append(
            #        multilinestring_df.loc[i, mls_col][j])
            id_col_list.append(multilinestring_df.loc[i, id_col])
            mls_col_list.append(multilinestring_df.loc[i, mls_col][j])            
    mls_df = pd.DataFrame(
            {id_col: id_col_list,
             'individual_linestring': mls_col_list})    
#    dict_to_df = pd.DataFrame.from_dict(mls_dict, orient='index')
#    dict_to_df = dict_to_df.reset_index()
#    dict_to_df.columns = [id_col, 'split_linestring']
    return mls_df

# initialize default values
prag_streets['updated_street'] = prag_streets['street_geometry']
prag_points['shortest_path'] = '' # will be linestring geometry
prag_points['closest_street_id'] = '' # will be identifier to original street
prag_points['street_distance'] = 10000
prag_points['intersect_point'] = prag_points['point_geometry']
# calculate values in a loop (naive solution)

prag_lines = split_MultiLineString_to_LineStrings(prag_streets,
                                                  id_col='kod',
                                                  mls_col='updated_street')
prag_streets_lines = pd.merge(prag_streets, prag_lines, how='inner', on='kod')

def connect_nodes_to_closest_edges(edges_df, nodes_df,
                                   edges_geom='individual_linestring',
                                   nodes_geom='point_geometry'):
    """fdas
    """
    for i in range(len(prag_points)):
        point = prag_points.loc[i,nodes_geom]
        shortest_distance = 100000
        closest_street_index = None
        original_street_id = None
        for j in range(len(edges_df)):
            line = edges_df.loc[j,edges_geom]
            if line.distance(point) < shortest_distance:
                shortest_distance = line.distance(point)
                print(shortest_distance)
                closest_street_index = j
                original_street_id = edges_df.loc[j,'kod']
                intersect_point = line.interpolate(line.project(point))
                closest_line = line
        # write results - both to points and to streets
        # new street split at the closest point
        new_line = add_point_to_linestring(closest_line, intersect_point)
        print(new_line, '\n',
              closest_line, '\n',
              LineString([point, intersect_point]), '\n',
              original_street_id, '\n',
              shortest_distance, '\n',
              line == split(line, intersect_point))
        edges_df.loc[closest_street_index, edges_geom] = new_line     
        nodes_df.loc[i,'shortest_path'] = LineString([point, intersect_point])
        nodes_df.loc[i,'closest_street_id'] = original_street_id
        nodes_df.loc[i,'street_distance'] = point.distance(intersect_point)
        nodes_df.loc[i,'intersect_point'] = intersect_point
    return(edges_df, nodes_df)

new_dfka = connect_nodes_to_closest_edges(prag_streets_lines, prag_points)
new_dfka[0].head()


# visualizing results
fig = plt.figure()
ax = fig.add_subplot(111)
#for i in range(len(closest_line)):
for i in range(len(new_line)):
    ax.plot(new_line[i].xy[0], new_line[i].xy[1], color='#6699cc', alpha=0.7,
    linewidth=1, solid_capstyle='round', zorder=2)
    ax.scatter(new_line[i].xy[0], new_line[i].xy[1], color='red', marker=8)
ax.plot(point.xy[0],point.xy[1], color='orange', alpha=0.7, marker='o', label='node to street')
ax.plot(intersect_point.xy[0],intersect_point.xy[1], color='green', alpha=0.7, marker='o', label='node to street')
plt.title('Connecting terminal nodes to streets with shortest path')
plt.legend(loc='lower right')
fig
            
new_df = split_MultiLineString_to_LineStrings(multilinestring_df=prag_streets.loc[:,['kod', 'updated_street']],
                                     id_col='kod',
                                     mls_col='updated_street')
len(new_df)
print(new_df.loc[1, 'split_linestring'])

closest_line

ll = add_point_to_linestring(line, intersect_point)
print(intersect_point)
print(ll[0])

print(new_mls, closest_line)
new_mls == closest_line








