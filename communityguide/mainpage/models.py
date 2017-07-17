from __future__ import unicode_literals

from django.db import models



class Department(models.Model):
	departmentID = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 55)
	phone = models.CharField(max_length = 14)
	fax = models.CharField(max_length = 14, null = True, blank = True)
	hours = models.CharField(max_length = 28, null = True, blank = True)
	link = models.CharField(max_length = 100, null = True, blank = True)
	description = models.CharField(max_length = 200, null = True, blank = True)
	# Address
	streetName = models.CharField(max_length = 40, null = True, blank = True)
	stateInfo = models.CharField(max_length = 40, null = True, blank = True)
	googleMaps = models.CharField(max_length = 700, null = True, blank = True)
	
	def __str__(self):
		return self.name
	
	
class Utility(models.Model):
	utilityID = models.AutoField(primary_key=True)
	
	CATEGORY = {
		(1, 'Electric and Gas'),
		(2, 'Propane'),
		(3, 'Water, Sewer, and Trash'),
		(4, 'Telephone'),
		(5, 'Internet Service Providers'),
		(6, 'Cable Service Providers'),
	}
	
	name = models.CharField(max_length = 55)
	phone = models.CharField(max_length = 14)
	fax = models.CharField(max_length = 14, null = True, blank = True)
	hours = models.CharField(max_length = 28, null = True, blank = True)
	link = models.CharField(max_length = 100, null = True, blank = True)
	description = models.CharField(max_length = 200, null = True, blank = True)
	category = models.IntegerField(choices=CATEGORY, default=1)
	streetName = models.CharField(max_length = 40, null = True, blank = True)
	stateInfo = models.CharField(max_length = 40, null = True, blank = True)
	googleMaps = models.CharField(max_length = 700, null = True, blank = True)
	
	def __str__(self):
		return self.name
	
class Important(models.Model):
	importantID = models.AutoField(primary_key = True)
	
	CATEGORY = {
		('1','Mohave County Offices'),
		('2','County Supervisors'),
		('3','State Offices'),
		('4','Federal Offices'),
		('5','Emergency Services'),
		('6','Job Services'),
	}
	
	name = models.CharField(max_length = 55)
	phone = models.CharField(max_length = 14)
	fax = models.CharField(max_length = 14, null = True, blank = True)
	hours = models.CharField(max_length = 28, null = True, blank = True)
	link = models.CharField(max_length = 100, null = True, blank = True)
	description = models.CharField(max_length = 200, null = True, blank = True)
	category = models.IntegerField(choices=CATEGORY, default=1)
	streetName = models.CharField(max_length = 40, null = True, blank = True)
	stateInfo = models.CharField(max_length = 40, null = True, blank = True)
	googleMaps = models.CharField(max_length = 700, null = True, blank = True)
	
	def __str__(self):
		return self.title
	
	
class Education(models.Model):
	schoolID = models.AutoField(primary_key=True)
	CATEGORY = {
		('1','Preschool'),
		('2','Elementary'),
		('3','Middle & High'),
	}
	
	name = models.CharField(max_length = 55)
	phone = models.CharField(max_length = 14)
	fax = models.CharField(max_length = 14, null = True, blank = True)
	hours = models.CharField(max_length = 28, null = True, blank = True)
	link = models.CharField(max_length = 100, null = True, blank = True)
	description = models.CharField(max_length = 200, null = True, blank = True)
	category = models.IntegerField(choices=CATEGORY, default=1)
	streetName = models.CharField(max_length = 40, null = True, blank = True)
	stateInfo = models.CharField(max_length = 40, null = True, blank = True)
	googleMaps = models.CharField(max_length = 700, null = True, blank = True)
	
	def __str__(self):
		return self.name
		
class Restaurant(models.Model):
	restaurantID = models.AutoField(primary_key=True)
	
	name = models.CharField(max_length = 55)
	phone = models.CharField(max_length = 14)
	fax = models.CharField(max_length = 14, null = True, blank = True)
	hours = models.CharField(max_length = 28, null = True, blank = True)
	link = models.CharField(max_length = 100, null = True, blank = True)
	description = models.CharField(max_length = 200, null = True, blank = True)
	# Address
	streetName = models.CharField(max_length = 40, null = True, blank = True)
	stateInfo = models.CharField(max_length = 40, null = True, blank = True)
	googleMaps = models.CharField(max_length = 700, null = True, blank = True)
	
	def __str__(self):
		return self.name
	
class Attraction(models.Model):
	attractionsID = models.AutoField(primary_key=True)

	name = models.CharField(max_length = 55)
	phone = models.CharField(max_length = 14)
	fax = models.CharField(max_length = 14, null = True, blank = True)
	hours = models.CharField(max_length = 28, null = True, blank = True)
	link = models.CharField(max_length = 100, null = True, blank = True)
	description = models.CharField(max_length = 200, null = True, blank = True)
	# Address
	streetName = models.CharField(max_length = 40, null = True, blank = True)
	stateInfo = models.CharField(max_length = 40, null = True, blank = True)
	googleMaps = models.CharField(max_length = 700, null = True, blank = True)
	
	def __str__(self):
		return self.name
		
class LodgeCampRV(models.Model):
	LCRVID = models.AutoField(primary_key=True)

	name = models.CharField(max_length = 55)
	phone = models.CharField(max_length = 14)
	fax = models.CharField(max_length = 14, null = True, blank = True)
	hours = models.CharField(max_length = 28, null = True, blank = True)
	link = models.CharField(max_length = 100, null = True, blank = True)
	description = models.CharField(max_length = 200, null = True, blank = True)
	# Address
	streetName = models.CharField(max_length = 40, null = True, blank = True)
	stateInfo = models.CharField(max_length = 40, null = True, blank = True)
	googleMaps = models.CharField(max_length = 700, null = True, blank = True)
	
	def __str__(self):
		return self.name
