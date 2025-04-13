from django.shortcuts import render
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.corpus import wordnet

def index(request):
    return render(request, 'index.html')

def search(request):
    word = request.GET.get('word')
    meanings = []
    synonyms = set()
    antonyms = set()

    if word:
        for syn in wordnet.synsets(word):
            meanings.append(syn.definition())

            for lemma in syn.lemmas():
                synonyms.add(lemma.name())
                if lemma.antonyms():
                    antonyms.add(lemma.antonyms()[0].name())

    context = {
        'word': word,
        'meanings': meanings,
        'synonyms': list(synonyms),
        'antonyms': list(antonyms),
    }

    return render(request, 'word.html', context)
