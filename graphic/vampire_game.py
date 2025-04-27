import pyganim
images = pyganim.getImagesFromSpriteSheet(rows=1, cols=3)
frames = list(zip(images, [200, 200, 600]))
animObj = pyganim.PygAnimation(frames)
animObj.play()

