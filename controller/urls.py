from django.urls import path
from controller import views

app_name = 'controller'

urlpatterns = [
    path('<int:controller_id>/', views.add_to_database, name='add_to_database'),
    path('detail/<int:controller_id>/', views.view_controller_detail, name='controller_detail'),
]

# urlpatterns = [
#     path('/<int:controller_id>/<float:rv>/<float:rc>/<float:ap>/<float:rp>/', views.add_to_database, name='add_to_database'),
#     path('/<int:controller_id>/<float:rv>/<float:rc>/<float:ap>/<float:rp>/<str:pc>/', views.add_to_database, name='add_to_database_with_phase_connection'),
# ]