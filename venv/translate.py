from googletrans import Translator
from tkinter import *


def translate(from_str, to_acr):
    global translated_word
    translator = Translator()
    translated = translator.translate(from_str, to_acr)
    # print(translated)
    # print(translated.pronunciation)
    return translated


def onclick(text, lang):
    global text_label, text_label1
    language_acr = { 'English': 'en', 'Japanese': 'ja', 'French': 'fr', 'Chinese': 'zh-cn', 'Spanish': 'es', 'Hindi': 'hi'}
    translated_word = translate(text, language_acr[lang.get()])
    translation = 'Your translation: '+ str(translated_word.text)
    pronunciation = 'Pronounced as: ' + str(translated_word.pronunciation)
    if 'text_label1' in locals() or 'text_label1' in globals():
        text_label1.destroy()
    text_label1 = Label(window, text=translation, font=('arial', 20, 'bold'))
    text_label1.place(x=30, y=250)
    if 'text_label2' in locals() or 'text_label2' in globals():
        text_label2.destroy()
    if str(translated_word.pronunciation)!='None':
        text_label2 = Label(window, text=pronunciation, font=('arial', 20, 'bold'))
        text_label2.place(x=30, y=280)
    # print(translated_word.text)
    # print(translated_word.pronunciation)

window = Tk()
window.geometry('600x600')
window.title('Text translator')
text_label = Label(window,text='Enter your text here: ', font = ('arial', 20, 'bold'))
text_label.place(x=30, y=53)
text_entry = Entry(window, font = ('arial', 16))
text_entry.place(x=320, y=53, width =250, height = 35)
print(text_entry.get())
# Create a Tkinter variable
tkvar = StringVar(window)

# Dictionary with options
choices = { 'English','Spanish','French','Japanese','Hindi', 'Chinese'}
tkvar.set('English') # set the default option

popupMenu = OptionMenu(window, tkvar, *choices)
choice_label = Label(window, text="Choose a target language: ", font = ('arial', 20, 'bold'))
choice_label.place(x=30, y=100)
popupMenu.place(x=400, y=100, height = 35)

translate_button = Button(window, text = 'Translate', relief = RAISED, font = ('arial', 20, 'bold'), command = lambda : onclick(text_entry.get(), tkvar))
translate_button.place(x=220, y=150 )

window.mainloop()