from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User


# populate user data in html with ORM
def all_users(request):
	if 'super_user_id' not in request.session:
		return redirect('/')
	return render(request, 'users/all_users.html', {'users': User.objects.all()})

# static page with form
def new_user(request):
	if 'super_user_id' not in request.session:
		return redirect('/')
	return render(request, 'users/new_user.html')

# process route for new user form
def create_user(request):
	if 'super_user_id' not in request.session:
		return redirect('/')
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.items():
			messages.error(request, error, extra_tags=tag)
		print('errors found')
		return redirect('users/new')
	else:
		print('no errors found')
		# User.objects.update_user(request.POST)
		User.objects.create(
			first_name = request.POST['first_name'],
			last_name = request.POST['last_name'],
			email = request.POST['email']
			)
		return redirect('users')

# dedicated page to a single user's info
def view_user(request, id):
	if 'super_user_id' not in request.session:
		return redirect('/')
	return render(request, 'users/view_user.html', {'users': User.objects.get(id=id)})

# open form on edit page to edit user info
def edit_user(request, id):
	if 'super_user_id' not in request.session:
		return redirect('/')
	return render(request, 'users/edit_user.html', {'users': User.objects.get(id=id)})

# update user route
def update_user(request, id):
	if 'super_user_id' not in request.session:
		return redirect('/')
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		# for tag, error in errors.iteritems():
		# 	messages.error(request, error, extra_tags=tag)
		print('errors found')
		return redirect(f'{id}/edit')
	else:
		print('no errors found')
		# User.objects.update_user(request.POST)
		user = User.objects.get(id=id)
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']
		user.save()
		return redirect('users')

# delete user from DB
def destroy_user(request, id):
	User.objects.get(id=id).delete()
	return redirect('/users')




#