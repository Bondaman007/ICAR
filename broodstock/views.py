from django.shortcuts import render
import mysql.connector as sql
hat_id=''
brood_type=''
name_brood=''
mgt_proc=''
no_ponds=''
no_spawn=''
spec_id=''
no_fry=''
no_nur=''

# Create your views here.
def broodstockaction(request):
    global hat_id,brood_type,name_brood,mgt_proc,no_ponds,no_spawn,spec_id,no_fry,no_nur
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="Bondaman@21",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="hat_id":
                hat_id=value
            if key=="brood_type":
                brood_type=value
            if key=="name_brood":
                name_brood=value
            if key=="mgt_proc":
                mgt_proc=value
            if key=="no_ponds":
                no_ponds=value
            if key=="no_spawn":
                no_spawn=value
            if key=="spec_id":
                spec_id=value
            if key=="no_fry":
                no_fry=value
            if key=="no_nur":
                no_nur=value
            
        
        c="insert into broodstock values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(hat_id,brood_type,name_brood,mgt_proc,no_ponds,no_spawn,spec_id,no_fry,no_nur)
        cursor.execute(c)
        m.commit()
    
    return render(request,"broodstock.html")

