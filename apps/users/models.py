from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class User_Manager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if postData['first_name'] == '':
			errors['first_name'] = 'First name cannot be blank'
		if postData['last_name'] == '':
			errors['last_name'] = 'Last name cannot be blank'
		if postData['email'] == '':
			errors['email'] = 'Email cannot be blank'
		if not EMAIL_REGEX.match(postData['email']):
			errors['email'] = 'Invalid Email Address'
		print(errors)
		return errors

	# def update_user(self, postData):
		# user = User.objects.get(id=id)
		# user.first_name = postData['first_name']
		# user.last_name = postData['last_name']
		# user.email = postData['email']
		# user.save()


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = User_Manager()

	def __repr__(self):
		return f"<User object: {self.first_name} {self.last_name} {self.email}>"




#