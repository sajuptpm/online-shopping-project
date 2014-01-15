from django import forms
 
class UserRegistrationForm(forms.Form):
	uname = forms.CharField(max_length=200, label=("Name:"))
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("Password:"))
	emailid = forms.EmailField(max_length=100, label=("Email Id:"))
	mobile = forms.CharField(max_length=10, label=("Mobile:"))

class LoginForm(forms.Form):

	uname = forms.CharField(max_length=200, label=("Name:"))
	password = forms.CharField(max_length=30, label=("Password:"))

class ProductForm(forms.Form):

	pname=forms.CharField(max_length=200)
	discription=forms.CharField(max_length=500)
	price=forms.IntegerField()
	noitem=forms.IntegerField()
	createdby=models.ForeignKey(Usertb)
	cid=models.ForeignKey(Catagorytb)



		

    
