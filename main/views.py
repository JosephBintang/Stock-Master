from django.shortcuts import render
def show_main(request):
    context = {
        'name': 'Joseph Bintang',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)