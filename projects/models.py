from django.db import models
from django.utils import timezone


#=======================================================================================#
#			                            Categone                                    	#
#=======================================================================================#


class Categories(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


#=======================================================================================#
#			                            Project                                     	#
#=======================================================================================#


class Projects(models.Model):
    title = models.CharField(max_length=250, unique=True)
    details = models.TextField(blank=True)
    rate = models.IntegerField(null=True)
    total_target = models.IntegerField()
    current_donation = models.IntegerField(default=0)
    start_campaign = models.DateTimeField(default=timezone.now)
    end_campaign = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    selected_at_by_admin = models.DateTimeField(null=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
