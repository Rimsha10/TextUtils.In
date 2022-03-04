from django.http import HttpResponse
from django.shortcuts import render
import string
#create templates py dir where manage.py is stored


def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    print(djtext)
    removepunc = request.POST.get('removepunc', 'off')
    removespace = request.POST.get('removespace', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    charcount = request.POST.get('charcount', 'off')
    newlineremove= request.POST.get('newlineremove', 'off')
    print(removepunc)
    purposelist=[]
    st=''
    if removepunc=="on":
      textstring=''
      for i in djtext:
        if i not in string.punctuation:
            textstring+=i
      a_text={"purpose":"Punctuations Removed","Analyzed_Text":textstring}
      djtext=textstring
      purposelist.append(a_text["purpose"])

    if removespace=="on":
        textstring=''
        djtext = djtext.split(" ")
        for i in djtext:
            textstring+=i
        a_text = {"purpose": "Spaces Removed", "Analyzed_Text": textstring}
        djtext = textstring
        purposelist.append(a_text["purpose"])

    if uppercase=="on":
        textstring=''
        for i in djtext:
          textstring+=i.upper()
        a_text = {"purpose": "UPPER CASE", "Analyzed_Text": textstring}
        djtext = textstring
        purposelist.append(a_text["purpose"])

    if charcount=="on":
        count=0
        textstring = ''
        djtext = djtext.split(" ")
        for i in djtext:
            for j in i:
                count+=1
        a_text = {"purpose": "Characters Counted", "Analyzed_Text": count}
        djtext = textstring
        purposelist.append(a_text["purpose"])

    if newlineremove=="on":
        if newlineremove == "on":
            djtext = djtext.replace('\r\n', '').replace('\n', '')
            textstring = ""
            for char in djtext:
                if char != "\n":
                    textstring = textstring + char
        a_text = {"purpose": "NewLines Removed", "Analyzed_Text": textstring}
        purposelist.append(a_text["purpose"])

    if removespace =="off" and uppercase=="off" and charcount=="off" and newlineremove=="off" and removepunc=="off":
        return HttpResponse("Error")

    if len(purposelist)>1:
      for i in purposelist:
        st=st+'-'+i
      a_text["purpose"]=st

    return render(request, 'analyze.html', a_text)


def about(request):
    file=open("aboutus.txt")
    data=file.read()
    return HttpResponse('<p><pre>'+str(data)+'</pre></p>')


def contactus(request):
    file=open("contact.txt")
    data=file.read()
    return HttpResponse('<p><pre>'+str(data)+'</pre></p>')











