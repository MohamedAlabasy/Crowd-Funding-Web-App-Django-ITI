from django.db import models
from django.utils import timezone
from user.models import User


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
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#=======================================================================================#
#			                            Pictures                                     	#
#=======================================================================================#
class Pictures(models.Model):
    image = models.ImageField(max_length=255, upload_to="img/%y", null=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return self.image

#=======================================================================================#
#			                            comments                                     	#
#=======================================================================================#


class Comments(models.Model):
    comment = models.TextField(blank=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
