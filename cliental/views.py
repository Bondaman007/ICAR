from django.shortcuts import render
import mysql.connector as sql
hat_id=''
client=''
yrs=''
client_id=''


# Create your views here.
def clientalaction(request):
    global hat_id,client,yrs,client_id
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="Bondaman@21",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="hat_id":
                hat_id=value
            if key=="client":
                client=value
            if key=="yrs":
                yrs=value
            if key=="clt_id":
                client_id=value
        
        c="insert into cliental values('{}','{}','{}','{}')".format(hat_id,client,yrs,client_id)
        cursor.execute(c)
        m.commit()
    
    return render(request,"cliental.html")
