from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    storage_visitors = Visit.objects.filter(
        passcard__is_active=True,
        leaved_at=None
    )
    for visitor in storage_visitors:
        visit_duration = Visit.get_duration(visitor)
        non_closed_visits.append(
            {
                'who_entered': visitor.passcard.owner_name,
                'entered_at': visitor.entered_at,
                'duration': Visit.format_duration(visit_duration),
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
