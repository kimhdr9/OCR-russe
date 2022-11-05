from googletrans import Translator

traduction = Translator()
text='Что вы помните?'

detection_langue = traduction.detect(text)
print(detection_langue)

out = traduction.translate(text,dest="en")

print(out.text)