from django import forms
from django.db import connection
from .models import BankAccount
from .models import Member
from .models import House
from .models import Room
from .models import Catalog
from .models import Comment
from .models import Feedback
from .models import Login
#from .models import Image
CHOICES1 = (
	('For Sale','For Sale'),
	('For Rent','For Rent'),
)

CHOICES = (
	('1 BHK','1 BHK'),
	('2 BHK','2 BHK'),
	('3 BHK','3 BHK'),
	('4 BHK','4 BHK'),
	('5 BHK','5 BHK'),
)

CHOICES2 = (
	('Andaman','Andaman and Nicobar Islands(AN)'),
    ('Andhra','Andhra Pradesh (AP)'),
    ('Arunachal','Arunachal Pradesh (AR)'),
    ('Assam','Assam (AS)'),
    ('Bihar','Bihar (BR)'),
	('Chand','Chandigarh (CH)'),
    ('Chhat','Chhattisgarh (CG)'),
	('Dadra','Dadra and Nagar Haveli (DN)'),
	('Daman','Daman and Diu (DD)'),
	('Delhi','Delhi (DL)'),
    ('Goa','Goa (GA)'),
    ('Gujar','Gujarat (GJ)'),
    ('Haryana','Haryana (HR)'),
    ('Himachal','Himachal Pradesh (HP)'),
    ('Jammu','Jammu and Kashmir (JK)'),
    ('Jharkhand','Jharkhand (JH)'),
    ('Karnataka','Karnataka (KA)'),
    ('Kerala','Kerala (KL)'),
	('Lakshadw'.'Lakshadweep (LD)'),
    ('Madhya','Madhya Pradesh (MP)'),
    ('Maharas','Maharashtra (MH)'),
    ('Manip','Manipur (MN)'),
    ('Meghal','Meghalaya (ML)'),
    ('Mizor','Mizoram (MZ)'),
    ('Nagaland','Nagaland (NL)'),
    ('Odisha','Odisha(OR)'),
	('Pondicherry','Pondicherry (PY)'),
    ('Punjab','Punjab (PB)'),
    ('Rajasthan','Rajasthan (RJ)'),
    ('Sikkim','Sikkim(SK)'),
    ('Tamil','Tamil Nadu (TN)'),
    ('Tripura','Tripura (TR)'),
    ('Uttar','Uttar Pradesh (UP)'),
    ('Uttarakhand','Uttarakhand (UK)'),
    ('West','West Bengal (WB)'),
	
)


class RentSellForm(forms.Form):
	City = forms.CharField()
	State = forms.ChoiceField(choices=CHOICES2)
	Houseno = forms.CharField()
	Price = forms.CharField()
	Rooms = forms.ChoiceField(choices=CHOICES)
	Pincode = forms.CharField()
	Status = forms.ChoiceField(choices=CHOICES13)
	cursor = connection.cursor()
	cursor.execute("select Member,Member from houses_member")
	CHOICES = cursor.fetchall()
	Member = forms.ChoiceField(choices = CHOICES3)
	

	

	
	
	
	
	
	
