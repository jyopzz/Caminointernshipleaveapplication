from . import views
from django.urls import URLPattern, path
from django.conf import urls



urlpatterns =[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('login/logged/',views.logged,name='logged'),

    #admin urls start
    path('login/logged/admindash/',views.admindash,name='admindash'),
    path('login/logged/admindash/empdetails/addemployee/',views.addemployee,name='addemployee'),
    path('login/logged/admindash/empdetails/',views.empdetails,name='empdetails'),
    path('login/logged/admindash/leavedetails/',views.leavedetails,name='leavedetails'),
    path('login/logged/admindash/addadmin/',views.addadmin,name='addadmin'),
    
    
    #admin urls end

    #employee urls start
    path('login/logged/empdash/',views.empdash,name='empdash'),
    path('login/logged/empdash/leaveapply/',views.leaveapply,name='leaveapply'),
    path('login/logged/empdash/leavestatus/',views.leavestatus,name='leavestatus'),
    #employee urls start

    # admin logout urls start
    path('login/logged/admindash/logout/',views.logout,name='logout'),
    path('login/logged/admindash/empdetails/logout/',views.logout,name='logout'),
    path('login/logged/admindash/leavedetails/logout/',views.logout,name='logout'),
    path('login/logged/admindash/empdetails/addemployee/logout/',views.logout,name='logout'),
    path('login/logged/admindash/addadmin/logout/',views.logout,name='logout'),
    # admin logout urls end

    # employee logout urls start
     path('login/logged/empdash/logout/',views.logout,name='logout'),
     path('login/logged/empdash/leaveapply/logout/',views.logout,name='logout'),
     path('login/logged/empdash/leavestatus/logout/',views.logout,name='logout'),
    # employee logout urls end

    #redirecting admin urls starting
    path('login/logged/admindash/empdetails/admindash1/',views.admindash1,name='admindash1'),
    path('login/logged/admindash/addadmin/admindash/',views.admindash1,name='admindash1'),
    path('login/logged/admindash/empdetails/addemployee/admindash1/',views.admindash1,name='admindash1'),
    path('login/logged/admindash/empdetails/addemployee/empdetails1/',views.empdetails1,name='empdetails1'),
    path('login/logged/admindash/empdetails/addemployee/leavedetails1/',views.leavedetails1,name='leavedetails1'),
    path('login/logged/admindash/empdetails/leavedetails1/',views.leavedetails1,name='leavedetails1'),
    path('login/logged/admindash/leavedetails/admindash1/',views.admindash1,name='admindash1'),
    path('login/logged/admindash/leavedetails/empdetails1/',views.empdetails1,name='empdetails1'),
    path('login/logged/admindash/leavedetails/leaveapprove1/<int:i>/',views.leaveapprove1,name='leaveapprove1'),
    path('leaveapprove/<int:i>/',views.leaveapprove,name='leaveapprove'),
    path('login/logged/admindash/leavedetails/leavereject1/<int:i>/',views.leavereject1,name='leavereject1'),
    path('leavereject/<int:i>/',views.leavereject,name="leavereject"),
    #redirecting admin urls ending

    #redirecting emp urls starting
    path('login/logged/empdash/empdash1/',views.empdash1,name='empdash1'),
    path('login/logged/empdash/leaveapply/leaveapply1/',views.leaveapply1,name='leaveapply1'),
    path('login/logged/empdash/leavestatus/leavestatus1/',views.leavestatus1,name='leavestatus1'),
    path('login/logged/empdash/leaveapply/empdash1/',views.empdash1,name='empdash1'),
    path('login/logged/empdash/leaveapply/leavestatus1/',views.leavestatus1,name='leavestatus1'),
    path('login/logged/empdash/leavestatus/empdash1/',views.empdash1,name='empdash1'),
    path('login/logged/empdash/leavestatus/leaveapply1/',views.leaveapply1,name='leaveapply1'),


    #redirecting emp urls ending

    #database connecting urls starting
    path('login/logged/empdash/leaveapply/empleave',views.empleave,name='empleave'),
    path('login/logged/admindash/addadmin/admindata',views.admindata,name='admindata',)
    


    #database connecting urls starting
    
    

    
]