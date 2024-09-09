from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245503',
        'name': 'Samuel Sebastian Sibarani',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
