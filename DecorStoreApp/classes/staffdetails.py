# from urllib import response
# from ..models import *
# from DecorStoreApp.projectmodules import *




# class createstaff(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     def post(self, request, format=None):
#         name = request.data['name']
#         phone = request.data['phone']
#         staff_type = request.data['staff_type']


#         try:
#             addstaff = Staff(
#                 name = name,
#                 phone = phone,
#                 staff_type = staff_type
#             )
#             addstaff.save()

#             resdata = {
#                 'id': addstaff.id,
#                 'name': addstaff.name,
#                 'phone': addstaff.phone,
#                 'type': addstaff.staff_type
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



# class editstaff(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     def put(self, request, id, format=None):
        
#         name = request.data['name']
        
#         phone = request.data['phone']
        
#         staff_type = request.data['staff_type']
        
#         try:
#             clientupdate = Staff.objects.get(id=id)
           
#             clientupdate.name = name

            
#             clientupdate.phone = phone

            
#             clientupdate.staff_type = staff_type

#             clientupdate.save()
            
#             responseData = {
#                 'error' : False,
#                 'message': "Updated Successfully"
#             }
#             return Response(responseData)


#         except:
#             responseData = {
#                 'error' : True,
#                 'message' : "Not Modified"
#             }

#             return Response(responseData)



# class staffdelete(APIView):
#     def delete(self, request, id, format=None):
#         try:
#             deletestaff = Staff.objects.get(id= id)
#             deletestaff.delete()
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