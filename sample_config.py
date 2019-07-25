# ** SAMPLE CONFIG FILE FOR DEMONSTRATION PURPOSES **
# Config file to hold variables I don't want to put in the main file.
# Also for later, so that I can put potentially sensitive info here
# and not push it to GitHub accidentally. 

adm1 = 'input/gadm36_USA_49.json'

#epsg = 32662 #Kenya
epsg = 5070 #USA

seed_location = 'lowerleft'
round_to = 10
num_shape_divisor = 6

symbology_column = 'County' #Kenya

vertices_col = 'vertices'
geom_col = 'geometry'

tile_id = 'tile_id'
admin_id = 'CID'