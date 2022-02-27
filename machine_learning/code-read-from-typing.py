__version__ = '0.1.0'

# โค้ดอ่านออกเสียงจากที่พิมพ์
from playsound import playsound
from gtts import gTTS

tts = gTTS(text="ป้าๆๆ คนสวย", lang="th")
tts.save("helloWorld.mp3")
playsound("helloWorld.mp3", True)
