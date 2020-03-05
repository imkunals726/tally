from django.shortcuts import render , redirect
from django.core.files.storage import FileSystemStorage
from tally import settings
import os
# Create your views here.
from .utils import uploadFileToS3
from .models import UploadedFile
def upload_file_view( req ):   
    return  render( req , 'upload.html', {} )

def success_page( req ):
	return render( req , 'success.html' ,{})

def upload_file_to_s3(request):
	try:
		if request.method == 'POST' and request.FILES['fileToUpload']:

			fileToUpload 	= request.FILES['fileToUpload']
			fs 				= FileSystemStorage()
			
			filename 			= fs.save(fileToUpload.name, fileToUpload)
			uploaded_file_url 	= fs.url(filename)

			result 			= uploadFileToS3( settings.MEDIA_ROOT + filename )
			file_url 		= result[ 'data' ][ 'fileURL' ]
			# uploaded_file 	= UploadedFile( file_name = fileToUpload.name , file_url = file_url )

			# uploaded_file.save()
			print( 'done' )
			os.remove( settings.MEDIA_ROOT + filename )
			
			return redirect( '/uploader/success' )
	except Exception as e:
		_,_,tb_info = sys.exc_info()
		print( tb_info.lineno ,'lineno')

def all_files(req):

	files = UploadedFile.objects.all()
	all_files_info = []

	for file_info in files:
		all_files_info.append({'file_name' : file_info.file_name , 
								  'file_url' : file_info.file_url})

	return render( req , 'all_files.html' , { "files" : all_files_info } )
