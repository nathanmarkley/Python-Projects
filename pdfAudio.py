import pyttsx3,PyPDF2

#Ask user for PDF file that they want to convet to speech
pdffile = input('\nPut file path to PDF here!! File Path: ')

#Open PDF file and extract text and clean up text 
pdfreader = PyPDF2.PdfFileReader(open(pdffile, 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extract_text()
    cleanText = text.strip().replace('\n', ' ')
    print(cleanText)

#Save text to audio mp3 file
speaker.save_to_file(cleanText, 'audio.mp3')
speaker.runAndWait()

speaker.stop()