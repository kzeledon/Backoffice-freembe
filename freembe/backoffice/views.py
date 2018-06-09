from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests


def index(request):
	request.session['Login'] = True
	if request.method == 'POST':
		email = request.POST.get('email')
		password = str(request.POST.get('password'))

		token = login(email,password)

		if token == False:
			return render(request, 'backoffice/index.html')
		else:
			data = {'Users':[],'Categorias':[],'Sub':[],'Anuncios':[], 'Token': token}
			users = get_user(token)
			categories = get_categories(token)
			subcategories = get_subcategories(token)
			anuncios = get_announcements(token)

			data['Users'] = users
			data['Categorias'] = categories
			data['Sub'] = subcategories
			data['Anuncios'] = anuncios

			return render(request, 'backoffice/backoffice.html', data)
	else:
		return render(request, 'backoffice/index.html')

def backoffice(request):
	return render(request, 'backoffice/index.html')	

def login(email, password):
	r = requests.post('https://freembe.herokuapp.com/api/authenticate?email='+email+'&password='+password)
	if r.status_code == 200:
		data = r.json()
		if data['role'] == 'Administrator':
			return data['auth_token']
		else:
			return False
	else:
		return False

def get_user(token):
	r = requests.get('https://freembe.herokuapp.com/api/users',  headers={'Authorization': token})
	return r.json()

def get_categories(token):
	r = requests.get('https://freembe.herokuapp.com/api/categories',  headers={'Authorization': token})
	return r.json()

def get_subcategories(token):
	r = requests.get('https://freembe.herokuapp.com/api/subcategoriesxcategories',  headers={'Authorization': token})
	return r.json()

def get_announcements(token):
	r = requests.get('https://freembe.herokuapp.com/api/announcements/',  headers={'Authorization': token})
	return r.json()
