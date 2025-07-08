# Auto-Resize All Images in a Folder
from PIL import Image  
import os
[Image.open(f).resize((800,600)).save(f"resized_{f}") for f in os.listdir() if f.endswith(".png")]

# 