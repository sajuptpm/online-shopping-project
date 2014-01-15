from django.db import models

# Create your models here.

class Usertb(models.Model):
	uname = models.CharField(max_length=200)
	password= models.CharField(max_length=50)
	emailid=models.EmailField(max_length=100)
	mobile=models.CharField(max_length=10)

class Catagorytb(models.Model):
	cname=models.CharField(max_length=200)
	purdate=models.DateTimeField('purchase-date')
	createdby=models.ForeignKey(Usertb)

class Producttb(models.Model):
	pname=models.CharField(max_length=200)
	discription=models.CharField(max_length=500)
	#price=models.IntegerField()
	#noitem=models.IntegerField()
	createdby=models.ForeignKey(Usertb)
	cid=models.ForeignKey(Catagorytb)

class Carttb(models.Model):
	pid=models.ForeignKey(Producttb)
	noitem=models.IntegerField()
	totalprice=models.IntegerField()
	status=models.CharField(max_length=10)
	purdate=models.DateTimeField("purchase-date")
	deldate=models.DateTimeField("delivary-date")




		

	
		
		
