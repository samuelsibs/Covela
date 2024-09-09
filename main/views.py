from django.shortcuts import render

def show_main(request):
    context = {
        'app_names' : 'Covela',
        'name': 'Samuel Sebastian Sibarani',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
