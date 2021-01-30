from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from .models import FilesAdmin
from .forms import Sentiment_Typed_Tweet_analyse_form
from .sentiment_analysis_code import sentiment_analysis_code

# Create your views here.
def home(request):
	context={'file':FilesAdmin.objects.all()}
	return render(request,'layouts/base-fullscreen.html',context)

def dashboard(request):
	context={'file':FilesAdmin.objects.all()}
	return render(request,'dashboard.html',context)

def icon(request):
	context={'file':FilesAdmin.objects.all()}
	return render(request,'icons.html',context)

def map(request):
	context={'file':FilesAdmin.objects.all()}
	return render(request,'maps.html',context)

def prof(request):
	context={'file':FilesAdmin.objects.all()}
	return render(request,'profile.html',context)

def prediction(request):
	context={'file':FilesAdmin.objects.all()}
	return render(request,'prediction.html',context)

def predictionresult(request):
	context={'file':FilesAdmin.objects.all()}
	return render(request,'predictionresult.html',context)

def corpus(request):
	context={'file':FilesAdmin.objects.all()}
	return render(request,'corpus.html',context)

def sentiment_analysis_type(request):
    if request.method == 'POST':
        form = Sentiment_Typed_Tweet_analyse_form(request.POST)
        analyse = sentiment_analysis_code()
        if form.is_valid():
            tweet = form.cleaned_data['sentiment_typed_tweet']
            sentiment = analyse.get_tweet_sentiment(tweet)
            args = {'tweet':tweet, 'sentiment':sentiment}
            return render(request, 'predictionresult.html', args)

    else:
        form = Sentiment_Typed_Tweet_analyse_form()
        return render(request, 'prediction.html')


def download(request,path):
	file_path=os.path.join(settings.MEDIA_ROOT,path)
	if os.path.exists(file_path):
		with open(file_path,'rb')as fh:
			response=HttpResponse(fh.read(),content_type="application/adminupload")
			response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
			return response
	raise Http4040

