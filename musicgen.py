#!/usr/bin/python
from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note
import pdb

import pygame

def getSingleObj(fx, fy, gx, gy):
    """ Get 2 note objects and keep writing them. """
    a = Note(int(fx/60), int(fy/48))
    b = Note(int(gx/60), int(fy/48))
    return a, b

# TODO: Add function to generate note str from number moduloed.
def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    clock = pygame.time.Clock()
    pygame.init()
    try:
        pygame.mixer.music.load(music_file)
        print "Music file %s loaded!" % music_file
    except pygame.error:
        print "File %s not found! (%s)" % (music_file, pygame.get_error())
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

def proc(centroid_list):
    num_notes = len(centroid_list)/4
    notes = []
    for i in range(num_notes):
        a, b = getSingleObj(centroid_list[i], centroid_list[i+1],\
                centroid_list[i+2], centroid_list[i+3])
        notes.append(a)
        notes.append(b)
    pdb.set_trace()
    sequence = NoteSeq(notes)
    midi = Midi(i, tempo=90, instrument=0)
    midi.seq_notes(sequence, track=0)
    midi.write("temp.mid")
    play_music("temp.mid")

        

def main():
    note = "D4 E#10 F#8 Gg4 A Bb4 "
    notes = ""
    for i in xrange(10):
        notes += note
    notes1 = NoteSeq(notes)
    midi = Midi(1, tempo=90, instrument=0)
    midi.seq_notes(notes1, track=0)
    midi.write("demo.mid")
    play_music("demo.mid")

if __name__ == '__main__':
    play_music("temp.mid")
    main()
