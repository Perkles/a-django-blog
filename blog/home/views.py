from django.shortcuts import render


def home_page_rendering(request):
    if request.method == 'GET':
        home = ''
        return render(request, 'home.html', {'home': home})
