from django.db import models
from django.utils import timezone
from user.models import User
#=======================================================================================#
#			                            Categone                                    	#
#=======================================================================================#
class Categories(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


#=======================================================================================#
#			                            Project                                     	#
#=======================================================================================#
class Projects(models.Model):
    title = models.CharField(max_length=250, unique=True)
    details = models.TextField()
    rate = models.IntegerField()
    total_target = models.IntegerField()
    current_donation = models.IntegerField()
    start_campaign = models.DateTimeField(default=timezone.now)
    end_campaign = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    selected_at_by_admin = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    owner = models.ForeignKey(User,  on_delete=models.CASCADE)

    def __str__(self):
        return self.title


#=======================================================================================#
#			                            Pictures                                     	#
#=======================================================================================#
class Pictures(models.Model):
    image = models.ImageField(max_length=255, upload_to="img/%y")
    project = models.ForeignKey(
        Projects, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"/media/{self.image}"

#=======================================================================================#
#			                              Tags                                         	#
#=======================================================================================#
class Tags(models.Model):
    tag = models.CharField(max_length=250)
    project = models.ForeignKey(
        Projects, on_delete=models.CASCADE, related_name='tags')

    def __str__(self):
        return self.tag
    
    
#=======================================================================================#
#			                            comments                                     	#
#=======================================================================================#
class Comments(models.Model):
    comment = models.TextField()
    project = models.ForeignKey(
        Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.user.first_name} {self.user.last_name} on {self.project.title}")


#=======================================================================================#
#			                            Replies                                     	#
#=======================================================================================#
class Replies(models.Model):
    replie = models.TextField()
    comment = models.ForeignKey(
        Comments, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.user.first_name} {self.user.last_name} on Commint id = {self.comment.id}")


#=======================================================================================#
#			                            ReportsProject                                  #
#=======================================================================================#
class ReportsProject(models.Model):
    reason = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.user.first_name} {self.user.last_name} on report {self.project.title} "


#=======================================================================================#
#			                            ReportsComment                                 	#
#=======================================================================================#
class ReportsComment(models.Model):
    reason = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} on report id = {self.comment.id}"


#=======================================================================================#
#			                            Donations                                     	#
#=======================================================================================#
class Donations(models.Model):
    paid_up = models.IntegerField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.user} Donate to {self.project}")


#=======================================================================================#
#			                            Rates                                        	#
#=======================================================================================#
class Rates(models.Model):
    rate = models.IntegerField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.user} rate to {self.project}")
