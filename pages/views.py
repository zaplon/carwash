from django.shortcuts import render, render_to_response


def homeView(request):
    return render_to_response('home.html', {})
