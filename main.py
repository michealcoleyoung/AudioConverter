from pydub import AudioSegment
from appJar import gui

def convert(btn):
    if app.getRadioButton("choice") == "MP3":
        print("MP3")
    else:
        print("WAV")

# set
app = gui('Audio Converter', useTtk=True)
app.setTtkTheme('clam')

app.addFileEntry("audio_file")  #  select audio file

app.addRadioButton("choice", "MP3")
app.addRadioButton("choice", "WAV")

app.addButton("CONVERT", convert)

app.go()