from urllib import response
# from DecorStoreApp.serializers import ProjectsSerializer
from ..models import *
from DecorStoreApp.forms import *
# from DecorStoreApp.projectmodules import *
from django.http import HttpResponse
from django.views import View


class getSavedata(View):
    def post(self, request):

            try:
                if request.method == 'POST':
                    print("ALL POST DATA ", request.POST)
                    Gform = LineItemGlassForms(request.POST) 
                    Qform = QuoteForms(request.POST or None)
                    # Fform = LineItemFittingsForms(request.POST)
                   
                    Mform = LineItemMiscForms(request.POST)
                    print("POST REQ Quote DATA ", Qform)
                    print("POST REQ GLASS DATA ", Gform)
                    if Qform.is_valid() or Gform.is_valid() or Mform.is_valid(): 
                        
                        # id = form.cleaned_data['id']
                        
                        
                        # Fform.save()
                        Gform.save()
                        Mform.save()
                        obj = Qform.save()
                        print("FORM VALID" , obj.pk)
                        return HttpResponse(obj.pk )
                    
                    else:
                        # output form.errors here and figure out what fields aren't passing validation
                        return HttpResponse(json.dumps({'Error MEssaGe':Qform.errors}))

            except:
                responseData = {
                    'error' : True,
                    'message' : "Cound Not Find Item With ID"
                }
            context = {
                'Qform': Qform,
                'Gform': Gform,
                'Mform': Mform,
            }

            return Response("Invalid Request")