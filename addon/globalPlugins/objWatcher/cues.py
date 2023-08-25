import os
from nvwave import playWaveFile

def Start():
	play_sound("Start")

def Stop():
	play_sound("Stop")

def NoObj():
	play_sound("NoObj")

def play_sound(filename):
	path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'sounds', filename))
	return playWaveFile(path + ".wav")
