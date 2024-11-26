from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home, name='home'),
    path('add_task', views.add_task, name='add_task'),
    path('history', views.history, name='history'),
    path('about', views.aboutus, name='about'),
    path('update/<int:id>', views.upd, name='upd'),
    path('delete/<int:id>', views.dele, name='dele'),
    path('restore/<int:id>', views.restore, name='restore'),
    path('delete_/<int:id>', views.delet, name='delet'),
    path('detail_a/<int:id>', views.details, name='details'),
    path('no_c/<int:id>', views.notc, name='no_t'),
    path('compt/',views.tc,name='tcs'),
    path('Restoreall',views.Restoreall,name='Restoreall'),
    path('re_tc',views.Restoreall_tc,name='re_tc'),
    path('clear',views.clear,name='clear'),
    path('contacts',views.contacts,name='contacts'),
    path('profile',views.profile,name='profile'),
    path('completed_a/<int:id>',views.completed_a, name='comp'),
    path('e_p/<int:id>',views.e_p,name='e_p'),
    path('delete_p/<int:id>',views.delete_p,name='delete_p')
   
]