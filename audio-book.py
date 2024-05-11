# pip install PyPDF2 && pip install pyttsx3 #
import PyPDF2, pyttsx3

# Open the ebook #
path = open('The_art_of_war.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(path)

speak = pyttsx3.init()

# Scroll through the pages of the ebook, extract the text and read it #
for pages in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[pages].extract_text()
    speak.say(text)
    speak.runAndWait()
speak.stop()
