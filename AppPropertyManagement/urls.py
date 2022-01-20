from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
	path('',views.home,name='home'),
	path('base/',views.base,name='base'),
	path('UserLogin/',views.UserLogin,name='UserLogin'),
	path('AdminLogin/',views.AdminLogin,name='AdminLogin'),
	path('UserRegister/',views.UserRegister,name='UserRegister'),
    path('AdminRegister/',views.AdminRegister,name='AdminRegister'),
    path('logout/', views.logout, name='logout'),
    path('ViewProperty/',views.ViewProperty,name='ViewProperty'),
    path('FavouriteProperty/',views.FavouriteProperty,name='FavouriteProperty'),
    path('BookAppointment/',views.BookAppointment,name='BookAppointment'),
    path('AddProperty/',views.AddProperty,name='AddProperty'),
    path('AddDigitalProperty/',views.AddDigitalProperty,name='AddDigitalProperty'),
    path('Propertydetails/<id>',views.Propertydetails,name='Propertydetails'),
    path('Appointment/',views.Appointment,name='Appointment'),
    path('ViewCustomer/',views.ViewCustomer,name='ViewCustomer'),
    path('BookedAppointment/',views.BookedAppointment,name='BookedAppointment'),
    path('destroy/<int:id>',views.destroy,name='destroy'),
    path('remove/<int:id>',views.remove,name='remove'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('deleteproperty/<int:id>',views.deleteproperty,name='delete'),
    path('deletedigital/<int:id>',views.deletedigital,name='delete'),
    path('ViewProperties/',views.ViewProperties,name='ViewProperties'),
    path('ViewDigitalProperties/',views.ViewDigitalProperties,name='ViewDigitalProperties'),
    path('updates/<int:id>/',views.updates,name='updates'),
    path('updated/',views.updated,name='updated'),
    path('Advertisement/',views.Advertisement,name='Advertisement'),
    path('AddAdvertisement/',views.AddAdvertisement,name='AddAdvertisement'),
    path('PropertyType/',views.PropertyType,name='PropertyType'),
    path('DigitalProperty/',views.DigitalPropertyAdmin,name='DigitalProperty'),

  
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)