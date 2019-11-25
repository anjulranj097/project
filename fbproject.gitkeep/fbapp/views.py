from django.shortcuts import render
from django.http import HttpResponse
from . models import *

# Create your views here.
def fn_page(request):
    return render(request,'login.html')

def fn_userlogin(request):
    print(request.POST)
    user_data = request.POST['username']
    pass_data = request.POST['Password']
          
    try:
        login = Login.objects.get(username=user_data)
        if login.password == pass_data:
            request.session['user_id'] = login.id
            return render(request,'successfullylogin1.html')
            #image_obj = UploadImage.objects.filter(fk_login=login)
            # if image_obj:
            #     response = {'image':image_obj}
            # return render(request,'profile.html',response)
        else:
            return render(request,'password.html')
    except Exception as e:
        print(str(e))
        return render(request,'fb1.html')

def fn_Userregister(request):
    if request.method == "POST":
        print(request.POST)
        uname = request.POST['username']
        username_exist = Login.objects.filter(username=uname).exists()
        if username_exist == False:

            firstname     = request.POST['firstname']
            lastname      = request.POST['lastname']
            password      = request.POST['password']
            dob           = request.POST['dob']
            gender        = request.POST['Radio']
            print(firstname,lastname,password,dob,gender)
    try:    
            login = Login(username=uname,password=password)
            login.save()
        
            if login.id > 0:
                userdetails_obj = UserDetails(first_name=firstname,last_name=lastname,date_of_birth=dob,gender=gender,fk_login=login)
                userdetails_obj.save()
                if userdetails_obj.id > 0:
                    return render(request,'login.html')
    except Exception as e:
            print(str(e))
            return render(request,'login.html')
    
def fn_ChangePassword(request):
    if request.method == "POST":
        user_id = request.session['user_id']
        print('session id: ',user_id)
        exist_password = request.POST['current_password']
        print('current password:'+exist_password)
        new_password   = request.POST['new_password']
        print('new password:'+new_password)
        login = Login.objects.get(id=user_id)
        print(login.password)
        if exist_password == login.password:
            login.password = new_password
            login.save()
            return render(request,'successfullylogin1.html',{'msg':'password updated'})
        else:
            return HttpResponse('password change failed')
    return render(request,'changepass.html')
    

def fn_ViewProfile(request):
    usr_id    = request.session['user_id']
    data      = UserDetails.objects.get(fk_login=usr_id) 
    print(data)
    log       = Login.objects.get(id=usr_id)
    context = {}
    try:
        if request.method == 'POST':
            firstnam = request.POST['firstname']
            lastnam  = request.POST['lastname']
            data.first_name = firstnam
            data.last_name  = lastnam
            data.save()
            if request.FILES:
                user_image = request.FILES['file_upload']
                upload = UploadImage.objects.get(fk_login=usr_id)
                upload.image = user_image
                upload.save()
        image_obj = UploadImage.objects.get(fk_login=usr_id)
        data.userimage = image_obj.image
        return render(request,'profile.html',{'user':data})
    except Exception as e:
        print('image does not exist')
        if request.method == 'POST':
            obj_upload = UploadImage(image=user_image,fk_login=log)
            obj_upload.save()
            data.userimage = obj_upload.image
        return render(request,'profile.html',{'user':data})

def fn_AddFriend(request):
    usr_id  = request.session['user_id']
    context = {}
    name    = UserDetails.objects.all().exclude(fk_login=usr_id)
    print(name)
    return render(request,'addfrnd.html',{'user':name})
      

    
        
    


