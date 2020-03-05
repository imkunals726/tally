from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from tally import settings
import os
# Create your views here.
from .utils import uploadFileToS3
def upload_file_view( req ):
    
    return  render( req , 'upload.html', {} )


def upload_file_to_s3(request):
	try:
		if request.method == 'POST' and request.FILES['fileToUpload']:

			fileToUpload 	= request.FILES['fileToUpload']
			fs 				= FileSystemStorage()
			
			filename 		= fs.save(fileToUpload.name, fileToUpload)
			uploaded_file_url 		= fs.url(filename)

			result 					= uploadFileToS3( settings.MEDIA_ROOT + filename )
			os.remove( settings.MEDIA_ROOT + filename )
			
			return render(request, 'success.html', { 
			    'uploaded_file_url': uploaded_file_url
			})

		return render(request, 'success.html' , {})
	except Exception as e:
		_,_,tb_info = sys.exc_info()
		print( tb_info.lineno ,'lineno')
