from django.db import models
#from imagekit.models import ImageSpecField
#from imagekit.processors import ResizeToFill
# Create your models here.

class BankAccount(models.Model):
	AccountId=models.CharField(primary_key = True,max_length=20)
	AccountHolder=models.CharField(max_length=30)
	Balance=models.IntegerField()
	def __str__(self):
		return self.AccountHolder
		
	class Admin:
		pass
		
class Member(models.Model):
	MemberId=models.CharField(primary_key = True,max_length=20)
	Name=models.CharField(max_length=30)
	House_no=models.CharField(max_length=30)
	City=models.CharField(max_length=30)
	State=models.CharField(max_length=30)
	PinCode=models.CharField(max_length=10)
	Email=models.EmailField()
	Account=models.ForeignKey('BankAccount',to_field='AccountId')
	def __str__(self):
		return self.Name

	class Admin:
		pass

class House(models.Model):
	
	
	
	HouseId=models.AutoField(primary_key = True)
	Price=models.CharField(max_length=10)
	Rooms=models.CharField(max_length=5)
	Status=models.CharField(max_length=30)
	House_no=models.CharField(max_length=30)
	City=models.CharField(max_length=30)
	State=models.CharField(max_length=30)
	PinCode=models.CharField(max_length=10)
	Member=models.ForeignKey('Member',to_field='MemberId')
	def __str__(self):
		return self.House_no
	class Admin:
		pass
	
class Room(models.Model):
	CHOICES = (
		('Bedroom','Bedroom'),
		('kitchen','Kitchen'),
		('Drawing room','Drawing room'),
		('Balcony','Balcony'),
		('OTHERS','OTHERS'),
		
		
	)
	RoomId=models.CharField(primary_key = True,max_length=20)
	Area=models.CharField(max_length=30)
	Type=models.CharField(max_length=30,choices = CHOICES)
	House=models.ForeignKey('House',to_field='HouseId')
	#Images = models.ImageField(upload_to='/tmp')
	def __str__(self):
		return self.Type
	class Admin:
		pass
	
class Catalog(models.Model):
	CHOICES = (
		('1','1'),
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),
		('6','6'),
		('7','7'),
		('8','8'),
		('9','9'),
		('10','10'),
	)
	Title=models.CharField(max_length=30)
	Rating=models.CharField(max_length=3,choices = CHOICES)
	Properties=models.CharField(max_length=30)
	House=models.ForeignKey('House',to_field='HouseId')
	def __str__(self):
		return self.Title
	class Admin:
		pass
	
class Comment(models.Model):
	CommentId=models.CharField(primary_key = True,max_length=20)
	Member=models.ForeignKey('Member',to_field='MemberId')
	House=models.ForeignKey('House',to_field='HouseId')
	Description=models.CharField(max_length=30)
	def __str__(self):
		return self.Description
	class Admin:
		pass
		
class Feedback(models.Model):
	Member=models.ForeignKey('Member',to_field='MemberId')
	Feedback=models.CharField(max_length=30)
	def __str__(self):
		return self.Feedback
	class Admin:
		pass
	
class Login(models.Model):
	Member=models.ForeignKey('Member',to_field='MemberId')
	Password=models.CharField(max_length=30)
	
	class Admin:
		pass
		#//< im"
	
#class Image(models.Model):
#	img = models.ImageField(upload_to='F:\New folder\pics\hom pics\home pics 1')
