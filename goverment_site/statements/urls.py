from .views import StatementListView, StatementDetailView, StatementCreateView,\
                   StatementUpdateView, StatementDeleteView
from django.urls import path

app_name = 'statements'

urlpatterns = [
    path('', StatementListView.as_view(), name='list'),
    path('<int:pk>/', StatementDetailView.as_view(), name='detail'),
    path('create/', StatementCreateView.as_view(), name='create'),
    path('update/<int:pk>/', StatementUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', StatementDeleteView.as_view(), name='delete'),
]