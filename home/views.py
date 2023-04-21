from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import AudioForm
from .models import Audio

# Create your views here.

def index(request):
    # Page from the theme 
    return render(request, 'pages/index.html')

def audio_upload(request):
    return render(request, 'pages/audio_upload.html')

@csrf_exempt
def upload_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            audio = form.save()
            return JsonResponse({'success': True, 'audio_id': audio.id})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        return redirect('home')
