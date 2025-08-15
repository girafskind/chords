#!/usr/bin/env python3

notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

def circle_of_fifths():
  i = 0
  for x in range(12):
    print(notes[i%12])
    i += 7

def major(note):
  x = notes.index(note.upper())
  print(notes[(x)]+"-"+notes[(x+4)%12]+"-"+notes[(x+7)%12])

def minor(note):
  x = notes.index(note.upper())
  print(notes[(x)]+"-"+notes[(x+3)%12]+"-"+notes[(x+7)%12])

def aug(note):
  x = notes.index(note.upper())
  print(notes[(x)]+"-"+notes[(x+4)%12]+"-"+notes[(x+8)%12])

def dim(note):
  x = notes.index(note.upper())
  print(notes[(x)]+"-"+notes[(x+3)%12]+"-"+notes[(x+6)%12])

def seventh(note):
  x = notes.index(note.upper())
  print(notes[(x)]+"-"+notes[(x+4)%12]+"-"+notes[(x+7)%12]+"-"+notes[(x+10)%12])

def majseventh(note):
  x = notes.index(note.upper())
  print(notes[(x)]+"-"+notes[(x+4)%12]+"-"+notes[(x+7)%12]+"-"+notes[(x+11)%12])

def majorpentatonic(note):
  x = notes.index(note.upper())
  print(notes[x]+"-"+notes[(x+2)%12]+"-"+notes[(x+4)%12]+"-"+notes[(x+7)%12]+"-"+notes[(x+9)%12])

def minorpentatonic(note):
  x = notes.index(note.upper())
  print(notes[x]+"-"+notes[(x+3)%12]+"-"+notes[(x+5)%12]+"-"+notes[(x+7)%12]+"-"+notes[(x+10)%12])

