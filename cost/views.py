from django.shortcuts import render
import mysql.connector as sql
hat_id=''
cost_spa=''
cost_fry=''
cost_fin=''
cost_year=''

# Create your views here.
def costaction(request):
    global hat_id,cost_spa,cost_fry,cost_fin,cost_year
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="Bondaman@21",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="hat_id":
                hat_id=value
            if key=="cost_spa":
                cost_spa=value
            if key=="cost_fry":
                cost_fry=value
            if key=="cost_fin":
                cost_fin=value
            if key=="cost_year":
                cost_year=value
        
        c="insert into cost values('{}','{}','{}','{}','{}')".format(hat_id,cost_spa,cost_fry,cost_fin,cost_year)
        cursor.execute(c)
        m.commit()
    
    return render(request,"cost.html")

