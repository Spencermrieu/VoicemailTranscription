import speech_recognition as sr


filename = "input.wav"


# initialize the recognizer
r = sr.Recognizer()


# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)




# write data in a file.
file1 = open("Voicemail Transcrption.txt","w")

file1.write(text)

file1.close() #to change file access modes
