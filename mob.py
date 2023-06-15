from ursina import *

from direct.actor.Actor import Actor
from player import Player

class Mob(Entity):
    def __init__(self):
        super().__init__(#model='anime',
                                  color= color.peach,
                                  origin_y=0.5,
                                  collider='box',
                                  scale=7,
                                  position = (0,10,20),
                                  double_sided=True,
                                  animation_speed=0.2, 
                                  )

    def action(self):
        self.actor = Actor("mobModel.glb")  # change filename to the GLB file
        self.actor.reparent_to(self)
        self.actor.play("moveForward")
