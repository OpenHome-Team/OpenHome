import json

def on_init(app):
    config = json.load('homeconfig.json')
    for i in config['objects']:
        obj = app.loader.LoadModel(i['filename'])
        x = i['x']
        y = i['y']
        z = i['z']
        obj.setPos(x,y,z)
        obj.reparentTo(app.render)
        
    
    
        
