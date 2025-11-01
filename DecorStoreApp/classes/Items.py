from django.http import JsonResponse
# from DecorStoreApp.serializers import ProjectsSerializer
from ..models import *
from DecorStoreApp.projectmodules import *
from django.views import View


class getItemRate(View):
    def get(self, request, id):
        try:
            item = ItemMaster.objects.get(id=id)
            # return the raw rate so existing frontend code (expects a number) continues to work
            return JsonResponse(item.Rate, safe=False)

        except ItemMaster.DoesNotExist:
            return JsonResponse("Invalid Request", safe=False, status=404)
        except Exception:
            # generic error
            return JsonResponse("Invalid Request", safe=False, status=500)