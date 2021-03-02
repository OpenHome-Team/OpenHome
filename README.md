# OpenHome
**Microsoft Bob but good**

OpenHome is a plugin-oriented program launcher built off of Panda3D.

## Configuration
### Adding Objects
Add it to the object array
```
objects: [
    {
        "filename": "chaibudai.obj",
        "x":0,
        "y":0,
        "z":0
    }
]
```
### Adding Plugins
Add it to the `config` array, and put it in the plugins folder
```
config: [
    plugins: {
        "physics": true
    }
]
```


