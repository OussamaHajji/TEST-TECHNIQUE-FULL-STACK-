from django.urls import path
from . import views
'''
Utilisé pour acheminer les URL vers les fonctions d'affichage appropriées
'''

urlpatterns = [
	# Path Converters
	# int: numbers
	# str: strings
	# path: Tous les URL/
	# slug: hyphen-and_underscores_stuff
	# UUID: universally unique identifier

    path('', views.home, name="home"),
	path('<int:year>/<str:month>/', views.home, name="home"),
	path('add_event', views.add_event, name='add-venue'),
	path('list_venues', views.list_venues, name='list-venues'),
	path('show_venue/<venue_id>', views.show_venue, name='show-venue'),	
	path('update_venue/<venue_id>', views.update_venue, name='update-venue'),
	path('delete_venue/<venue_id>', views.delete_venue, name='delete-venue'),
	path('venue_text', views.venue_text, name='venue_text'),
	
]