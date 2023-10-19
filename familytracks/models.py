from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
# create meep model
class Meep(models.Model):
	user = models.ForeignKey(
		User, related_name="meeps", 
		on_delete=models.DO_NOTHING
		)
	body = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	likes = models.ManyToManyField(User, related_name="meep_like", blank=True)


	# Keep track or count of likes
	def number_of_likes(self):
		return self.likes.count()



	def __str__(self):
		return(
			f"{self.user} "
			f"({self.created_at:%Y-%m-%d %H:%M}): "
			f"{self.body}..."
			)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self",
                                     related_name="followed_by",
                                     symmetrical=False,
                                     blank=True)
    date_modified = models.DateTimeField(User, auto_now=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images")
    
    def __str__(self):
        return self.user.username

#create profile when new user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
        # have the user follow themselves
        instance.profile.follows.set([instance.profile.id])
        instance.profile.save()
        

post_save.connect(create_profile, sender=User)