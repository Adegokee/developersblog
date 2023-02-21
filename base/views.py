from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
rooms = [
    {'id': 1, 'name': 'Let learn python'},
    {'id': 2, 'name': 'Let learn JavaScript'},
    {'id': 3, 'name': 'Let learn Django'},
    {'id': 4, 'name': 'Let learn Web-development'},
]

def home(request):
    context={'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room=None
    for i in rooms:
        if i['id'] == int(pk):
            room=i
    context={'room': room}
    return render(request, 'base/room.html', context)