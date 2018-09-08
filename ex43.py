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
        print("You do a dive roll into the Weapon Armony, crouch and scan the room")
        print("for more Gothons that might be hiding. It's dead quiet, too quiet.")


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
