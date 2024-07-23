from django.shortcuts import render


def home_view(request):

    print(request.META)

    return render(request, 'a_posts/home.html')
