from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from react_render.django.render import render_component

def index(request):
    props = {
        'foo': 'bar',
        'woz': [1,2,3],
    }
    component = render_component('components/app.js', props=props)
    context = { 'component': component }
    return render(request, "index.html", context)
