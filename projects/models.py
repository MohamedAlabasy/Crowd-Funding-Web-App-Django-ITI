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
        return self.project

#=======================================================================================#
#			                            comments                                     	#
#=======================================================================================#
class Comments(models.Model):
    comment = models.TextField(blank=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.user} on {self.project}")

#=======================================================================================#
#			                            Replies                                     	#
#=======================================================================================#
class Replies(models.Model):
    replie = models.TextField(blank=True)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.user} on {self.comment}")

#=======================================================================================#
#			                            Reports                                     	#
#=======================================================================================#
class Reports(models.Model):
    reason = models.TextField(blank=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return (f"{self.project} {self.comment} by {self.user}")

#=======================================================================================#
#			                            Donations                                     	#
#=======================================================================================#
class Donations(models.Model):
    paid_up = models.TextField(blank=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.user} Donate to {self.project}")
    
#=======================================================================================#
#			                              Tags                                         	#
#=======================================================================================#
class Tags(models.Model):
    name = models.CharField(max_length=250, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
