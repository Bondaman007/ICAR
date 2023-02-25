from django.shortcuts import render
import mysql.connector as sql
user_id=''
first=''
last=''
gender=''
email=''
phone=''
organization=''
department=''
designation=''
password=''
confirm=''
# Create your views here.
def signupaction(request):
    global user_id,first,last,gender,email,phone,organization,department,designation,password,confirm
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="Bondaman@21",database="authentic")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="user_id":
                user_id=value
            if key=="firstName":
                first=value
            if key=="lastName":
                last=value
            if key=="gender":
                gender=value
            if key=="email":
                email=value
            if key=="phone":
                phone=value
            if key=="organization":
                organization=value
            if key=="dept":
                department=value
            if key=="designation":
                designation=value
            if key=="password":
                password=value
            if key=="passconfirmation":
                confirm=value
        
        c=f"insert into users values('{user_id}','{first}','{last}','{gender}','{email}',{phone},'{organization}','{department}','{designation}','{password}','{confirm}')"
        cursor.execute(c)
        m.commit()    
    return render(request,'signuppage.html')