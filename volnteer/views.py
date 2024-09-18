from django.contrib import messages
from django.shortcuts import render

from login.enums import WhoNeedHelpVolunteer
from .dto import dto_to_backend
from .models import Volunteer


def choose_volunteer_charity(request):
    return render(request, 'volnteerandcharity/volnteercharity.html')


def volunteer(request):
    volnteer_list = Volunteer.objects.filter(type=1). \
        values_list(
        'name',
        'description',
        'company__name',
        'company__mail',
        'company__phone_number',
        'company__website'
    ).all()
    if not volnteer_list.exists():
        messages.error(request, "No volunteer available at the moment.")
    return render(request, 'volnteerandcharity/volnteers.html', {'volnteer_list': volnteer_list})


def charities(request):
    charities_list = Volunteer.objects.filter(type=2). \
        values_list(
        'name',
        'description',
        'company__name',
        'company__mail',
        'company__phone_number',
        'company__website'
    ).all()
    if not charities_list.exists():
        messages.error(request, "No charities available at the moment.")
    return render(request, 'volnteerandcharity/charities.html', {'charities_list': charities_list})


def filter_volunteer(request, who_need_help):
    who_need_help_value = dto_to_backend(who_need_help)
    volnteer_list = Volunteer.objects.filter(who_need_help=who_need_help_value, type=1). \
        values_list(
        'name',
        'description',
        'company__name',
        'company__mail',
        'company__phone_number',
        'company__website'
    ).all()

    return render(request, f'volnteerandcharity/{who_need_help}.html', {'volnteer_list': volnteer_list})


def filter_charities(request, who_need_help):
    who_need_help_value = dto_to_backend(who_need_help)
    charities_list = Volunteer.objects.filter(who_need_help=who_need_help_value, type=2). \
        values_list(
        'name',
        'description',
        'company__name',
        'company__mail',
        'company__phone_number',
        'company__website'
    ).all()
    if not charities_list.exists():
        messages.error(request, "No charities available at the moment.")
    return render(request, f'volnteerandcharity/{who_need_help}.html', {'charities_list': charities_list})
