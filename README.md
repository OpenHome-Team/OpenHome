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
        "physics"
    }
]
```
## Using
1. Run `git clone https://github.com/zurgeg/p3d-simpleengine` to get `simpleengine`
2. Copy the `levels/level.json` and the `levels/scripts` folder to the `p3d-simpleengine` folder
3. Type `cd p3d-simpleengine` and run `python(3) core.py`
4. Enjoy!

