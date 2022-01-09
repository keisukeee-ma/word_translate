from googletrans import Translator

def translate_word(request):
    translator = Translator()
    word_j = input()
    translated = translator.translate(word_j, src= "ja", dest="de") #ドイツ語
    return {'ja': word_j, 'de': translated.text}