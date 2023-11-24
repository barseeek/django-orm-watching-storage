from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    current_passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    passcard_visits = Visit.objects.filter(passcard__passcode=passcode)
    for visit in passcard_visits:
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': Visit.format_duration(Visit.get_duration(visit)),
                'is_strange': Visit.is_visit_long(visit, minutes=60)
            }
        )
    context = {
        'passcard': current_passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
