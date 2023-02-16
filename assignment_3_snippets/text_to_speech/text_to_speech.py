# sudo apt install python3-pip
# sudo apt install mpg321
# sudo pip3 install gTTS

# Execute above commands to install required packages

from gtts import gTTS
import os

text = "det er helt Texas!"
langauge = "no"
obj = gTTS(text=text, lang=langauge, slow=False)
obj.save("wel.mp3")
os.system("mpg321 wel.mp3")
