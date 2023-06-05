# I have created this file-Pashupati
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return  HttpResponse("Home")

def english(request):
    return render(request,'english.html')

def nepali(request):
    return render(request,'nepali.html')


def ex1(request):
    sites = ['''<h1>For Entertainment </h1><a href="https://www.youtube.com">youtube video</a>''',
             '''<h1>For Interaction</h1><a href="https://www.facebook.com">Facebook</a>''',
             '''<h1>For Insight</h1><a href="https://www.ted.com/talks">Ted talks</a>''',
             ]
    return HttpResponse((sites))


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # check which checkbox is on
    if removepunc == "on":
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed New lines', 'analyzed_text': analyzed}
        djtext = analyzed
    # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed spaces', 'analyzed_text': analyzed}

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)


'''
def capfirst(request):
  return HttpResponse("capitalize first")

def newlineremove(request):
  return HttpResponse("newline remove first")

def spaceremove(request):
  return HttpResponse("space remover <a href='/'>back</a>")

def charcount(request):
  return HttpResponse("charcount")
'''