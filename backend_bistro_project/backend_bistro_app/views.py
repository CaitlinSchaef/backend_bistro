from rest_framework import viewsets


from .models import *
#can do .models as opposed to a more explicit path because we're in same folder


from .serializers import *
# we are going to use the serialized data here so we need it all

# Create your views here.

# class StudentViewSet(viewsets.ModelViewSet):
#    #two things going on that are pretty much always there, queryset based on what we want to look at (which you can filter down but we won't here)
#    #this is all the students
#    queryset = Student.objects.all()
#    #and what serializer to use, it will be the student serializer
#    #this is basically the endpoint, but we need to register it in the url
#    serializer_class = StudentSerializer
