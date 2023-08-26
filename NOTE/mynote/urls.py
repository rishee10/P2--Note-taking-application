from django.contrib import admin
from django.urls import path
from mynote import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about1.html",views.about1,name="about1"),
    path("index.html",views.index,name='index'),
    
    path('object/<int:item_id>/index1.html', views.index1, name='index1'),
    path('object/<int:item_id>/', views.about, name='about'),
    path('object/<int:item_id>',views.edit,name='edit'),
    path('update/<int:item_id>', views.object_edit, name='object_edit'),
    # lkl
    # path('object/<int:item_id>/object_edit/', views.object_edit, name='object_edit'),
    #  lkh
    path("contact",views.contact,name="contact"),
    
    path('object/<int:item_id>/about1.html', views.stosaved, name='stosaved'),
    
    
    path('object/<int:item_id>/delete/', views.delete_object, name='delete_object'),

    path('object/about1.html', views.seetoabout1, name='seetoabout1'),
    path('object/index.html', views.seetoindex, name='seetoindex'),
]


# http://127.0.0.1:8000/object/%7B%25%20url%20'object_edit'%20item.id%20%7D
