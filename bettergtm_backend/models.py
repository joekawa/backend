from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#* A USER CAN...
#* Login, Create Release Tasks, Assign Tasks to Team Members
#* Update or edit release actiivities, Create a Release, Open a Release
#* Share a release, Close a release, Approve release activities
#* Be assigned to a release, Be assigned to a team, Be assigned to a role
#* Be assigned release activities, Process release activities
#* BE PART OF A TEAM BUT MUST BE ASSIGNED TO A CUSTOMER

class Customer(models.Model):
  name = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  zip_code = models.CharField(max_length=100, null=True)

#! NEED TO ADD CUSTOMER KEY HERE
class Team(models.Model):
  name = models.CharField(max_length=100)
  short_name = models.CharField(max_length=10, null=True) #* Short name for team i.e. PMM for Product Marketing Managers
  description = models.TextField(null=True)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
  def __str__(self):
    return self.name



#* Status indicates the current state of a release.
#* Will need to have approval before it's released to document viewers
#* Document viewers are people like sales or customer success who
#* can see all the outputs after they've been approved
class Status(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(null=True)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.name


#* Release Type is a collection of release activities
class ReleaseType(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(null=True)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.name

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
  company = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)


#* Releases are...
#* Business milestones that impact a product
#* New features, bug fixes, or other changes to a product
#* revenue drivers, improved customer experience, etc.
#* requires envolvment, planning, and execution outside of the product/engineering team

class Release(models.Model):
  name = models.CharField(max_length=100)
  release_date = models.DateField()
  description = models.TextField(null=True)
  status = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.name


#* Release Tasks are...
#* Specific tasks that need to be completed to complete a release
#* Tasks can be assigned to a user or team
#* Expected to have certain outputs
#* Must be completed by a certain date

class ReleaseActivity(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(null=True)
  due_date = models.DateField()
  status = models.CharField(max_length=100) #*NEED TO SET AN ENUM FOR STATUS
  assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                                  related_name="user_assigned_to")
  release = models.ForeignKey(Release, on_delete=models.CASCADE)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="user_created_by")
  team_assignment = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
  release_type = models.ForeignKey(ReleaseType, on_delete=models.CASCADE,
                                   null=True)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.name


class Goal(models.Model):
  release = models.ForeignKey(Release, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.TextField(null=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  goal_value = models.CharField(max_length=100, null=True)
  goal_type = models.CharField(max_length=100, null=True)
  actual_value = models.CharField(max_length=100, null=True)
  goal_due_date = models.DateField(null=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.name


class Output(models.Model):
  release_activity = models.ForeignKey(ReleaseActivity, on_delete=models.CASCADE)
  name = models.CharField(max_length=100, null=True)
  description = models.TextField(null=True)
  file = models.FileField((""), upload_to=None, max_length=100)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)


