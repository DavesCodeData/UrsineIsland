from ursina import *


class Enemy(Entity):
    def __init__(self):
        super().__init__(model='cube',
                                  origin_y=0.5,
                                  collider='mesh',
                                  scale=9, 
                                  double_sided=True,
                                  position = (0,15,20),
                                  color = color.peach
        )


