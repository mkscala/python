 # coding: utf-8
# !/usr/bin/env python3
'''class — Tell Python to make a new kind of thing.
• object — Two meanings: the most basic kind of thing, and any instance of some thing.
• instance — What you get when you tell Python to create a class.
• def — How you define a function inside a class.
• self — Inside the functions in a class, self is a variable for the instance/object being accessed.
• inheritance — The concept that one class can inherit traits from another class, much like
you and your parents.
• composition — The concept that a class can be composed of other classes as parts, much
like how a car has wheels.
• attribute — A property classes have that are from composition and are usually variables.
• is- a — A phrase to say that something inherits from another, as in a “salmon” is- a “fish.”
• has- a — A phrase to say that something is composed of other things or has a trait, as in “a
salmon has- a mouth.
'''
 
#  MODULES, CLASSES, AND OBJECTS  p. 142     'learn python the hard way'
class Song(object):
    def __init__(self, lyrics):
	  self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

'''
 
Why do I need self when I make __init__ or other functions for classes?

If you don’t have self, then code like cheese = 'Frank' is ambiguous. That code isn’t clear
about whether you mean the instance’s cheese attribute or a local variable named cheese. With
self.cheese = 'Frank' it’s very clear you mean the instance attribute self.cheese.
'''

# Learning to Speak Object Oriented  p. 144     'learn python the hard way'