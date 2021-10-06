import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS



def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=True)
    myobj.save(filename)
        


def mergAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    # kripya dhyan dijiye
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 0000
    finish = 4600
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format = "mp3")
    # train number and train name



    #thodi hi der me platform number
    start = 9800
    finish = 12000
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format = "mp3")
    # platform number

    # par aa rahi hai
    start = 12400
    finish = 19000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format = "mp3")



def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # train_number + train_name
        textToSpeech(item['train_number'] + "" + item['train_name'], '2_hindi.mp3')
        # platform number
        textToSpeech(item['platform_number'], '4_hindi.mp3')
        audios = [f"{i}_hindi.mp3" for i in range(1,6)]

        announcement = mergAudios(audios)
        announcement.export(f"announcement_{item['train_number']}_{index+1}.mp3", format = "mp3")


if __name__ == '__main__':
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("Book1.xlsx")