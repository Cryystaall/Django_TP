from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Participation
from .forms import ParticipationForm
from django.contrib.auth.decorators import login_required


@login_required
def event_list(request):
    events = Event.objects.all()
    
    # Ajoute le nombre de participants confirmés pour chaque événement
    for event in events:
        event.confirmed_participants = event.participation_set.filter(is_coming=True).count()

    return render(request, 'events/event_list.html', {'events': events})


@login_required
def event_detail(request, id_event):
    event = get_object_or_404(Event, id=id_event)
    
    # Lorsque l'utilisateur soumet le formulaire pour participer
    if request.method == "POST":
        # Vérifie si l'utilisateur est déjà inscrit
        if not Participation.objects.filter(event=event, user=request.user).exists():
            Participation.objects.create(event=event, user=request.user, is_coming=True)
    
    # Récupère la participation de l'utilisateur
    user_is_coming = Participation.objects.filter(event=event, user=request.user).exists()

    return render(request, 'events/event_detail.html', {
        'event': event,
        'user_is_coming': user_is_coming
    })