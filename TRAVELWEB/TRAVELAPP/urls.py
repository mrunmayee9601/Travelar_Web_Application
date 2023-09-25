from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('hotel/',views.hotel,name='hotel'),
    path('Hotelinfo/',views.Hotelinfo,name='Hotelinfo'),
    path('HotelConfirm/',views.HotelConfirm,name='HotelConfirm'),
    path('Confirmed/',views.HConfirmed,name='HConfirmed'),
    path('packages/',views.packages,name='packages'),
    path('PackageBook/',views.pbook,name='pbook'),
    path('PackageConfirm/',views.Pconfirm,name='Pconfirm'),
    path('flights/',views.flights,name='flights'),
    path('FlightsBook/',views.fbook,name='fbook'),
    path('FlightsConfirm/',views.fconfirm,name='fconfirm'),
    path('FlightsDone/',views.flightdone,name='flightdone'),
    path('Reviews/',views.review,name='review'),
    path('Reviewcnf/',views.reviewcnf,name='reviewcnf'),
    path('Contact/',views.contact,name='contact'),
    path('Login/',views.Login,name='Login'),
    path('Register/', views.Register, name='Register'),
    path('Logout/',views.LogoutUser,name='LogoutUser'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="TRAVELAPP/Password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="TRAVELAPP/Password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="TRAVELAPP/Password_reset_confirm.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="TRAVELAPP/Password_reset_done.html"),name="password_reset_complete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)