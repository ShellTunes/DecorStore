# from urllib import response

# from DecorStoreApp.serializers import ProjectsSerializer
# from ..models import *
# from DecorStoreApp.projectmodules import *


# class createprojectdetails(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     def post(self, request, format=None):
#         type_of_work = request.data['type_of_work']
#         client_id = request.data['client_id']
#         staff_id = request.data['staff_id']
#         diagram_status = request.data['diagram_status']
#         diagram_file = request.data['diagram_file']
#         quote_status = request.data['quote_status']
#         quote_file = request.data['quote_file']
#         finalize = request.data['finalize']
#         dispatch_status = request.data['dispatch_status']
#         staffid = request.data['staffid']
#         total_sq_ft = request.data['total_sq_ft']
#         work_completion_status = request.data['work_completion_status']
#         invoice_status = request.data['invoice_status']
#         invoice_file = request.data['invoice_file']
#         payment_status = request.data['payment_status']


#         try:
#             addprojects = Projects(
#                 type_of_work = type_of_work,
#                 client_id_id = client_id,
#                 measurement_staff_id = staff_id,
#                 diagram_status = diagram_status,
#                 diagram_file = diagram_file,
#                 quote_status = quote_status,
#                 quote_file = quote_file,
#                 finalize = finalize,
#                 dispatch_status = dispatch_status,
#                 installation_staff_id = staffid,
#                 total_sq_ft = total_sq_ft,
#                 work_completion_status = work_completion_status,
#                 invoice_status = invoice_status,
#                 invoice_file = invoice_file,
#                 payment_status = payment_status
#             )

#             addprojects.save()

#             resdata = {
#                 'type_of_work': addprojects.type_of_work,
#                 'client_id': addprojects.client_id_id,
#                 'measurement_staff': addprojects.measurement_staff_id,
#                 'diagram_status': addprojects.diagram_status,

#             }

#             responseData = {
#                 'error' : False,
#                 'data' : resdata,
                
#             }
#             return Response(responseData)
        
#         except:
#             responseData = {
#                 'error' : True,
#                 'data' : {},
                
#             }
#             return Response(responseData)




# class updateprojects(APIView):
#     def put(self, request, id):
#         obj = Projects.objects.get(id=id)
#         projectserializer = ProjectsSerializer(obj, data=request.data)
        

#         if projectserializer.is_valid():
#             projectserializer.save()
            

#             content = {
#                 'error' : False,
#                 'message' : 'success',
#                 'data' : projectserializer.data
#             }

#             return Response(content)
#         else:
#             return Response(projectserializer.errors)



# class deleteprojects(APIView):
#     def delete(self, request, id):
#         try:
#             deleteprojects = Projects.objects.get(id= id)
#             deleteprojects.delete()
#             responseData = {
#                 'error' : False,
#                 'message' : "Deleted Successfully"
#             }

#             return Response(responseData)

#         except:
#             responseData = {
#                 'error' : True,
#                 'message' : "Not Modified"
#             }

#             return Response(responseData)