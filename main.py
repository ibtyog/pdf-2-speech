import PyPDF2, os
from gtts import gTTS

#file_path = input("Please provide file path:")
file_path = 'sample.pdf'
reader = PyPDF2.PdfReader(file_path)
no_pages = len(reader.pages)
# page = reader.pages[0]
# print(page.extract_text(0))

whole_text = ''
for i in range(0,no_pages):
    whole_text += f'Page {i+1}\n'
    whole_text += f'{reader.pages[i].extract_text(0)}\n'.replace('\n',' ')
print(whole_text)

audio = gTTS(text=whole_text,lang='en',slow=False)
audio.save('audio.mp3')
os.system('start audio.mp3')