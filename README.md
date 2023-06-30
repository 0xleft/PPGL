# Intro

This is just a library so when I'm working on some projects I don't need to make everything from scratch. I'll be hopefully improving it as I go on.

## Install
```
pip install ppgl
```

It just works :)

## Example:

```python
from ppgl.ppgl import GUI

gui = GUI(1000,1000)
gui.add_text("Hello world!", 0,0).pack()
gui.add_button("Exit", gui.root.destroy(),0,0,0,0).pack()
gui.start()
```
