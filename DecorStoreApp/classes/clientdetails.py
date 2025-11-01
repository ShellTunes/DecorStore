# from urllib import response
# from ..models import *
# from DecorStoreApp.projectmodules import *



# class addclient(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     def post(self, request, format=None):
#         firstname = request.data['firstname']
#         lastname =  request.data['lastname']
#         email  =  request.data['email']
#         phone_number =  request.data['phone_number']
#         building =  request.data['building']
#         street =  request.data['street']
#         landmark =  request.data['landmark']
#         city =  request.data['city']
#         zip =  request.data['zip']

#         try:
#             addclientdata = Client(
#                 firstname = firstname,
#                 lastname = lastname,
#                 email = email,
#                 phone_number = phone_number,
#                 building = building,
#                 street = street,
#                 landmark = landmark,
#                 city = city,
#                 zip = zip
#             )

#             addclientdata.save()


#             resdata = {
#                 'id': addclientdata.id,
#                 'name': str(addclientdata.firstname)+" "+str(addclientdata.lastname),
#                 'email': addclientdata.email,
#                 'phone': addclientdata.phone_number,
#                 'address': str(addclientdata.building)+", "+str(addclientdata.street)+", "+str(addclientdata.city)+", "+str(addclientdata.landmark)+"-"+str(addclientdata.zip)
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





# class updateclient(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     def put(self, request, id, format=None):
        
#         firstname = request.data['firstname']
        
#         lastname =  request.data['lastname']
        
#         email  =  request.data['email']
        
#         phone_number =  request.data['phone_number']
        
#         building =  request.data['building']
        
#         street =  request.data['street']
        
#         landmark =  request.data['landmark']
        
#         city =  request.data['city']
       
#         zip =  request.data['zip']
        

#         try:
#             updateclientdetails = Client.objects.get(id=id)
            
            
#             updateclientdetails.firstname = firstname
           
#             updateclientdetails.lastname = lastname
            
#             updateclientdetails.email = email
            
#             updateclientdetails.phone_number = phone_number
            
#             updateclientdetails.building = building
            
#             updateclientdetails.street = street
            
#             updateclientdetails.landmark = landmark
            
#             updateclientdetails.city = city
            
#             updateclientdetails.zip = zip

#             updateclientdetails.save()


            

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



# class clientdelete(APIView):
#     def delete(self, request, id, format=None):
#         try:
#             deleteclient = Client.objects.get(id= id)
#             deleteclient.delete()
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