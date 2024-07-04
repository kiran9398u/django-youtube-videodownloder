# importing all the required modules 
from django.shortcuts import render, redirect 
from pytube import *


# defining function 
def youtube(request): 

	# checking whether request.method is post or not 
	if request.method == 'POST': 
		
		# get link from frontend 
		link = request.POST['link'] 
		video = YouTube(link) 

		# setting video resolution 
		stream = video.streams.get_lowest_resolution() 
		
		# download video 
		stream.download() 

		# return HTML page 
		return render(request, 'home.html') 
	return render(request, 'home.html')

    