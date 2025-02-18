from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm
from .models import Film, Kniha, Hra  # Přidej modely, které používáš
from .forms import FeedbackForm  # Přidej import pro FeedbackForm




class ContactView(View):
    def get(self, request):
        # Zobrazení formuláře pro kontaktování
        form = ContactForm()
        return render(request, 'menu/ukol5.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            # Zpracování formuláře a výpis do konzole
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            print(f"Received message from {name}: {message}")

            # Přesměrování na výchozí stránku (např. na home)
            return redirect('home')  # Pokud chceš přesměrovat na domovskou stránku
        return render(request, 'menu/ukol5.html', {'form': form})


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

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            print(f"Received feedback from {name}: {message}")
            return render(request, 'menu/ukol3.html', {'name': name, 'success': True})
    else:
        form = FeedbackForm()

    return render(request, 'menu/ukol3.html', {'form': form, 'success': False})

def ukol3(request):
    return render(request, 'menu/ukol3.html')

def ukol4(request):
    return render(request, 'menu/ukol4.html')

def ukol5(request):
    return render(request, 'menu/ukol5.html')

def vysledky(request):
    return render(request, 'menu/vysledky.html')
