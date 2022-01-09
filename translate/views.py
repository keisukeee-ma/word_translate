from django.http import HttpResponse
from django.shortcuts import render
from translate.forms import KakikomiForm
from googletrans import Translator

def kakikomi(request):
    f = KakikomiForm()
    if request.method == 'POST':
        word = request.POST['word']
    else:
        word = ''
    words = translate_word(word)
    return render(
        request,'kakikomiform.html',{'form': f, 'words': words} )


def translate_word(word):
    if word == '':
        return {'ja': '', 'en': '', 'es': '', 'pt': '', 'de': ''}
    else:
        translator = Translator()
        translated_1 = translator.translate(word, src= "ja", dest="en")
        translated_2 = translator.translate(word, src= "ja", dest="es")
        translated_3 = translator.translate(word, src= "ja", dest="pt")
        translated_4 = translator.translate(word, src= "ja", dest="de")
        translated_5 = translator.translate(word, src= "ja", dest="fr")
        return {'ja': word, 'en': translated_1.text, 'es': translated_2.text, 'pt': translated_3.text, 'de': translated_4.text, 'fr': translated_5.text}