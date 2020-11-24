from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import *
from .models import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password="Abinaya$03",
  database="djangoproject"
)

mycursor = mydb.cursor()
current_user = None
current_user_job = None
current_user_regno = None
staf_current=None
std_current=None
Allstud=None

# Create your views here.
def login(request):
    global mycursor,mydb,current_user,current_user_job,current_user_regno
    form=NameForm()

    if request.method=='POST':
        name = ''
        pswrd = ''
        print("start123")
        form = NameForm(request.POST)
        
        if form.is_valid():
            print("Validation success!")
            name = form.cleaned_data['name']
            pswrd = form.cleaned_data['password']
            context = {
            'name':name,
            'pswrd':pswrd,
            
            }
            print(context)
            mycursor.execute("SELECT * FROM stud_app_credentials")
            credentials_datas = mycursor.fetchall()
            all_creds = dict()
            for x in credentials_datas:
                all_creds[str(x[1])] = [x[2],x[3],x[4]]
            

            
            if str(context['name']) in all_creds:
                # print('passed')
                username = context['name']
                password = all_creds[str(context['name'])][0]
                job_class = all_creds[str(context['name'])][1]
                reg_no = all_creds[str(context['name'])][2]
                print(username,password,job_class,reg_no)

                if str(context['pswrd']) == password:
                    # print('passed2')
                    if job_class == 1:
                        print('Validated')
                        
                        return redirect("superuser")
                    
                    elif job_class == 2: 
                        print('Validated')
                        current_user = username
                        current_user_regno = reg_no
                        current_user_job = job_class
                        return redirect("superAdmin")
                    
                    elif job_class==4:
                        print('validated')
                        current_user = username
                        current_user_regno = reg_no
                        current_user_job = job_class
                        return redirect("superstaff")

                    elif job_class==3:
                        print('validated')
                        current_user = username
                        current_user_regno = reg_no
                        current_user_job = job_class
                        return redirect("superstud")
                    
                    
                    else:
                        return redirect('/')
                
                else:
                    print('Incorrect password')
            else:
                print('user not available')

                

            return redirect('/')
        else:
            form=NameForm()
    context={'form':form}
    return render(request,'login.html',context)


def superuser(request):
    # form=schoolAdmin(request.POST or None)
    # if 'add' in request.POST:
    if request.method=="POST":
        form=schoolAdmin(request.POST or None)
        if form.is_valid():
            print("superadmin form")
            nam=form.cleaned_data.get("name")
            usrn=form.cleaned_data.get("username")
            passwrd=form.cleaned_data.get("password")
            scl=form.cleaned_data.get("school")
            reg=form.cleaned_data.get("Regno")
            reg1=School_Admin(name=nam,username=usrn,password=passwrd,school=scl,Regno=reg)
            reg1.save()
            reg2=Credentials(name=nam,password=passwrd,job_Class=2,regno=reg)
            reg2.save()
            form=schoolAdmin()
    else:
        form=schoolAdmin()
    std=School_Admin.objects.all()
    context={'form':form,'stu':std}
    return render(request,'superuser.html',context)
   
    # return render(request,'superuser.html')

def delete_data(request,id):
    if request.method=="POST":
        pi=School_Admin.objects.get(Regno=id)
        p2=Credentials.objects.get(regno=id)
        pi.delete()
        p2.delete()
        return redirect("superuser")

def update_data(request,id):
    if request.method=="POST":
        pi=School_Admin.objects.get(Regno=id)
        print(pi)
        form=schoolAdmin(request.POST,instance=pi)
        if form.is_valid():
            
            print('saving here')
            usrn=form.cleaned_data.get("name")
            passwrd=form.cleaned_data.get("password")
            reg=form.cleaned_data.get("Regno")
            a=Credentials.objects.get(regno=reg)
            print(a)
            a.name=form.cleaned_data.get("name")
            a.password=form.cleaned_data.get("password")
            a.regno=form.cleaned_data.get("Regno")
            a.save()
            print(a)
            # # sql =("UPDATE stud_app_credentials SET name=%s password = %s WHERE regno=%d ;")           
            # val=(usrn,passwrd,reg)
            # mycursor.execute(sql,val)
            # mydb.commit()
            form.save()
            return redirect("superuser")
    else:
        print('update not sucessful')
        pi=School_Admin.objects.get(Regno=id)
        form=schoolAdmin(instance=pi)
        
    return render(request,"update_data.html",{'form':form})

def superAdmin(request):
    return render(request,'superAdmin.html')

def Student_page(request):
    if request.method=="POST":
        form=studentform(request.POST or None)
        if form.is_valid():
            print("superuser form")
            nam=form.cleaned_data.get("name")
            passwrd=form.cleaned_data.get("password")
            std=form.cleaned_data.get("stand")
            reg=form.cleaned_data.get("Regno")
            reg1=student(name=nam,password=passwrd,stand=std,Regno=reg)
            reg1.save()
            reg2=Credentials(name=nam,password=passwrd,job_Class=3,regno=reg)
            reg2.save()
            form=studentform()
    else:
        form=studentform()
    std=student.objects.all()
    context={'form':form,'stu':std}
    return render(request,'student.html',context)

def delete_stu_data(request,id):
    if request.method=="POST":
        pi=student.objects.get(Regno=id)
        p2=Credentials.objects.get(regno=id)
        pi.delete()
        p2.delete()
        return redirect("student")

def update_stu_data(request,id):
    if request.method=="POST":
        pi=student.objects.get(Regno=id)
        form=studentform(request.POST,instance=pi)
        if form.is_valid():
            print('saving here')
            reg=form.cleaned_data.get("Regno")
            a=Credentials.objects.get(regno=reg)
            print(a)
            a.name=form.cleaned_data.get("name")
            a.password=form.cleaned_data.get("password")
            a.regno=form.cleaned_data.get("Regno")
            a.save()
            print(a)
            form.save()
            return redirect("student")
    else:
        print('update not sucessful')
        pi=student.objects.get(Regno=id)
        form=studentform(instance=pi)
    return render(request,"update_stu_data.html",{'form':form})

def staff_page(request):
    if request.method=="POST":
        form=stafform(request.POST or None)
        if form.is_valid():
            print("superuser form")
            nam=form.cleaned_data.get("name")
            passwrd=form.cleaned_data.get("password")
            std=form.cleaned_data.get("stand")
            reg=form.cleaned_data.get("Regno")
            sub=form.cleaned_data.get("subj")
            reg1=staff(name=nam,password=passwrd,stand=std,Regno=reg,subj=sub)
            reg1.save()
            reg2=Credentials(name=nam,password=passwrd,job_Class=4,regno=reg)
            reg2.save()
            form=stafform()
    else:
        form=stafform()
    staf=staff.objects.all()
    context={'form':form,'stu':staf}
    return render(request,'staff.html',context)

def delete_staff_data(request,id):
    if request.method=="POST":
        pi=stafform.objects.get(Regno=id)
        p2=Credentials.objects.get(regno=id)
        pi.delete()
        p2.delete()
        return redirect("staff_page")

def update_staff_data(request,id):
    if request.method=="POST":
        pi=staff.objects.get(Regno=id)
        form=studentform(request.POST,instance=pi)
        if form.is_valid():
            print('saving here')
            reg=form.cleaned_data.get("Regno")
            a=Credentials.objects.get(regno=reg)
            print(a)
            a.name=form.cleaned_data.get("name")
            a.password=form.cleaned_data.get("password")
            a.regno=form.cleaned_data.get("Regno")
            a.save()
            print(a)
            form.save()
            return redirect("staff_page")
    else:
        print('update not sucessful')
        pi=staff.objects.get(Regno=id)
        form=stafform(instance=pi)
    return render(request,"update_staff_data.html",{'form':form})


def superstaff(request):
    global current_user,current_user_job,current_user_regno
    staf_current=staff.objects.get(Regno=current_user_regno)
    std_current=staf_current.stand
    Allstud=student.objects.filter(stand=std_current)
    
    staff_dict = {
        'name':current_user,'std_current':std_current,"Allstud":Allstud,"staf_current":staf_current,
    }

    return render(request,"superstaff.html",staff_dict)

def update_mark(request,id):
    global current_user,current_user_job,current_user_regno,staf_current,std_current,Allstud
    if request.method=="POST":
        pi=student.objects.get(Regno=id)
        print(pi)
        form=studentform2(request.POST,instance=pi)
        if form.is_valid():
            
            # print('saving here')
            # usrn=form.cleaned_data.get("name")
            # passwrd=form.cleaned_data.get("password")
            reg=form.cleaned_data.get("Regno")
            a=student.objects.get(Regno=reg)
            print(a)
            a.tamil=form.cleaned_data.get("tamil")
            a.science=form.cleaned_data.get("science")
            a.Maths=form.cleaned_data.get("Maths")
            a.Social=form.cleaned_data.get("Social")
            a.English=form.cleaned_data.get("English")

            a.save()
            print(a)
            # # sql =("UPDATE stud_app_credentials SET name=%s password = %s WHERE regno=%d ;")           
            # val=(usrn,passwrd,reg)
            # mycursor.execute(sql,val)
            # mydb.commit()
            form.save()
            
            staf_current=staff.objects.get(Regno=current_user_regno)
            std_current=staf_current.stand
            Allstud=student.objects.filter(stand=std_current)
    
            staff_dict = {
            'name':current_user,'std_current':std_current,"Allstud":Allstud
            }

            return render(request,"superstaff.html",staff_dict)
    else:
        print('update not sucessful')
        pi=student.objects.get(Regno=id)
        form=studentform2(instance=pi)
        
    return render(request,"update_mark.html",{'form':form})

def superstud(request):
    global current_user,current_user_job,current_user_regno
    stu=student.objects.get(Regno=current_user_regno)
    context={'stu':stu,}

    return render(request,"superstud.html",context)