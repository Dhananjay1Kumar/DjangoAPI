from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from .models import Employee

class EmployeeList(APIView):

    def get(self, request):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # emp = request.data # json format
        serializer = EmployeeSerializer(data=request.data)  # dict format
        if serializer.is_valid():
            serializer.save()       # store into db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):

    def get_object_by_id(self, id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        else:
            return emp

    def get(self, request, id):
        emp = self.get_object_by_id(id)

        if emp is None:
            return Response("Record not available", status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data, status= status.HTTP_200_OK)

    def put(self, request, id):
        emp = self.get_object_by_id(id)
        if emp is None:
            return Response("This id record does not exist",status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = EmployeeSerializer(emp,data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK  )

            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        emp = self.get_object_by_id(id)

        if emp is None:
            return Response("This id record does not exist",status=status.HTTP_404_NOT_FOUND)

        else:
            del emp
            return Response("Record Deleted", status=status.HTTP_204_NO_CONTENT)