from pydub import AudioSegment
from appJar import gui
import re

def convert(btn):
    audio_file = app.getEntry("audio_file")
    song = AudioSegment.from_wav(audio_file)

    if app.getRadioButton("choice") == "MP3":
        song.export("test.mp3", format="mp3")
    else:
        song.export("text.wav", format="wav")


app = gui('Audio Converter', useTtk=True)
app.setTtkTheme('clam')

app.addFileEntry("audio_file")  #  select audio file

#  audio formats to choose from are WAV and MP3
app.addRadioButton("choice", "MP3")
app.addRadioButton("choice", "WAV")

app.addButton("CONVERT", convert)

app.go()