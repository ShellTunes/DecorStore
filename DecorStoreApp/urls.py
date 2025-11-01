from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
# from DecorStoreApp.classes.clientdetails import *
# from DecorStoreApp.classes.staffdetails import *
# from DecorStoreApp.classes.projects import *
from DecorStoreApp.classes.Items import *
from DecorStoreApp.classes.savedata import *
from DecorStoreApp.classes.pdfquotes import *
from DecorStoreApp.classes.stockreport import *
from DecorStoreApp.classes.ProjectReport import *
from . import views


urlpatterns = [
    # path('addclient/', addclient.as_view()),
    # path('updateclient/<int:id>/',updateclient.as_view()),
    # path('deleteclient/<int:id>/',clientdelete.as_view()),
    # path('createstaff/', createstaff.as_view()),
    # path('updatestaff/<int:id>/',editstaff.as_view()),
    # path('deletestaff/<int:id>/',staffdelete.as_view()),
    # path('createprojects/', createprojectdetails.as_view()),
    # path('updateprojects/<int:id>/',updateprojects.as_view()),
    # path('deleteprojects/<int:id>/',deleteprojects.as_view()),
    path('getItemRate/<int:id>/', getItemRate.as_view()),
    path('print/quotepdf/<int:id>/', printPDFView.as_view(), name='site-print-pdf'),
    path('stockreport', StockReportView.as_view(), name='stockreport'),
    path('SaveData/', getSavedata.as_view()),
    # path('projectReportshow', ProjectReportFunc, name='projectReportshow'),
    path('projectReport', ProjectReportFuncShow.as_view(), name='projectReport'),
    path('get_transporter_contact/', views.get_transporter_contact, name='get_transporter_contact'),
]


