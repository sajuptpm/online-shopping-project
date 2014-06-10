from book.models import Catagory
from django import forms
from datetime import date
import warnings

 
class UserRegistrationForm(forms.Form):
	username = forms.CharField(max_length=200, label=("User Name:"), required=True)
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("Password:"))
	#repeatpswd = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("Repeate Password:*"))
	fname = forms.CharField(max_length=10, label=("First Name:"), required=True)
	lname = forms.CharField(max_length=10, label=("Last Name:"), required=True)
	emailid = forms.EmailField(max_length=100, label=("Email Address:"), required=True)
	#address=forms.CharField(max_length=200, widget=forms.Textarea,label=("Street Address:*")) 
	#lanmark=forms.CharField(max_length=100, label=("Landmark:*"))
	#state=forms.CharField(max_length=50, label=("State:*"))
	#country=forms.CharField(max_length=50, label=("Country:*"))
	#pincode=forms.IntegerField(label=("Pincode:*"))
	#phone=forms.IntegerField(label=("Phone Number:*"))
	#gender=forms.CharField(max_length=7, label=("Gender:*"))


class UserProfileUpdateForm(forms.Form):
	#username = forms.CharField(max_length=200, label=("User Name:"), required=True)
	#password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("Password:"))
	#repeatpswd = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("Repeate Password:*"))
	fname = forms.CharField(max_length=10, label=("First Name:"), required=True)
	lname = forms.CharField(max_length=10, label=("Last Name:"), required=True)
	emailid = forms.EmailField(max_length=100, label=("Email Address:"), required=True)
	#address=forms.CharField(max_length=200, widget=forms.Textarea,label=("Street Address:*")) 
	#lanmark=forms.CharField(max_length=100, label=("Landmark:*"))
	#state=forms.CharField(max_length=50, label=("State:*"))
	#country=forms.CharField(max_length=50, label=("Country:*"))
	#pincode=forms.IntegerField(label=("Pincode:*"))
	#phone=forms.IntegerField(label=("Phone Number:*"))
	#gender=forms.CharField(max_length=7, label=("Gender:*"))

class ProductForm(forms.Form):
	#cname = forms.CharField(max_length=300, label=("Catagory Name:"))
	#CHOICES = ()
	cname = forms.ChoiceField()
	pname = forms.CharField(max_length=300, label=("Product Name:"), required=True)
	discription = forms.CharField(max_length=500, widget=forms.Textarea,label=("Discription:"), required=True)
	price = forms.IntegerField(label=("Price:"), required=True)
	noitem = forms.IntegerField(label=("No: Of Items:"), required=True)
	photo  = forms.ImageField(required=True)

	#def __init__(self):
		#forms.Form.__init__(self)
	def __init__(self, *args, **kwargs):
          super(ProductForm, self).__init__(*args, **kwargs)
          #print "...args...",args
          #print "....kwargs.....",kwargs
          #print "fffffffffff..........self.........fffffffffffffff",self
          
          cat = Catagory.objects.all()

          cname_choice_list = []

          for c in cat:
          	#print c.cname
          	#print c.id
          	cname_choice_list.append((c.id,c.cname))



          #cname_choice_list = ((1,1),(2,2))
          #cname_choice_list = (Catagory.objects.all())
          self.fields['cname'] = forms.ChoiceField(choices = cname_choice_list)



class CatagoryForm(forms.Form):
	cname = forms.CharField(max_length=200,label=("Catagory Name:"), required=True)


class ChangePasswordForm(forms.Form):
	newpassword= forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("New Password"))
	renewpasssword=forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("Retype New Password"))
		


class OrderCancelForm(forms.Form):
	oname = forms.CharField(label=("Order Id:"), required=True)

#class PincodeForm(forms.Form):
	#pincode = forms.CharField(label=("pincode:"), required=True)
