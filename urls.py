from django.urls import path
from .import views
from .views import JobinfoList
from .views import JobinfoDetail
from .views import JobinfoCreate,JobinfoUpdate,JobinfoDelete 


urlpatterns=[
     path('jobinfo',views.jobinfo,name='jobinfo'),
     path('resume',views.resume,name='resume'), 
     path('show',views.show,name='show'),
     path('hrreg',views.hrreg,name='hrreg'),
     path('job',views.job,name='job'),
     path('clogin',views.clogin,name='clogin'),
     path('candidate',views.candidate,name='candidate'),
     path('registration',views.registration,name='registration'),
     path('hlogin',views.hlogin,name='hlogin'),
     path('logout',views.logout,name='logout'),
     path('home',views.home,name='home'),
     path('jobcreate',JobinfoCreate.as_view()),
     path('joblist', JobinfoList.as_view()),
     path('<pk>/',JobinfoDetail.as_view()),
     path('<pk>/jupdate',JobinfoUpdate.as_view()),
     path('<pk>/jdelete',JobinfoDelete.as_view()),
]