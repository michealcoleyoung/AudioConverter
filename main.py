from pydub import AudioSegment
from appJar import gui
import ntpath


def convert(btn):
    audio_file = app.getEntry("audio_file")    # Selects audio from filepath
    song = AudioSegment.from_file(audio_file)  # Identifies what file type (WAV or MP3 etc.)
    file_name = ntpath.basename(audio_file)    # Gets basename from file path (a/b/c/basename)

    song.export(f'/Users/michealcoleyoung/Downloads/{file_name.replace(".wav", "")}.mp3', format="mp3")
    # Convert file to MP3 and save to the downloads directory

    app.infoBox("message", "Song was successfully converted!")


app = gui('WAV-P3', useTtk=True)
app.setTtkTheme('clam')

app.addFileEntry("audio_file")  # select audio file
app.addButton("CONVERT", convert)

app.go()