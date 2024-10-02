from flask import Flask
from pydub import AudioSegment
from pydub.playback import play

app = Flask(__name__)

@app.route('/ring')
def hello():

    sound = AudioSegment.from_mp3("Westminster-doorbell-chime-sound.mp3")
    play(sound)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)