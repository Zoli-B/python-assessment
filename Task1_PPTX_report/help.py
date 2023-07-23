import control
from pptx import Presentation

prs1 = Presentation()

for i, layout in enumerate(control.prs.slide_layouts):
    print(f"Index: {i}")
    print(f"Name: {layout.name}")
    print("--------------------")