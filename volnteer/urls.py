from django.urls import path
from .views import choose_volunteer_charity, volunteer, \
    filter_volunteer, charities, filter_charities

urlpatterns = [
    path('volnteer_charity/', choose_volunteer_charity, name='volnteer_charity'),
    path('volnteers/', volunteer, name='volnteers'),
    path('volnteers/<str:who_need_help>', filter_volunteer, name='vol_child'),
    path('charities/', charities, name='charities'),
    path('charities/<str:who_need_help>', filter_charities, name='char_child')
]
