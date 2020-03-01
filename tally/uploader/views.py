from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from tally import settings

# Create your views here.
from .utils import uploadFileToS3
def upload_file_view( req ):
    
    return  render( req , 'upload.html', {} )


def upload_file_to_s3(request):
	if request.method == 'POST' and request.FILES['fileToUpload']:

		fileToUpload 	= request.FILES['fileToUpload']
		fs 				= FileSystemStorage()
		filename 		= fs.save(fileToUpload.name, fileToUpload)
		
		print( filename ,'filename' , settings.BASE_DIR )	
		uploaded_file_url 		= fs.url(filename)
		result 					= uploadFileToS3( settings.BASE_DIR +'/'+ uploaded_file_url )
		print( result )

		print( 'Saved File to S3')
		
		return render(request, 'success.html', { 
		    'uploaded_file_url': uploaded_file_url
		})

	return render(request, 'success.html' , {})
