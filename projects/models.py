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
#			                              Tags                                         	#
#=======================================================================================#


class Tags(models.Model):
    name = models.CharField(max_length=250, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#=======================================================================================#
#			                            Project                                     	#
#=======================================================================================#


class Projects(models.Model):
    title = models.CharField(max_length=250, unique=True)
    details = models.TextField(blank=True)
    rate = models.IntegerField(default=0)
    total_target = models.IntegerField()
    current_donation = models.IntegerField(default=0)
    start_campaign = models.DateTimeField(default=timezone.now)
    end_campaign = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    selected_at_by_admin = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    owner = models.ForeignKey(User,  on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title

#=======================================================================================#
#			                            Pictures                                     	#
#=======================================================================================#


class Pictures(models.Model):
    image = models.ImageField(max_length=255, upload_to="img/%y", null=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.title

#=======================================================================================#
#			                            comments                                     	#
#=======================================================================================#


class Comments(models.Model):
    comment = models.TextField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.user.first_name} {self.user.last_name} on {self.project.title}")

#=======================================================================================#
#			                            Replies                                     	#
#=======================================================================================#


class Replies(models.Model):
    replie = models.TextField()
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.user.first_name} {self.user.last_name} on Commint id = {self.comment.id}")

#=======================================================================================#
#			                            Reports                                     	#
#=======================================================================================#


class Reports(models.Model):
    reason = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, blank=True)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, blank=True)
    replie = models.ForeignKey(Replies, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        if self.project.title:
            result = f" {self.user.first_name} {self.user.last_name} on project {self.project.title} "
        elif self.comment.id:
            result = f" {self.user.first_name} {self.user.last_name} on comment id = {self.comment.id} "
        elif self.replie.id:
            result = f" {self.user.first_name} {self.user.last_name} on replie id = {self.replie.id} "
        return result

#=======================================================================================#
#			                            Donations                                     	#
#=======================================================================================#


class Donations(models.Model):
    paid_up = models.TextField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.user} Donate to {self.project}")
