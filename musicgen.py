#!/usr/bin/python
from pyknon.genmidi import Midi
from pyknon.music import NoteSeq

import pygame
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

notes1 = NoteSeq("D4 F#8 A Bb4")
midi = Midi(1, tempo=90)
midi.seq_notes(notes1, track=0)
midi.write("demo.mid")
play_music("demo.mid")
