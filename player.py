from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.actor.Actor import Actor

class Player(FirstPersonController):
    def __init__(self):
        print('firstpersoncroller got called -=====================================')
        super().__init__(position = (0,3,0),
                        speed=30,
                        origin=(0,0,-2),
                        scale=(7),
                        collider='box',
                        health=100,
                                    )
        print('firstpersoncroller got called -=====================================')
        self.ghostPerson = Entity(parent=self, position = (0,0,2), rotation_y = 180)


    def doubleSpeed(self):
        self.original_speed = self.speed
        self.speed *= 2



