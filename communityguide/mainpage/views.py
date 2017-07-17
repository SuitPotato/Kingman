from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mainpage.models import Department, Utility, Important, Education, Restaurant, Attraction

# Import all the models

# Create your views here.


def index(request):
	return render(request, 'mainpage/index.html')
	
def explore(request):
	return render(request, 'mainpage/explore.html')

# Default is page 1, unless given another page through a url or href
def departments(request, page=1):

	department_list = Department.objects.all()
	
	paginator = Paginator(department_list, 9)
	
	try: 
		departments = paginator.page(page)
	except PageNotAnInteger:
		# Query the first nine or page 1
		departments = paginator.page(9)
	except EmptyPage:
		departments = paginator.page(paginator.num_pages)
	context = {"departments": departments, "page": page}
	return render(request, 'mainpage/departments.html', context)
	
def utilandservice(request, page=1):
	
	utility = Utility.object.all()
	paginator = Paginator(utility, 9)
	
	try: 
		util = paginator.page(page)
	except PageNotAnInteger:
		# Query the first nine or page 1
		util = paginator.page(9)
	except EmptyPage:
		util = paginator.page(paginator.num_pages)
	context = {"utilities": utilities, "page": page}
		
		
	return render(request, 'mainpage/utilandservice.html', context)

def important(request, page=1):

	important = Important.object.all()
	paginator = Paginator(important, 9)
	
	try: 
		port = paginator.page(page)
	except PageNotAnInteger:
		# Query the first nine or page 1
		port = paginator.page(9)
	except EmptyPage:
		port = paginator.page(paginator.num_pages)
	context = {"important": important, "page": page}

	return render(request, 'mainpage/important.html',context)
	
def lodgecamprv(request,page=1):

	lcrv = LCRV.object.all()
	paginator = Paginator(lcrv, 9)
	
	try: 
		j = paginator.page(page)
	except PageNotAnInteger:
		# Query the first nine or page 1
		j = paginator.page(9)
	except EmptyPage:
		j = paginator.page(paginator.num_pages)
	context = {"lodge": lodge, "page": page,}

	return render(request, 'lodgecamprv.html', context)
	
def education(request,page=1):

	education = Education.object.all()
	paginator = Paginator(utility, 9)
	
	try: 
		util = paginator.page(page)
	except PageNotAnInteger:
		# Query the first nine or page 1
		util = paginator.page(9)
	except EmptyPage:
		util = paginator.page(paginator.num_pages)
	context = {"utilities": utilities, "page": page}

	return render(request, 'education.html', context)
	
def restaurant(request,page=1):

	restaurant = Restaurant.objects.all()
	paginator = Paginator(restaurant, 9)
	
	try: 
		restaurants = paginator.page(page)
	except PageNotAnInteger:
		# Query the first nine or page 1
		restaurants = paginator.page(9)
	except EmptyPage:
		restaurants = paginator.page(paginator.num_pages)
	context = {"restaurant": restaurant, "page": page}

	return render(request, 'mainpage/restaurants.html', context)
	
	

def attractions(request,page=1):

	attractions = Attractions.object.all()
	paginator = Paginator(utility, 9)
	
	try: 
		att = paginator.page(page)
	except PageNotAnInteger:
		# Query the first nine or page 1
		util = paginator.page(9)
	except EmptyPage:
		util = paginator.page(paginator.num_pages)
	context = {"utilities": utilities, "page": page}

	return render(request, 'attractions.html', context)