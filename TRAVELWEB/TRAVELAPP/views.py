from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.utils.datetime_safe import strftime

from .models import SearchHotel,BookHotel,ConfirmHotel
from .models import MyUsers
from .forms import SignUpForm
from .models import PBook
from .models import PConfirm
from .models import Review
from .models import SearchFlight,FlightInfo,Fconfirm
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
#Create your views here.

@login_required(login_url='Login')
def home(request):
     return render(request,'TRAVELAPP/Home.html')

def Register(request):
     if request.user.is_authenticated:
          return redirect('Home')
     else:
          form=SignUpForm()
          if request.method=="POST":
             form=SignUpForm(request.POST)
             if(form.is_valid()):
                  form.save()
                  user=form.cleaned_data.get('username')
                  messages.success(request,'Account for '+user+' is created!')
                  myuser=MyUsers(username=user,email=form.cleaned_data.get('email'))
                  myuser.save()
                  return redirect('Login')
          context={'form':form}
          return render(request, 'TRAVELAPP/Register.html',context)

def Login(request):
     if request.user.is_authenticated:
          return redirect('Home')
     else:
          if request.method=="POST":
             username = request.POST.get('uname')
             password = request.POST.get('pwd')
             user = authenticate(request,username=username,password=password)
             if user is not None:
                  login(request,user)
                  return redirect('home')
             else:
                  messages.info(request,'Username or Password is incorrect!')
          return render(request, 'TRAVELAPP/Login.html')

def LogoutUser(request):
     logout(request)
     return redirect('Login')

@login_required(login_url='Login')
def hotel(request):
     return render(request,'TRAVELAPP/H1.html')
@login_required(login_url='Login')
def Hotelinfo(request):
     v=""
     username=request.user.username
     c=v.join(request.POST.getlist("Cities"))
     chkin=request.POST.get("checkin")
     chkout=request.POST.get("checkout")
     no="".join((request.POST.getlist("rooms")))
     n=int(no)
     o_ref=SearchHotel(city=c,checkin=chkin,checkout=chkout,no_rooms=n,uname=username)
     o_ref.save()
     if(c.__eq__("Goa")):
          return render(request,'TRAVELAPP/HGoa.html')
     if(c.__eq__("Mumbai")):
          return render(request,'TRAVELAPP/HMumbai.html')
     if(c.__eq__("Delhi")):
          return render(request, 'TRAVELAPP/HDelhi.html')
     if (c.__eq__("Shimla")):
          return render(request, 'TRAVELAPP/HShimla.html')

@login_required(login_url='Login')
def HotelConfirm(request, a=None):
     if request.method=="POST":
          Hotelname=request.POST.get('hotelname')
          p=int(request.POST.get('cost'))
          #MUMBAI HOTELS
          if (Hotelname == "JW MARIOTT HOTEL"):
               city = "Mumbai"
               add = "Juhu Rd, Juhu Tara, Juhu, Mumbai, Maharashtra"
               img = "jw.jpg"
               room = "Deluxe, Guest Room, 1 King Or 2 Twin/single Bed(s)"
               myuser = request.user.username
               obj = BookHotel(City=city, Address=add, Hotel_name=Hotelname, room_type=room, price=p, pic=img,
                               user=myuser)
               obj.save()
               Search = SearchHotel.objects.filter(uname=myuser).last()
               Hotel = BookHotel.objects.filter(Hotel_name=Hotelname).last()
               total = (Search.no_rooms) * p
               count = ConfirmHotel.objects.filter(fname=request.user.first_name).count()
               if (count == 1):
                         total = total - (0.20 * total)
               elif (count == 2):
                         total =total- (0.30 *total)
               elif (count== 3):
                         total = total - (0.40 * total)
               elif (count >= 4):
                         total = total - (0.50 * total)

               fname = request.user.first_name
               lname = request.user.last_name
               mail = request.user.email
               context = {'Search': Search, 'Hotel': Hotel, 'Total': total, 'Firstname': fname, 'Lastname': lname,
                          'Mail': mail,'count':count+1}
               return render(request, "TRAVELAPP/HotelConfirm.html", context)
          if (Hotelname == "SAHARA STAR"):
               city = "Mumbai"
               add = "Opposite Domestic Airport, Vile Parle-East, Mumbai"
               img = "sahara_1.jpg"
               room = "Mercury City Facing"
               myuser = request.user.username
               obj = BookHotel(City=city, Address=add, Hotel_name=Hotelname, room_type=room, price=p, pic=img,
                               user=myuser)
               obj.save()
               Search = SearchHotel.objects.filter(uname=myuser).last()
               Hotel = BookHotel.objects.filter(Hotel_name=Hotelname).last()
               total = (Search.no_rooms) * p
               count = ConfirmHotel.objects.filter(fname=request.user.first_name).count()
               if (count == 1):
                    total = total - (0.20 * total)
               elif (count == 2):
                    total = total - (0.30 * total)
               elif (count == 3):
                    total = total - (0.40 * total)
               elif (count >= 4):
                    total = total - (0.50 * total)
               fname = request.user.first_name
               lname = request.user.last_name
               mail = request.user.email
               context = {'Search': Search, 'Hotel': Hotel, 'Total': total, 'Firstname': fname, 'Lastname': lname,
                          'Mail': mail,'count':count+1}
               return render(request, "TRAVELAPP/HotelConfirm.html", context)
          if (Hotelname == "HYATT REGENCY MUMBAI"):
               city = "Mumbai"
               add = "Bandra Kurla Complex Vicinity, Off Western Express Highway"
               img = "Hyatt.jpg"
               room = "Grand Room Twin with Bathtub"
               myuser = request.user.username
               obj = BookHotel(City=city, Address=add, Hotel_name=Hotelname, room_type=room, price=p, pic=img,
                               user=myuser)
               obj.save()
               Search = SearchHotel.objects.filter(uname=myuser).last()
               Hotel = BookHotel.objects.filter(Hotel_name=Hotelname).last()
               total = (Search.no_rooms) * p
               count = ConfirmHotel.objects.filter(fname=request.user.first_name).count()
               if (count == 1):
                    total = total - (0.20 * total)
               elif (count == 2):
                    total = total - (0.30 * total)
               elif (count == 3):
                    total = total - (0.40 * total)
               elif (count >= 4):
                    total = total - (0.50 * total)
               fname = request.user.first_name
               lname = request.user.last_name
               mail = request.user.email
               context = {'Search': Search, 'Hotel': Hotel, 'Total': total, 'Firstname': fname, 'Lastname': lname,
                          'Mail': mail,'count':count+1}
               return render(request, "TRAVELAPP/HotelConfirm.html", context)
          #DELHI HOTELS
          if (Hotelname == "VIVANTA NEW DELHI DWARKA"):
               city = "Delhi"
               add = "Metro Station Rd, Sector 21, Dwarka, New Delhi, Delhi 110075"
               img = "vivantadelhi.jpg"
               room = "Superior Room City View King Bed 32.5 Sq Mt Comp Basic Wifi"
               myuser = request.user.username
               obj = BookHotel(City=city, Address=add, Hotel_name=Hotelname, room_type=room, price=p, pic=img,
                               user=myuser)
               obj.save()
               Search = SearchHotel.objects.filter(uname=myuser).last()
               Hotel = BookHotel.objects.filter(Hotel_name=Hotelname).last()
               total = (Search.no_rooms) * p
               count = ConfirmHotel.objects.filter(fname=request.user.first_name).count()
               if (count == 1):
                    total = total - (0.20 * total)
               elif (count == 2):
                    total = total - (0.30 * total)
               elif (count == 3):
                    total = total - (0.40 * total)
               elif (count >= 4):
                    total = total - (0.50 * total)
               fname = request.user.first_name
               lname = request.user.last_name
               mail = request.user.email
               context = {'Search': Search, 'Hotel': Hotel, 'Total': total, 'Firstname': fname, 'Lastname': lname,
                          'Mail': mail,'count':count+1}
               return render(request, "TRAVELAPP/HotelConfirm.html", context)
          if (Hotelname == "COUNTRY INN AND SUITES BY RADDISON"):
               city = "Delhi"
               add = "A1, DLF South Court, District Center, Saket New Delhi, Delhi "
               img = "countryin.jpg"
               room = "Twin Smoking Superior Room"
               myuser = request.user.username
               obj = BookHotel(City=city, Address=add, Hotel_name=Hotelname, room_type=room, price=p, pic=img,
                               user=myuser)
               obj.save()
               Search = SearchHotel.objects.filter(uname=myuser).last()
               Hotel = BookHotel.objects.filter(Hotel_name=Hotelname).last()
               total = (Search.no_rooms) * p
               count = ConfirmHotel.objects.filter(fname=request.user.first_name).count()
               if (count == 1):
                    total = total - (0.20 * total)
               elif (count == 2):
                    total = total - (0.30 * total)
               elif (count == 3):
                    total = total - (0.40 * total)
               elif (count >= 4):
                    total = total - (0.50 * total)
               fname = request.user.first_name
               lname = request.user.last_name
               mail = request.user.email
               context = {'Search': Search, 'Hotel': Hotel, 'Total': total, 'Firstname': fname, 'Lastname': lname,
                          'Mail': mail,'count':count+1}
               return render(request, "TRAVELAPP/HotelConfirm.html", context)
          if (Hotelname == "RADISSON BLU NEW DELHI DWARKA"):
               city = "Delhi"
               add = "Plot No 4, Sector 13, Next To Metro Station, Dwarka City Centre, Near Airport"
               img = "raddison.jpg"
               room = "Superior Double Room"
               myuser = request.user.username
               obj = BookHotel(City=city, Address=add, Hotel_name=Hotelname, room_type=room, price=p, pic=img,
                               user=myuser)
               obj.save()
               Search = SearchHotel.objects.filter(uname=myuser).last()
               Hotel = BookHotel.objects.filter(Hotel_name=Hotelname).last()
               total = (Search.no_rooms) * p
               count = ConfirmHotel.objects.filter(fname=request.user.first_name).count()
               if (count == 1):
                    total = total - (0.20 * total)
               elif (count == 2):
                    total = total - (0.30 * total)
               elif (count == 3):
                    total = total - (0.40 * total)
               elif (count >= 4):
                    total = total - (0.50 * total)
               fname = request.user.first_name
               lname = request.user.last_name
               mail = request.user.email
               context = {'Search': Search, 'Hotel': Hotel, 'Total': total, 'Firstname': fname, 'Lastname': lname,
                          'Mail': mail,'count':count+1}
               return render(request, "TRAVELAPP/HotelConfirm.html", context)
          #SHIMLA HOTELS
          if(Hotelname=="GOLDENFERN RESORT SHIMLA"):
               city="Shimla"
               add="Kacchi Ghatti PO Tara Devi District Shimla"
               img="goldenfern.jpg"
               room="Classic Room"
               myuser=request.user.username
               obj=BookHotel(City=city,Address=add,Hotel_name=Hotelname,room_type=room,price=p,pic=img,user=myuser)
               obj.save()
               Search=SearchHotel.objects.filter(uname=myuser).last()
               Hotel=BookHotel.objects.filter(Hotel_name=Hotelname).last()
               total= (Search.no_rooms)*p
               count = ConfirmHotel.objects.filter(fname=request.user.first_name).count()
               if (count == 1):
                    total = total - (0.20 * total)
               elif (count == 2):
                    total = total - (0.30 * total)
               elif (count == 3):
                    total = total - (0.40 * total)
               elif (count >= 4):
                    total = total - (0.50 * total)
               fname=request.user.first_name
               lname=request.user.last_name
               mail=request.user.email
               context={'Search':Search,'Hotel':Hotel,'Total':total,'Firstname':fname,'Lastname':lname,'Mail':mail,'count':count+1}
               return render(request,"TRAVELAPP/HotelConfirm.html",context)
          if(Hotelname=="ROYAL TULIP SHIMLA KUFRI"):
               city= "Shimla"
               add= "National Highway 22, Kufri, Shimla, Himachal Pradesh 171012"
               img="royaltulip.jpg"
               room = "Deluxe Room - Staycation Special"
               myuser = request.user.username
               obj = BookHotel(City=city, Address=add, Hotel_name=Hotelname, room_type=room, price=p, pic=img, user=myuser)
               obj.save()
               Search = SearchHotel.objects.filter(uname=myuser).last()
               Hotel = BookHotel.objects.filter(Hotel_name=Hotelname).last()
               total = (Search.no_rooms) * p
               count = ConfirmHotel.objects.filter(fname=request.user.first_name).count()
               if (count == 1):
                    total = total - (0.20 * total)
               elif (count == 2):
                    total = total - (0.30 * total)
               elif (count == 3):
                    total = total - (0.40 * total)
               elif (count >= 4):
                    total = total - (0.50 * total)
               fname = request.user.first_name
               lname = request.user.last_name
               mail = request.user.email
               context = {'Search': Search, 'Hotel': Hotel, 'Total': total, 'Firstname': fname, 'Lastname': lname,
                          'Mail': mail,'count':count+1}
               return render(request, "TRAVELAPP/HotelConfirm.html", context)
          if (Hotelname == "TAJ THEOG RESORT AND SPA SHIMLA"):
               city = "Shimla"
               add = "Tehsil, Theog, Himachal Pradesh 171201"
               img = "theogtaj.jpg"
               room = "Premium Room Valley View King Bed"
               myuser = request.user.username
               obj = BookHotel(City=city, Address=add, Hotel_name=Hotelname, room_type=room, price=p, pic=img, user=myuser)
               obj.save()
               Search = SearchHotel.objects.filter(uname=myuser).last()
               Hotel = BookHotel.objects.filter(Hotel_name=Hotelname).last()
               total = (Search.no_rooms) * p
               count = ConfirmHotel.objects.filter(fname=request.user.first_name).count()
               if (count == 1):
                    total = total - (0.20 * total)
               elif (count == 2):
                    total = total - (0.30 * total)
               elif (count == 3):
                    total = total - (0.40 * total)
               elif (count >= 4):
                    total = total - (0.50 * total)
               fname = request.user.first_name
               lname = request.user.last_name
               mail = request.user.email
               context = {'Search': Search, 'Hotel': Hotel, 'Total': total, 'Firstname': fname, 'Lastname': lname,
                          'Mail': mail,'count':count+1}
               return render(request, "TRAVELAPP/HotelConfirm.html", context)
          #GOA HOTELS
          if (Hotelname == "BELEZA BY THE BEACH"):
               city = "Goa"
               add = "Thandwaddo, Betalbatim,Salcete, Goa"
               img = "v12_1.png"
               room = "Superior Double Room"
               myuser = request.user.username
               obj = BookHotel(City=city, Address=add, Hotel_name=Hotelname, room_type=room, price=p, pic=img, user=myuser)
               obj.save()
               Search = SearchHotel.objects.filter(uname=myuser).last()
               Hotel = BookHotel.objects.filter(Hotel_name=Hotelname).last()
               total = (Search.no_rooms) * p
               count = ConfirmHotel.objects.filter(fname=request.user.first_name).count()
               if (count == 1):
                    total = total - (0.20 * total)
               elif (count == 2):
                    total = total - (0.30 * total)
               elif (count == 3):
                    total = total - (0.40 * total)
               elif (count >= 4):
                    total = total - (0.50 * total)
               fname = request.user.first_name
               lname = request.user.last_name
               mail = request.user.email
               context = {'Search': Search, 'Hotel': Hotel, 'Total': total, 'Firstname': fname, 'Lastname': lname,
                          'Mail': mail,'count':count+1}
               return render(request, "TRAVELAPP/HotelConfirm.html", context)
          if (Hotelname == "VIVANTA GOA PANAJI"):
               city = "Goa"
               add = "D. B. Bandodkar Road, MG Road"
               img = "Vivanta.jpg"
               room = "Superior Room City View Queen Bed"
               myuser = request.user.username
               obj = BookHotel(City=city, Address=add, Hotel_name=Hotelname, room_type=room, price=p, pic=img, user=myuser)
               obj.save()
               Search = SearchHotel.objects.filter(uname=myuser).last()
               Hotel = BookHotel.objects.filter(Hotel_name=Hotelname).last()
               total = (Search.no_rooms) * p
               count = ConfirmHotel.objects.filter(fname=request.user.first_name).count()
               if (count == 1):
                    total = total - (0.20 * total)
               elif (count == 2):
                    total = total - (0.30 * total)
               elif (count == 3):
                    total = total - (0.40 * total)
               elif (count >= 4):
                    total = total - (0.50 * total)
               fname = request.user.first_name
               lname = request.user.last_name
               mail = request.user.email
               context = {'Search': Search, 'Hotel': Hotel, 'Total': total, 'Firstname': fname, 'Lastname': lname,
                          'Mail': mail,'count':count+1}
               return render(request, "TRAVELAPP/HotelConfirm.html", context)
          if (Hotelname == "THE LALIT GOLF AND SPA RESORT"):
               city = "Goa"
               add = "Raj Baga, Canacona, Goa"
               img = "lalit.jpg"
               room = "Garden View Suite King"
               myuser = request.user.username
               obj = BookHotel(City=city, Address=add, Hotel_name=Hotelname, room_type=room, price=p, pic=img, user=myuser)
               obj.save()
               Search = SearchHotel.objects.filter(uname=myuser).last()
               Hotel = BookHotel.objects.filter(Hotel_name=Hotelname).last()
               total = (Search.no_rooms) * p
               count = ConfirmHotel.objects.filter(fname=request.user.first_name).count()
               if (count == 1):
                    total = total - (0.20 * total)
               elif (count == 2):
                    total = total - (0.30 * total)
               elif (count == 3):
                    total = total - (0.40 * total)
               elif (count >= 4):
                    total = total - (0.50 * total)
               fname = request.user.first_name
               lname = request.user.last_name
               mail = request.user.email
               context = {'Search': Search, 'Hotel': Hotel, 'Total': total, 'Firstname': fname, 'Lastname': lname,
                          'Mail': mail,'count':count+1}
               return render(request, "TRAVELAPP/HotelConfirm.html", context)

@login_required(login_url='Login')
def HConfirmed(request):
     if(request.method=="POST"):
          name=request.POST.get('pname')
          indate=request.POST.get('check-in')
          outdate=request.POST.get('check-out')
          fname=request.POST.get('fname')
          lname=request.POST.get('lname')
          mobile=request.POST.get('Phn')
          email=request.POST.get('EmailId')
          type=request.POST.get('travelers')
          payment=request.POST.get('radio')
          amt=request.POST.get('Tamount')
          obj=ConfirmHotel(name=name,indate=indate,outdate=outdate,fname=fname,lname=lname,mobile=mobile,email=email,room_type=type,payment=payment,total=amt)
          obj.save()
          send_mail(
               'Confirmation Mail of Booking done for '+fname,
               'Thankyou for Booking through Travelar.We have now booked and confirmed your tour as follows:'+'\n'+
               'Name of Customer: '+fname+' '+lname+'\n'+
               'Contact Number: '+mobile+'\n'+
               'Email: '+email+'\n'+
               'Name of Booked Hotel: '+name+'\n'+
               'Check In date: '+indate+'\n'+
               'Check Out date: '+outdate+'\n'+
               'Type of Room: '+type+'\n'+
               'Payment Method: '+payment+'\n'+
               'Total Bill: Rs '+amt+'\n',
               'travelar.group@gmail.com',
               [email],
               fail_silently=False)
          cnf=ConfirmHotel.objects.filter(fname=request.user.first_name).last()
          context={'Cnf':cnf}
          return render(request,'TRAVELAPP/Home.html',context)



@login_required(login_url='Login')
def packages(request):
     return render(request,'TRAVELAPP/P1.html')

@login_required(login_url='Login')
def pbook(request):
     if(request.method=="POST"):
          user=request.user.username
          Name=request.POST.get('p_name')
          Durations=request.POST.get('duration')
          included=request.POST.get('inclusions')
          price=request.POST.get('price')
          p=price.replace('Rs.','')
          p1=float(p.replace('/-*',''))

          counter=PConfirm.objects.filter(fname=request.user.first_name).count()
          if (counter == 1):
               p1 = p1 - (0.20 * p1)
          elif (counter == 2):
              p1 = p1 - (0.30 * p1)
          elif (counter == 3):
               p1 = p1 - (0.40 * p1)
          elif (counter >= 4):
               p1 = p1 - (0.50 * p1)
          if(Name==" Exotic Goa 3N4D"):
             pic="v209_0.png"
          if(Name==" Exotic Sikkim 5N6D"):
               pic="v212_570.png"
          if (Name == " Exotic Kerla 3N4D"):
               pic="v212_647.png"
          if (Name == " Exotic Pondicherry 4N5D"):
               pic = "p212_570.jpg"
          if (Name == " Exotic Rajastan 3N4D"):
               pic = "s212_570.jpg"
          if (Name == " Exotic Mumbai 2N3D"):
               pic = "m212_570.jpg"
          obj=PBook(Pname=Name,duration=Durations,inclusions=included,price=p1,user=user,pic=pic)
          obj.save()
          Pack=PBook.objects.filter(user=request.user.username).last()
          fname = request.user.first_name
          lname = request.user.last_name
          mail = request.user.email
          context={'Pack':Pack,'Firstname': fname, 'Lastname': lname,
                          'Mail': mail,'counter':counter+1}
          return render(request,'TRAVELAPP/Pconfirm.html',context)

@login_required(login_url='Login')
def Pconfirm(request):
     if (request.method == "POST"):
          name = request.POST.get('pname')
          date = request.POST.get('check-in')
          fname = request.POST.get('fname')
          lname = request.POST.get('lname')
          mobile = request.POST.get('Phn')
          email = request.POST.get('EmailId')
          duration = request.POST.get('address')
          payment = request.POST.get('radio')
          amt = request.POST.get('Tamount')
          obj = PConfirm(name=name, date=date, fname=fname, lname=lname, mobile=mobile,
                             email=email,no_of_days=duration, payment=payment, total=amt)
          obj.save()
          send_mail(
               'Confirmation Mail of Booking done for ' + fname,
               'Thankyou for Booking through Travelar.We have now booked and confirmed your tour as follows:' + '\n' +
               'Name of Customer: ' + fname + ' ' + lname + '\n' +
               'Contact Number: ' + mobile + '\n' +
               'Email: ' + email + '\n' +
               'Name of Booked Package: ' + name + '\n' +
               'Date of Journey: ' + date + '\n' +
               'Duration : ' + duration + '\n' +
               'Payment Method: ' + payment + '\n' +
               'Total Bill:Rs' + amt + '\n'+
               '!HAPPY HOLIDAYS!',
               'travelar.group@gmail.com',
               [email],
               fail_silently=False)

          cnfp = PConfirm.objects.filter(fname=request.user.first_name).last()
          context = {'cnfp': cnfp}
          return render(request, 'TRAVELAPP/Home.html', context)

@login_required(login_url='Login')
def flights(request):
     return render(request,'TRAVELAPP/F1.html')

@login_required(login_url='Login')
def fbook(request):
     if(request.method=="POST"):
          start=''.join(request.POST.getlist('From'))
          end=''.join(request.POST.getlist('To'))
          date=request.POST.get('date')
          number=''.join(request.POST.getlist('adults'))
          no=int(number)
          user=request.user.username
          type=''.join(request.POST.getlist('class'))
          obj=SearchFlight(boarding=start,destination=end,type=type,seats=no,date=date,user=user)
          obj.save()
          if (start.__eq__("Mumbai") and end.__eq__("Shimla")):
               return render(request,"TRAVELAPP/MumtoShim.html")
          if(start.__eq__("Mumbai") and end.__eq__("Cochin")):
               return render(request,"TRAVELAPP/MumtoCoc.html")
          if (start.__eq__("Delhi") and end.__eq__("Shimla")):
               return render(request, "TRAVELAPP/DelhitoShim.html")
          if (start.__eq__("Delhi") and end.__eq__("Cochin")):
               return render(request, "TRAVELAPP/DelhitoCoc.html")

@login_required(login_url='Login')
def fconfirm(request):
     if(request.method=="POST"):
          airline=request.POST.get('Airline')
          dtime=request.POST.get('dtime')
          atime=request.POST.get('atime')
          price=request.POST.get('price')
          price1=int(price)
          username=request.user.username
          obj=FlightInfo(airline=airline,departure=dtime,arrival=atime,price=price1,username=username)
          obj.save()
          Search=SearchFlight.objects.filter(user=username).last()
          info=FlightInfo.objects.filter(username=username).last()
          fname=request.user.first_name
          total=int(Search.seats)*price1
          count=Fconfirm.objects.filter(username=request.user.username).count()
          if (count == 1):
               total = total - (0.20 * total)
          elif (count == 2):
               total = total - (0.30 * total)
          elif (count == 3):
               total = total - (0.40 * total)
          elif (count >= 4):
               total = total - (0.50 * total)
          lname=request.user.last_name
          mail=request.user.email
          context={'Search':Search,'info':info,'fname':fname,'lname':lname,'mail':mail,'total':total,'count':count+1}
          return render(request,"TRAVELAPP/Fconfirm.html",context)

@login_required(login_url='Login')
def flightdone(request):
     if(request.method=="POST"):
          number=request.POST.get('phn')
          payment=request.POST.get('radio')
          username=request.user.username
          date=request.POST.get('check-in')
          bill=request.POST.get('Tamount1')
          bill1=float(bill)
          obj=Fconfirm(payment=payment,phone=number,username=username,bill=bill1)
          obj.save()
          Search = SearchFlight.objects.filter(user=username).last()
          info = FlightInfo.objects.filter(username=username).last()
          fname = request.user.first_name
          lname = request.user.last_name
          mail = request.user.email
          send_mail(
               'Confirmation Mail of Booking done for ' + fname,
               'Thankyou for Booking through Travelar.We have now booked and confirmed your tour as follows:' + '\n' +
               'Name of Customer: ' + fname + ' ' + lname + '\n' +
               'Contact Number: ' + number + '\n' +
               'Date of Journey: '+date+'\n'+
               'Email: ' + mail + '\n' +
               'Name of Booked Flight: ' + info.airline + '\n' +
               'Payment Method: ' + payment + '\n' +
               'Total Bill: ' + bill+ '\n'+
               '!Happy Journey!'+'\n' ,
               'travelar.group@gmail.com',
               [mail],
               fail_silently=False)

          context = {'Search':Search,'info':info}
          return render(request, 'TRAVELAPP/Home.html', context)

@login_required(login_url='Login')
def review(request):
     return render(request,"TRAVELAPP/AddReview.html")

@login_required(login_url='Login')
def reviewcnf(request):
     if(request.method=="POST"):
          fname=request.POST.get('f_name')
          lname=request.POST.get('l_name')
          mail=request.POST.get('email_id')
          review=request.POST.get('review')
          stars=request.POST.get('rating')
          obj=Review(fname=fname,lname=lname,mail=mail,review=review,stars=stars)
          obj.save()
          send_mail('Review received given by '+fname,
                    'Thankyou for giving your valuable feedback to us.'+'\n'+
                    'We will surely try to improve on the points mentioned by you'+'\n'+
                    'Here is what we received from you:'+'\n' +
                    'Name of User: '+fname+''+lname+''+'\n'+
                    'Review of User: '+review+'\n'+
                    'Rating given by User: '+stars+'\n'+
                    '!THANKYOU!'+'\n'+'HAPPY HOLIDAYS',
                    'travelar.group@gmail.com',
                    [mail],
                    fail_silently=False)
          s=Review.objects.filter(fname=request.user.first_name).last()
          context = {'s':s}
          return render(request, 'TRAVELAPP/Home.html', context)

@login_required(login_url='Login')
def contact(request):
     return render(request,"TRAVELAPP/chatbot.html")