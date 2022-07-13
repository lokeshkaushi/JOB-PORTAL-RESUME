from django.db import models
from django.db import models
class Job(models.Model):
    jobtitle = models.CharField(max_length=50)
    jobdiscription = models.CharField(max_length=50)

class Candidate(models.Model):
    email= models.CharField(max_length=50)
    jobid = models.CharField(max_length=50)
    applydate = models.CharField(max_length=50)
    cname = models.CharField(max_length=50)


class Registration(models.Model):
    email =models.CharField(max_length=100)
    password =models.CharField(max_length=100)
    mobileno =models.CharField(max_length=100)
    technology =models.CharField(max_length=100)
    candidatetype =models.CharField(max_length=100)
    higherquli =models.CharField(max_length=100)

class HrReg(models.Model):
    email =models.CharField(max_length=100)
    password =models.CharField(max_length=100)
    mobileno =models.CharField(max_length=100)
    companyname =models.CharField(max_length=100)
    
class Jobinfo(models.Model):
    jobtitle =models.CharField(max_length=100)
    experience =models.CharField(max_length=100)
    jobdescription =models.CharField(max_length=100)
    uploadimage =models.CharField(max_length=100)
    technology =models.CharField(max_length=100)
    postdate =models.CharField(max_length=100)
    duedate =models.CharField(max_length=100)

STATE_CHOICE = [
    ( 'Andhra Pradesh','Andhra Pradesh'),
    ( 'Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    (' Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    (' Haryana','Haryana'),
    (' Himachal Pradesh','Himachal Pradesh'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Jharkhand','Jharkhand') ,
    ('Karnataka','Karnataka'), 
    ('Kerala','Kerala'),
    ('Madhya Pradesh',' Madhya Pradesh'),
    ('Maharashtra',' Maharashtra'),
    ('Manipur',' Manipur'),
    ('Meghalaya',' Meghalaya'),
    ('Mizoram',' Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'), 
    ('Tamil Nadu','Tamil Nadu'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Tripura','Tripura'),
    ('west bengal','west bengal'),
]


class Resume(models.Model):
    name = models.CharField(max_length=100,default="")
    gender = models.CharField(max_length=100,default="")
    locality = models.CharField(max_length=100,default="")
    city = models.CharField(max_length=100,default="")
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE,max_length=50,default="")
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city =models.CharField(max_length=100,default="")
    Address = models.CharField(max_length=50,default=' ')
    linkedin = models.CharField(max_length=100,default="")
    objective = models.CharField(max_length=100,default="")
    workexperience = models.CharField(max_length=100,default="")
    
    hsc = models.CharField(max_length=50,default="")
    percentage = models.CharField(max_length=100,default="")
    subject = models.CharField(max_length=100 ,default="")
    passingyear = models.CharField(max_length=100,default="")
    course = models.CharField(max_length=100 ,default="")
    univercity = models.CharField(max_length=100,default="")
    diploma = models.CharField(max_length=50,default="")
    dpercentage = models.CharField(max_length=100,default="")
    dbranch = models.CharField(max_length=100 ,default="")
    dpassingyear = models.CharField(max_length=100 ,default="")
    dcourse = models.CharField(max_length=100 ,default="")
    dunivercity = models.CharField(max_length=100,default="")
    degree = models.CharField(max_length=50,default="")
    gpercentage = models.CharField(max_length=100 ,default="")
    gbranch = models.CharField(max_length=100 ,default="")
    gpassingyear = models.CharField(max_length=100 ,default="")
    gcourse = models.CharField(max_length=100 ,default="")
    gunivercity = models.CharField(max_length=100,default="")
    ppassingyear = models.CharField(max_length=50 ,default="")
    ppercentage = models.CharField(max_length=100,default="")
    pbranch = models.CharField(max_length=100 ,default="")
    postgraduation = models.CharField(max_length=100 ,default="")
    punivercity = models.CharField(max_length=100 ,default="")
    itskills = models.CharField(max_length=100,default="")
    projects = models.CharField(max_length=100,default="")
    trainings = models.CharField(max_length=100,default="")
    hobbies = models.CharField(max_length=100,default="")
    declaration = models.CharField(max_length=100,default='')
    Date = models.CharField(max_length=100 ,default="")
    sname = models.CharField(max_length=100,default="")
    