from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UsersStudy,Register
from .forms import usersstudymodelform,registermodelform,LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#Register View
def register(request):
    if request.method=="POST":
        form = registermodelform(request.POST)
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password!=confirm_password:
            messages.error(request,'Password MisMatch')
            return redirect('Register')
        else:
            form.save()
            messages.success(request,"Registed SuccessFully! Now You Can Login")
            return redirect('Register')
    else:
        form = registermodelform()
    print(form)

    return render(request,'Register.html',{'form':form})

#Login View
def Login(request):
    if request.method=="POST":
        username  = request.POST.get('username')
        password = request.POST.get('password')
        Object = Register.objects.filter(username=username,password=password).exists()
        if Object:
            Data = Register.objects.filter(username=username).first()
            request.session['username'] = Data.username #Dictionary-like-object.allows you to store and retrieve data on a per user basis for the duration of user's session
            return redirect('Users')
        else:
            messages.error(request,'INVAILD LOGIN DETAILS')
            return redirect('Login')
    return render(request,'Login.html',{'form':LoginForm})


#Users View
def users(request):
    print(request.session.get('username'))
    if 'username' not in request.session:
        return redirect('Login')
    Data = Register.objects.filter(username=request.session.get('username')).first()
    print(Data)   
    Object = UsersStudy.objects.filter(admin=Data)
    print(Object)
    
    # return render(request,'Users.html',{'Data':Data,'Object':Object})

    responses = render(request,'Users.html',{'Data':Data,'Object':Object})
    print(responses)
    responses['Cache-Control'] = 'no-cache,no-store,must-revalidate' #Tells the browser not to cache the page
    print(responses['Cache-Control'])
    responses['Pragma'] = 'no-cache' #To prevent the cache using http 1.0 backward-compatible header
    print(responses['Pragma'])
    responses['Expires'] = '0' #Forces the browser to consider the page as expired immdiately
    print(responses['Expires'])
    return responses
    
#Add Study View
def AddStudy(request):
    if 'username' in request.session:    
        if request.method=="POST":
            Object = Register.objects.filter(username=request.session.get('username')).first()
            form = UsersStudy()
            form.study_name = request.POST.get('study_name')
            form.study_description = request.POST.get('study_description')
            form.study_phase = request.POST.get('study_phase')
            form.sponser_name = request.POST.get('sponser_name')
            form.admin = Object
            form.save()
            return redirect('Users')
    else:
        return redirect('Login')
    return render(request,'study.html',{'usersstudymodelform':usersstudymodelform})

#View 
def View(request,id):
    if 'username' in request.session:
         Object = UsersStudy.objects.get(study_id=id)
         context = {"Object":Object}
    else:
        return redirect('Login')
    return render(request,"View.html",context)

#Update view
def Update(request,id):
    Object = UsersStudy.objects.get(study_id=id)
    if 'username' in request.session:
        if request.method == "POST":
            form = usersstudymodelform(request.POST,instance=Object)
            form.save()
            messages.success(request,f"Updated {Object.study_name} SuccessFully")
            return redirect('Users')
        else:
            form = usersstudymodelform(instance=Object)
    else:
        return redirect('Login')
    return render(request,"Update.html",{"form":form})

#ConfirmDelete view
def ConfirmDelete(request,id):
    if 'username' in request.session:
        Object = UsersStudy.objects.get(study_id=id)
    else:
        return redirect('Login')
    return render(request,"Delete.html",{"Object":Object})

#Delete View
def Delete(request,id):
    if 'username' in request.session:
        print(id)
        Object = UsersStudy.objects.get(study_id=id)
        Object.delete()
        messages.success(request,f"Deleted StudyName: {Object.study_name} Successfully")
        return redirect('Users')
    else:
        return redirect('Login')

#Logout view
def Logout(request):
    request.session.flush() #clear the session completely
    return redirect('HomePage')

#Home Viewś
def Home(request):
    return render(request,'base.html')


# Create your views here.
