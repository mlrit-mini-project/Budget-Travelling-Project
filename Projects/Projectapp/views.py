from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse


import mysql.connector

# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if(request.method=='POST'):  
           
        print('in register post event')
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="people"        
        )
        mycursor = conn.cursor()
        #retrive post details       
        
        fullname=request.POST['fullname']
        email=request.POST['email']
        password=request.POST['password']
           
        
        mycursor.execute("insert into users(fullname,email,password) values('"+fullname+"','"+email+"','"+password+"')")
        conn.commit()
        return render(request,'register.html',{"status":"Registered Successfully"})
    else:
        return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="people"        
        )
        mycursor = conn.cursor()
        #retrive post details       
        
        email=request.POST['email']
        password=request.POST['password']     
        
        mycursor.execute("select * from users where email='"+email+"' and password='"+password+"'")
        result=mycursor.fetchone()
        
        if(result!=None):
            request.session['email'] = email         
            return redirect('dashboard')
            #redirect('studenthome')
        else:
            #messages.warning(request, 'Invalid credentials!')
            return render(request,'login.html',{'status':'invalid credentials'})    
    else:
        
        return render(request,'login.html',{'status':'invalid credentials'})
    

def dashboard(request):
    if "email" in request.session:
        email=request.session['email']
        print("logged in as email",email)
        return render(request,'dashboard.html',{"email":email})
    return render(request,'register.html')
def logout(request):
    return render(request,'index.html')
def success(request):
    return render(request,'success.html')
def budget(request):
    if request.method == 'POST':
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="people"        
        )
        mycursor = conn.cursor()
        #retrive post details       
        
        service=request.POST['service']
        vehicletype=request.POST['vehicletype']
            
        
        mycursor.execute("select * from verify where service='"+service+"' and vehicletype='"+vehicletype+"'")
        result=mycursor.fetchone()
        
        if(result!=None):
            request.session['service'] = service  
            request.session['vehicletype'] = vehicletype
            return redirect('location')
            #redirect('studenthome')
        else:
            #messages.warning(request, 'Invalid credentials!')
            return render(request,'budget.html',{'status':'invalid credentials'})    
    else:
        
        return render(request,'budget.html',{'status':'invalid credentials'})
def location(request):
    return render(request,'location.html')
def Ts(request):
    return render(request,'Ts.html')
def Tn(request):
    return render(request,'Tn.html')

