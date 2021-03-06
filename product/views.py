from django.shortcuts import render
from .forms import CommentForm
from django.contrib import messages
from product.models import Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import translation
from django.utils.translation import activate

# Create your views here.

def index(request):
    return HttpResponse('coucou')

def comment(request, id):
    url = request.META.get('HTTP_REFERER') # Le dernier url
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.produit_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(request, 'votre avis compte')
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)

def selectlanguage(request):
    if request.method == "POST":
        cur_language = translation.get_language()
        lasturl = request.META.get("HTTP_REFERER")
        lang = request.POST['language']
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY]=lang
        return HttpResponseRedirect("/"+lang)

       
		
		
			
			
			
            
			
            
            
			
			
			

   

	