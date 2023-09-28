from django.urls import path
from . import views
app_name = 'FoodApp'
urlpatterns = [
    path('', views.home, name ='home'),
    path('<int:recipe_id>/', views.detail, name='detail'),
    # Add Recipe
    path('Add_Recipe', views.Add_Recipe,name='Add_Recipe'),
    # update
    path('update/<int:id>/',views.update_Recipe,name='update_Recipe'),
    # Delete Recipe
    path('Delete_Recipe/<int:id>', views.Delete_Recipe,name='Delete_Recipe')
]