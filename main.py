from pydub import AudioSegment
from appJar import gui
import os

# TODO: Make sure that a message box appears to confirm successful conversion


def convert(btn):
    audio_file = app.getEntry("audio_file")  #  Selects audio from filepath
    song = AudioSegment.from_file(audio_file) #  Identifies what file type (WAV or MP3)

    if app.getRadioButton("choice") == "MP3":
        #  Convert file to MP3 and save to the downloads directory

    else:
        #  Convert file to WAV and save to the downloads directory


app = gui('Audio Converter', useTtk=True)
app.setTtkTheme('clam')

app.addFileEntry("audio_file")  #  select audio file

#  audio formats to choose from are WAV and MP3
app.addRadioButton("choice", "MP3")
app.addRadioButton("choice", "WAV")

app.addButton("CONVERT", convert)

app.go()