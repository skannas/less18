from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.



def getProduct(request):
	#print(*dir(Good.objects, sep='\n'))
	data = {}
	data['goods'] = Good.objects.all()

	#print(*dir(request), sep ='\n')
	#print('______')
	#print(request.user)
	#print('______')
	#print('is_ajax', request.is_ajax)
	#data ={}
	data['info'] = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tenetur eligendi labore mollitia nihil accusamus eaque, pariatur, earum minima consequuntur voluptatibus alias provident quia, natus culpa accusantium quaerat dolor soluta incidunt!'
	return render(request, 'product/index.html', context=data)
	# return HttpResponse('<h1> hi </h1>')

def getIndexMy(request):
	#data ={}
	#data['hText'] = 'headr'
	#data['pText'] = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tenetur eligendi labore mollitia nihil accusamus eaque, pariatur, earum minima consequuntur voluptatibus alias provident quia, natus culpa accusantium quaerat dolor soluta incidunt!'
	#context['dataList'] = data
	return render(request, 'product/indexMy.html')#, context = context)
	# return HttpResponse('<h1> hi </h1>')