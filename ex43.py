"""Basic Object-Oriented Anaysis and Design."""

from sys import exit
from random import randint


class Scene(object):
    def enter(self):
        print 'This scene is not yet configured. Subclass it and implement enter().'
            exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print '\n--------'
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):
    quips = [
        'You died. You kinda suck at this.',
        'Your mom would be proud... if she were smarter.',
        'Such a loser.',
        'I have a small puppy that\'s better at this.'
    ]

    def enter(self):
        print Death.quips[randinit(0, len(self.quips)-1)]
        exit(1)


class CentralCorridor(Scene):
    def enter(self):
        print 'The Gothons of Planet Percal #25 have invaded you ship and destroyed'
        print 'your entire crew. You are the last surviving member and your last'
        print 'mission is to get the neuron destruct bomb from the Weapons Armory,'
        print 'put it in the bridge, and blow the ship up after getting into an '
        print 'escape pod.'
        print '\n'
        print 'You\'re running down the cnetral corridor to the Weapons Armony when'
        print 'a Gothon jumps out, red scaly skin, drak grimy teeth, and evil clown costume'
        print 'Armony and about to pull a weapon to blast you.'

        print 'Which action you would take? shoot! dodge! or tell a joke!'
        action = raw_input('> ')

        if action == 'shoot!':
            print 'Quick on the draw you yank out your blaster and fire it at the Gothon.'
            print 'His clone costume is flowing and moving around his body, which throws'
            print 'off you aim. Your laser hits his costume but misses him entirely. This'
            print 'completely ruins his brand new costume his mother bought him, which'
            print 'makes him fly into a rage and blast you repeatedly in the face until'
            print 'you are dead. Then he eats you.'
            return 'death'
        elif action == 'dodge!':
            print 'Like a world class boxer you dodge, weave, slip and slide right'
            print 'as the Gothon\'s blaster cranks a laser past your head.'
            print 'In the middle of your artful dodge your foot slips and you'
            print 'bang your head on the metal wall and pass out.'
            print 'You wake up shortly after only to die as the Gothon stomps on'
            print 'your head and eats you.'
            return 'death' 


class LaserWeaponArmory(Scene):
    def enter(self):
        print 'You do a dive roll into the Weapon Armony, crouch and scan the room' 
        print 'for more Gothons that might be hiding. It\'s dead quiet, too quiet.'
        print 'You stand up and run to the far side of the room and find the'
        print 'neutron bomb in its container. There\'s a keypad lock on the box'
        print 'and you need the code to get the bomb out. If you get the code'
        print 'wrong 10 times then the lock closes forever and you can\'t'
        print 'get the bomb. The code is 3 digits.'
        code = '{0}{1}{2}'.format(randomint(1, 9), randomint(1, 9), randomint(1, 9))
        guess = raw_input('[keypad]> ')
        guesses = 0

        while guess != code and guesses < 10:
            print 'BZZZZEDDD!'
            guesses += 1
            guess = raw_input('[keypad]> ')

        if guess == code:
            print 'The container clicks open and the seal breaks, letting gas out.'
            print 'You grab the neutron bomb and run as fast as you can to the'
            print 'bridge where you must place it in the right spot.'
            return 'the_bridge'
        else:
            print 'The lock buzzes one last time and then you hear a sickening'
            print 'melting sound as the mechanism is fused together.'
            print 'You decide to sit there, and finally Gothons blow up the'
            print 'ship from from their ship and you die.'
            return 'death'


class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass


class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
