from django.shortcuts import render
import mysql.connector as sql
user_name=''
password=''

# Create your views here.
def loginpageaction(request):
    #global user_name,password
    #if request.method=="POST":
    #    m=sql.connect(host="localhost",user="root",password="Bondaman@21",database='hatchery_seed')
    #    cursor=m.cursor()
    #    d=request.POST
    #    # for key,value in d.items():

    #c="insert into login values('{}','{}')".format(user_name,password)
    #cursor.execute(c)
    #m.commit()

    return render(request,"loginpage.html")