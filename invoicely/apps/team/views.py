from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from rest_framework import viewsets
from .models import Team
from .serializers import TeamSerializer
from django.core.exceptions import PermissionDenied
# Create your views here.

class TeamViewSet(viewsets.ModelViewSet):
    queryset= Team.objects.all()
    serializer_class = TeamSerializer

    def get_queryset(self):
        #queries all the teams created by the authenticated user
        teams = self.request.user.teams.all()

        if not teams:
            Team.objects.create(name='',org_number = '',created_by =self.request.user)

        return self.queryset.filter(created_by=self.request.user)
    #provided by the mixin classes
    def perform_create(self,serialzer):
        serialzer.save(created_by=self.request.user)
        


    def perform_update(self,serializer):
        #get_object is provided by the Returns an object 
        #instance that should be used for detail views
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied("Wrong Object owne!")
        serializer.save()



