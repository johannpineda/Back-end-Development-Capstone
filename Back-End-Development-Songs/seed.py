from backend.db import collection
songs=[
 {'title':'Midnight Drive','artist':'The Example Band','album':'Road Lights','year':2024,'lyrics':'We ride beneath the city lights'},
 {'title':'Open Sky','artist':'The Example Band','album':'Road Lights','year':2024,'lyrics':'Under an open sky we sing'},
 {'title':'Home Again','artist':'The Example Band','album':'Afterglow','year':2025,'lyrics':'Every road leads home again'}]
c=collection(); c.delete_many({}); c.insert_many(songs); print('Seeded',c.count_documents({}),'songs')
