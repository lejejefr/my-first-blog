from django.shortcuts import render,redirect
from .models import Character, Equipement
from .forms import MoveForm
from .queries import move

# Create your views here.
def marais(request):
    chara = Character.objects.filter(lieu__id_equip = 'marais')
    return render(request, 'blog/marais.html', {'characters': chara})

def konoha(request):
    chara = Character.objects.filter(lieu__id_equip = 'konoha')
    return render(request, 'blog/konoha.html', {'characters': chara})

def zone(request):
    chara = Character.objects.filter(lieu__id_equip = 'zone51')
    return render(request, 'blog/zone51.html', {'characters': chara})

def equipement(request):
    equip = Equipement.objects.filter()
    return render(request, 'blog/worldMap.html', {'equipements' : equip})

def chasse(request):
    chara = Character.objects.filter(lieu__id_equip = 'chasse')
    return render(request, 'blog/chasse.html', {'characters' : chara})

def psy(request):
    chara = Character.objects.filter(lieu__id_equip = 'psy')
    return render(request, 'blog/psy.html', {'characters' : chara})

def bataille(request):
    chara = Character.objects.filter(lieu__id_equip = 'champ_de_bataille')
    return render(request, 'blog/champ_de_bataille.html', {'characters' : chara})

def formulaire(request,id_character):
    form = MoveForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        msg = move(id_character,data['lieu'])
        if(msg == ""):
            return redirect('formulaire',id_character=id_character)
        else :
            return render(request, "blog/formulaire.html", {"form": form, 'message': msg})
    else:
        form = MoveForm()
        return render(request, "blog/formulaire.html", {"form": form,'message': ''})