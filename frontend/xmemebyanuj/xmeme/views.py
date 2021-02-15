from django.shortcuts import render, get_object_or_404
import requests

def index(request):
    response = requests.get('https://apixmeme.herokuapp.com/memes/')
    memedata = response.json()
    context = {
        'memedata' : memedata
    }
    return render(request, 'xmeme/index.html', context)

    
def postmeme(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        caption = request.POST.get('caption')
        memeurl = request.POST.get('memeurl')
        url = 'https://apixmeme.herokuapp.com/memes/'
        body = {"name" : name, "caption" : caption, "url" : memeurl}
        response = requests.post(url, headers={'Content-Type': 'application/json'}, json=body)
        if response.status_code == 200:
            print("Code 200")
        else:
            print("Code not 200")
        return render(request, 'xmeme/thanks.html')
    return render(request, 'xmeme/post.html')
