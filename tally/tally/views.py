from django.shortcuts import render ,redirect
from rest_framework.views import APIView

class LoginView( APIView):
	def get( self, req ):
		return render( req , 'login.html' , {} )

	def post( self, req ):
		data = req.POST
		user = data.get( 'user' )
		password = data.get( 'password')
		if user == 'kunal' and password == 'abc123':
			return redirect( '/uploader/upload' )
		else:
			return render(req , 'LoginFailure.html' , {})