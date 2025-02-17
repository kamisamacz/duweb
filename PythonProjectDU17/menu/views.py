from django.shortcuts import render
from .models import Film, Kniha, Hra

def home(request):
    return render(request, 'menu/home.html')

def ukol1(request):
    jmeno = request.GET.get('jmeno', 'neznámý uživatel')
    return render(request, 'menu/ukol1.html', {'jmeno': jmeno})


def ukol2(request):
    kategorie = request.POST.get('kategorie', 'Filmy')  # Hlavní kategorie (Filmy, Knihy, Hry)
    zanr = request.POST.get('zanr', '')  # Podkategorie (Žánr u filmů, knih a her)

    # Filtrujeme podle kategorie
    if kategorie == 'Filmy':
        vsechny_zanry = Film.objects.values_list('zanr', flat=True).distinct()
        data = Film.objects.filter(zanr=zanr).order_by('nazev') if zanr else Film.objects.all().order_by('zanr', 'nazev')

    elif kategorie == 'Knihy':
        vsechny_zanry = Kniha.objects.values_list('zanr', flat=True).distinct()
        data = Kniha.objects.filter(zanr=zanr).order_by('nazev') if zanr else Kniha.objects.all().order_by('zanr', 'nazev')

    elif kategorie == 'Hry':
        vsechny_zanry = Hra.objects.values_list('zanr', flat=True).distinct()
        data = Hra.objects.filter(zanr=zanr).order_by('nazev') if zanr else Hra.objects.all().order_by('zanr', 'nazev')

    else:
        vsechny_zanry = None
        data = []

    return render(request, 'menu/ukol2.html', {
        'kategorie': kategorie,
        'zanr': zanr,
        'data': data,
        'vsechny_zanry': vsechny_zanry
    })



def ukol3(request):
    return render(request, 'menu/ukol3.html')

def ukol4(request):
    return render(request, 'menu/ukol4.html')

def ukol5(request):
    return render(request, 'menu/ukol5.html')

def vysledky(request):
    return render(request, 'menu/vysledky.html')
