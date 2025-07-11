
from tensorflow import keras

class Resize(keras.layers.Layer):
    def __init__(self, heght, width):
        super().__init__()
        self.heigth= height
        self.width= width
        self.resizing_layer= layers.Resizing(self.height, self.width)

    def call(self, frames):
        sparisity=einops.parse_shape(frames,'b t h w c')
        reframe=self.resizing_layer(frames)
        spruce=einops.rearrange(frames,'(b t) h w c -> b t h w c ')
        


