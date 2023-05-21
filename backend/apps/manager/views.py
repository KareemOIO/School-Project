# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StudentsFilter
from .serializers import StudentsFilterSerializer

class StudentsFilterAPIView(APIView):
    def post(self, request):
        serializer = StudentsFilterSerializer(data=request.data)
        if serializer.is_valid():
            filtering_level = serializer.validated_data.get('FilteringLevel')
            student_specialized = serializer.validated_data.get('StudentSpecilized')
            student_level = serializer.validated_data.get('StudentLevel')
            student_class = serializer.validated_data.get('StudentClass')

            # Perform the filtering logic based on the received parameters
            filtered_students = StudentsFilter.objects.filter(
                FilteringLevel=filtering_level,
                StudentSpecilized=student_specialized,
                StudentLevel=student_level,
                StudentClass=student_class
            )

            # Serialize the filtered results
            filtered_students_serializer = StudentsFilterSerializer(filtered_students, many=True)

            return Response(filtered_students_serializer.data)
        
        return Response(serializer.errors, status=400)
