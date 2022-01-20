from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import *
from django.contrib import messages
from django.contrib.sessions.models import Session
import datetime

# Create your views here.
def home(request):
	return render(request,'home.html',{})

def base(request):
	return render(request,'base.html',{})

def UserRegister(request):
	if request.method == "POST":
		U_name = request.POST['name']
		U_mobile = request.POST['number']
		U_email = request.POST['userEmail']
		U_username = request.POST['username']
		U_password = request.POST['password']
		U_address = request.POST['address']
		users = UserRegisters(Name = U_name, Mobile= U_mobile, Email =  U_email, Address =  U_address, Username = U_username, Password= U_password)
		users.save()
		messages.info(request, 'Registered Sucessfully')
		return render(request, 'UserLogin.html', {})
	else:
		return render(request,'UserRegister.html',{})

def AdminRegister(request):
	if request.method == "POST":
		U_id = request.POST['id']
		U_username = request.POST['username']
		U_password = request.POST['password']
		admin = admindata(id = U_id, Username = U_username, Password= U_password)
		admin.save()
		messages.info(request, 'Registered Sucessfully')
		return render(request, 'AdminLogin.html', {})
	else:
		return render(request,'AdminRegister.html',{})

def UserLogin(request):
    if request.method == "POST":
        C_name = request.POST['Username']
        C_password = request.POST['password']
        # users = auth.authenticate(User_name = uname,Passwords = pword)
        print('done')
        if UserRegisters.objects.filter(Username=C_name, Password=C_password).exists():
            user = UserRegisters.objects.all().filter(Username=C_name, Password=C_password)
            messages.info(request, 'logged in')
            request.session['UserId'] = user[0].id
            request.session['UserType'] = "User"
            request.session['login'] = "Yes"
            return redirect("/ViewProperty")
        else:
            messages.info(request, 'Please Register')
            return redirect("/UserRegister")
    else:
    	return render(request,'UserLogin.html',{})

def AdminLogin(request):
	if request.method == "POST":
		A_username = request.POST['admin']
		A_password = request.POST['passwords']
		if admindata.objects.filter(Username = A_username,Password = A_password).exists():
			ad = admindata.objects.get(Username=A_username, Password=A_password)
			print('d')
			messages.info(request,'Your login is Sucessfull')
			request.session['UserType'] = "Admin"
			request.session['login'] = "Yes"
			return redirect("/ViewProperties")
		else:
			print('y')
			messages.error(request, 'Error wrong username/password')
	else:
		return render(request, "Adminlogin.html", {})

def logout(request):
    Session.objects.all().delete()
    return redirect('/')

def ViewProperty(request):
	if request.method =="POST":
		searched = request.POST['search']
		searches=PropertyDetails.objects.filter(Area__contains=searched)
		return render(request,'ViewProperty.html',{'searched':searched,'searches':searches})
	else:
		showprop = PropertyDetails.objects.all()
		print(showprop)
		return render(request,'ViewProperty.html',{'showprop':showprop})


def Propertydetails(request,id):
	prop1=PropertyDetails.objects.filter(id=id)
	return render(request,'Propertydetails.html', {'prop1':prop1})

def FavouriteProperty(request):
	if request.method =="POST":
		UserId=request.session['UserId']
		PID=request.POST['Pid']
		ptype=request.POST['type']
		pprice=request.POST['price']
		parea=request.POST['area']
		psqft=request.POST['sqft']
		if Favaourite.objects.filter(UserID=UserId,PropertyID=PID).exists():
			prop2=Favaourite.objects.all().filter(UserID=UserId)
			messages.info(request,'Property Already Added to favourite')
			return render(request,'FavouriteProperty.html', {'prop2':prop2})
			
		else: 
			favprop = Favaourite(UserID=UserId,PropertyID = PID, P_Type = ptype, Price = pprice, Area = parea, Sqft = psqft)
			favprop.save()
			prop2=Favaourite.objects.all().filter(UserID=UserId)
			messages.info(request,'Property Sucessfully Added to favourite')
			return render(request,'FavouriteProperty.html', {'prop2':prop2})
			
	else:
		UserId=request.session['UserId']
		prop2=Favaourite.objects.all().filter(UserID=UserId)
		return render(request,'FavouriteProperty.html', {'prop2':prop2})

def BookAppointment(request):
	if request.method == "POST":
		UserId=request.session['UserId']
		PID=request.POST['Pid']
		pprice=request.POST['price']
		parea=request.POST['area']
		date = datetime.datetime.now()
		if Appointment.objects.filter(User_ID=UserId,Property_ID=PID).exists():
			book1=Appointment.objects.all().filter(User_ID=UserId)
			messages.info(request,'Appointment Already Booked Sucessfully')
			return render(request,'BookAppointment.html',{'book1':book1})
		else:
			book = Appointment(User_ID=UserId,Property_ID = PID,Price = pprice, Area = parea,Date=date)
			book.save()
			book1=Appointment.objects.all().filter(User_ID=UserId)
			messages.info(request,'Appointment Booked Sucessfully')
			return render(request,'BookAppointment.html',{'book1':book1})
	else:
		UserId=request.session['UserId']
		book1=Appointment.objects.all().filter(User_ID=UserId)
		return render(request,'BookAppointment.html',{'book1':book1})

def AddProperty(request):
	if request.method == "POST":
		P_type=request.POST['type']
		P_sqft=request.POST['sqft']
		P_types=request.POST['types']
		P_address=request.POST['Address']
		P_landmark=request.POST['Landmark']
		P_devpname=request.POST['Developer Name']
		P_area=request.POST['area']
		P_price=request.POST['Price']
		P_bedroom=request.POST['Bedroom']
		P_bathroom=request.POST['Bathroom']
		P_park=request.POST['Parking']
		P_cctv=request.POST['CCTV']
		P_furnished=request.POST['Furnished']
		P_image=request.FILES['Image']
		prop = PropertyDetails(Type = P_type,Sqft = P_sqft,PropertyType = P_types,Address = P_address,Landmark = P_landmark,Area = P_area,DeveloperName = P_devpname,Price = P_price,Bedroom = P_bedroom,Bathroom = P_bathroom,Furnished = P_furnished,Parking = P_park,CCTV = P_cctv,Image = P_image)
		prop.save()
		return render(request,'home.html',{})
	else:
		return render(request,'AddProperty.html',{})


def ViewCustomer(request):
	if request.method =="POST":
		searched = request.POST['search']
		searches=UserRegisters.objects.filter(id__contains=searched)
		return render(request,'ViewCustomer.html',{'searched':searched,'searches':searches})
	else:
		users=UserRegisters.objects.all()
		return render(request,'ViewCustomer.html',{'users':users})

def BookedAppointment(request):
	booked=Appointment.objects.all()
	return render(request,'BookedAppointment.html',{'booked':booked})

def destroy(request, id):
	prop2 = Favaourite.objects.get(id=id)  
	prop2.delete()
	return redirect('/FavouriteProperty')

def remove(request, id):
	book1 = Appointment.objects.get(id=id)  
	book1.delete()
	return redirect('/BookAppointment')

def delete(request, id):
	users = UserRegisters.objects.get(id=id)  
	users.delete()
	return redirect('/ViewCustomer')

def deleteproperty(request, id):
	users = PropertyDetails.objects.get(id=id)  
	users.delete()
	return redirect('/ViewProperties')

def deletedigital(request, id):
	users = DigitalProperty.objects.get(id=id)  
	users.delete()
	return redirect('/DigitalProperty')

def ViewProperties(request):
	if request.method =="POST":
		searched = request.POST['search']
		searches=PropertyDetails.objects.filter(id__contains=searched)
		return render(request,'ViewProperties.html',{'searched':searched,'searches':searches})
	else:
		prop3=PropertyDetails.objects.all()
		return render(request,'ViewProperties.html',{'prop3':prop3})

def updates(request,id):
	prop3 = PropertyDetails.objects.all().filter(id=id)
	return render(request,'updates.html',{'prop3':prop3})

def updated(request):
	if request.method =="POST":
		P_Id=request.POST['property_id']
		P_type=request.POST['type']
		P_sqft=request.POST['sqft']
		P_types=request.POST['types']
		P_address=request.POST['Address']
		P_landmark=request.POST['Landmark']
		P_devpname=request.POST['Developer Name']
		P_area=request.POST['area']
		P_price=request.POST['Price']
		P_bedroom=request.POST['Bedroom']
		P_bathroom=request.POST['Bathroom']
		P_park=request.POST['Parking']
		P_cctv=request.POST['CCTV']
		P_furnished=request.POST['Furnished']
		P_image=request.FILES['Image']
		prop = PropertyDetails.objects.filter(id=P_Id).update(Type = P_type,Sqft = P_sqft,PropertyType = P_types,Address = P_address,Landmark = P_landmark,Area = P_area,DeveloperName = P_devpname,Price = P_price,Bedroom = P_bedroom,Bathroom = P_bathroom,Furnished = P_furnished,Parking = P_park,CCTV = P_cctv,Image = P_image)
		return redirect('/ViewProperties')
	else:
		return redirect('/ViewProperties')

def AddAdvertisement(request):
    if request.method == "POST":
    	name=request.POST['name']
    	Ads=request.FILES['filebutton']
    	ad = Advertisements(Name = name,AdsImage = Ads)
    	ad.save()
    	return redirect('/Advertisement')
    else:
    	return render(request,'AddAdvertisement.html',{})

def Advertisement(request):
	ad=Advertisements.objects.all()
	return render(request,'Advertisement.html',{'ad':ad})

def PropertyType(request):
	if request.method =="POST":
		Prop_Type=request.POST['Types']
		print(Prop_Type)
		print('a')
		P_Type=PropertyDetails.objects.filter(PropertyType__contains=Prop_Type)
		print(P_Type)
		print('b')
		return render(request,'ViewProperty.html',{'Prop_Type':Prop_Type,'P_Type':P_Type})
		print('c')
	else:
		showprop = PropertyDetails.objects.all()
		print(showprop)
		return render(request,'ViewProperty.html',{'showprop':showprop})

def DigitalViewProperty(request):
	if request.method =="POST":
		searched = request.POST['search']
		searches=PropertyDetails.objects.filter(Area__contains=searched)
		return render(request,'ViewProperty.html',{'searched':searched,'searches':searches})
	else:
		showprop = PropertyDetails.objects.all()
		print(showprop)
		return render(request,'ViewProperty.html',{'showprop':showprop})

def AddDigitalProperty(request):
	if request.method == "POST":
		P_type=request.POST['type']
		P_link=request.POST['link']
		P_image=request.FILES['Image']
		prop = DigitalProperty(Type = P_type,Link = P_link,Image = P_image)
		prop.save()
		return render(request,'home.html',{})
	else:
		return render(request,'AddDigitalProperty.html',{})

def ViewDigitalProperties(request):
	if request.method =="POST":
		searched = request.POST['search']
		searches=DigitalProperty.objects.filter(id__contains=searched)
		print(searches)
		return render(request,'ViewDigitalProperties.html',{'searched':searched,'searches':searches})
	else:
		prop3=DigitalProperty.objects.all()
		print(prop3)
		return render(request,'ViewDigitalProperties.html',{'prop3':prop3})

def DigitalPropertyAdmin(request):
	if request.method =="POST":
		searched = request.POST['search']
		searches=DigitalProperty.objects.filter(id__contains=searched)
		print(searches)
		return render(request,'DigitalProperty.html',{'searched':searched,'searches':searches})
	else:
		prop3=DigitalProperty.objects.all()
		print(prop3)
		return render(request,'DigitalProperty.html',{'prop3':prop3})