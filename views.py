from django.shortcuts import render,redirect 
from django.http import HttpResponse
from .models import Registration
from .models import Job
from .models import Candidate
from .models import HrReg
from .models import Jobinfo
from .models import Resume
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views import View
def job(request):
    if (request.session.has_key("uid")):
        suid=request.session["uid"]
        data1 = Job.objects.all()

        return render(request,"jobportal/job.html",{"res":"data inserted succesfully","d":Job.objects.all()})
    else:
        return redirect("clogin")

def clogin(request):
    if request.method=="POST":
        r = Registration.objects.filter(email=request.POST["email"],password=request.POST["password"])
        if r.count()>0:
            request.session['uid']=request.POST["email"]
            if request.POST["chk"]:
                res= HttpResponse(status=302)
                res.set_cookie('ukey',request.POST["email"])
                res.set_cookie('upass',request.POST["password"])
                res['Location'] ='resume'
                return res
            else:
                return render(request,"jobportal/clogin.html",{"res":"invalid user id password"})
    else:
        c1=""
        c2=""
        if request.COOKIES.get('ukey'):
          c1=request.COOKIES["ukey"]
          c2=request.COOKIES["upass"]
    return render(request,"jobportal/clogin.html",{"email":c1,"password":c2})


def candidate(request):
    if (request.session.has_key('uid')):
        suid=request.session['uid']
        job = Jobinfo.objects.all()
        if request.method=="POST":
            s = Candidate(email =request.POST["txtemail"],jobid=request.POST["ddljob"],applydate=request.POST["applydate"],
            cname=request.POST["txtcandidate"])
            s.save()
            return render(request,"jobportal/candidate.html",{"res":job,"msg":"data inserted successsfully"})
        return render(request,"jobportal/candidate.html",{"res":job,"jid":(request.GET["q"])})    

def registration(request):
    Qulification=["10th","12th","diploma","graduation","post graduation"]
    if request.method=="POST":
        r = Registration(email=request.POST["email"],password=request.POST["password"],
        mobileno =request.POST["mobileno"],technology=request.POST["technology"],
        candidatetype=request.POST["candidatetype"],higherquli=request.POST["education"])
        r.save()
        return render(request,"jobportal/registration.html",{"data": Qulification,"data1":"registration successsfully"})
    return render(request,"jobportal/registration.html",{"data":Qulification})

def hlogin(request):
    if request.method=="POST":
        r = Registration.objects.filter(email=request.POST["email"],password=request.POST["password"])
        if r.count()>0:
            request.session['uid']=request.POST["email"]
            if request.POST["chk"]:
                res= HttpResponse(status=302)
                res.set_cookie('ukey',request.POST["email"])
                res.set_cookie('upass',request.POST["password"])
                res['Location'] ='jobcreate'
                return res
            else:
                return render(request,"jobportal/hlogin.html",{"res":"invalid user id password"})
    else:
        c1=""
        c2=""
        if request.COOKIES.get('ukey'):
          c1=request.COOKIES["ukey"]
          c2=request.COOKIES["upass"]
    return render(request,"jobportal/hlogin.html",{"email":c1,"password":c2})

def logout(request):
   res = HttpResponse(status=302)
   res.delete_cookie('ukey',"/")
   res.delete_cookie('upass',"/")
   del request.session["uid"]
   res['Location']='clogin'
   return res 

def home(request): 
    return render(request,"jobportal/home.html")

def hrreg(request):
    
    if request.method=="POST":
        r = HrReg(email=request.POST["email"],password=request.POST["password"],
        mobileno =request.POST["mobileno"],companyname=request.POST["companyname"])
        r.save()
        return render(request,"jobportal/hrreg.html",{"data1":"registration successsfully"})
    return render(request,"jobportal/hrreg.html")

class JobinfoCreate(CreateView):
    model = Jobinfo
    fields = ['jobtitle', 'jobdescription','experience','uploadimage','technology','postdate','duedate']
    success_url='/jobportal/joblist'
    
class JobinfoList(ListView):
   
    # specify the model for list view
    model = Jobinfo
    
class JobinfoDetail(DetailView):
  
  model = Jobinfo   # Job.objects.all()  




class JobinfoUpdate(UpdateView):
    model = Jobinfo
    fields = ['jobtitle','jobdescription','experience','uploadimage','technology','postdate','duedate']
    success_url ='/jobportal/joblist'


class JobinfoDelete(DeleteView):
    model = Jobinfo
    success_url = '/jobportal/joblist'

def resume(request):
    r=None
    STATE =['Andhra Pradesh','Arunachal Prades','Assam','Bihar','Chhattisgarh','Goa',
    'Gujarat',' Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka', 
    'Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland',
    'Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Uttar Pradesh','Tripura','west bengal']
   
   
    Branch=["select","  ","General","mathematics","Biology","Automobile Engineering","Computer Science","Electronics & Communication","Agricultural Engineering","Architectural Engineering","information Technology","Civil Engineering"]
    
    Year=['select',' ','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']

    Course=['select',' ','10','12','DIPLOMA','Graduation','PostGraduation','Phd']
    if request.method=="POST":
        r = Resume(name=request.POST["name"],gender=request.POST["txt5"],locality =request.POST["locality"],
            city=request.POST["city"],pin=request.POST["pin"],state=request.POST["state"],mobile=request.POST["mnumber"],
            email=request.POST["gmail"],job_city=request.POST["jobcity"],Address=request.POST["txt11"],linkedin=request.POST["txt12"],
            objective=request.POST["txt13"],workexperience=request.POST["txt14"],hsc=request.POST["txt22"],subject=request.POST["txt23"],
            passingyear=request.POST["txt24"],percentage=request.POST["txt44"],univercity=request.POST["txt34"],diploma=request.POST["txt25"],
            dbranch=request.POST["txt26"],dpassingyear=request.POST["txt27"],dpercentage=request.POST["txt28"],dunivercity=request.POST["txt38"],
            degree=request.POST["txt29"],gbranch=request.POST["txt30"],gpassingyear=request.POST["txt31"],gpercentage=request.POST["txt32"],
            gunivercity=request.POST["txt39"],pbranch=request.POST["txt34"],ppassingyear=request.POST["txt35"],postgraduation=request.POST["txt33"],
            ppercentage=request.POST["txt36"],punivercity=request.POST["txt40"],itskills=request.POST["txt21"],projects=request.POST["txt15"],
            trainings=request.POST["txt16"],hobbies=request.POST["txt17"],declaration=request.POST["txt18"],Date=request.POST["txt19"],
            sname=request.POST["txt20"])
        r.save()
        return render(request,"jobportal/show.html",{"y":Year,"b":Branch,"c":Course,"data":STATE,"d":Resume.objects.filter(id=r.id)})
    return render(request,"jobportal/resume.html",{"y":Year,"b":Branch,"c1":Course,"data":STATE,"d":Resume.objects.all()})


def show(request):
    return render(request,"jobportal/show.html",{"d":Resume.objects.all})

def jobinfo(request):
    
    if request.method=="POST":
        r = Jobinfo(jobtitle=request.POST["title"],experience=request.POST["experience"],
       jobdescription =request.POST["description"],uploadimage=request.POST["image"],
       technology=request.POST["technology"],postdate=request.POST["postdate"],
       duedate =request.POST["duedate"])
        r.save()
        return render(request,"jobportal/job.html",{"res":Jobinfo.objects.all()})
    return render(request,"jobportal/jobinfo.html",{"res":Jobinfo.objects.all()})

# Create your views here.
