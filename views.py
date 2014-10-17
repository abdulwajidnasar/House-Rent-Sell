from django.shortcuts import render

# Create your views here.

	
	
def sellorrent(request):
	form2 = RentSellForm(request.POST or None)
	if form2.is_valid():
		City = form2.cleaned_data['City']
		State = form2.cleaned_data['State']
		Houseno = form2.cleaned_data['Houseno']
		Price = form2.cleaned_data['Price']
		Rooms = form2.cleaned_data['Rooms']
		Pincode = form2.cleaned_data['Pincode']
		Status = form2.cleaned_data['Status']
		Member = form2.cleaned_data['Member']
		cursor = connection.cursor()
		cursor.execute("INSERT INTO houses_house (Price,Rooms,Status,House_no,City,State,PinCode,Member) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,)",[Price,Rooms,Status,Houseno,City,State,Pincode,Member])
		cursor.execute('COMMIT')
		data = "Review has been added. It will be displayed once approved by the admin."
		return render_to_response('boilerplate.html', {'data': data})
