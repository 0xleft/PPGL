```
pip install git+https://github.com/0xleft/PPGL.git
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