# coding=utf-8
from django import http
import requests

def test(request):
	response = http.HttpResponse('{"result": "OK", "reply": "kết quả trả về nè"}')
	response['content-type'] = 'application/json; charset=utf-8'
	return response

def test_update(request):
	response = http.HttpResponse('{"result": "OK", "reply": "Đây là api test update"}')
	response['content-type'] = 'application/json; charset=utf-8'
	return response

def docker(request):
	response = http.HttpResponse('{"result": "OK", "reply": "docker api trả về kết quả"}')
	response['content-type'] = 'application/json; charset=utf-8'
	return response

def deeper_api(request):
	response = requests.get('http://0.0.0.0:7000/chiencon')
	# response = http.HttpRequest.REQUEST.get('{"result": "OK", "reply": "docker api trả về kết quả"}')
	# response['content-type'] = 'application/json; charset=utf-8'
	return response

def chiencon(request):
	response = http.HttpRequest.REQUEST.get('{"result": "OK", "reply": "chiên con rất dễ thương"}')
	response['content-type'] = 'application/json; charset=utf-8'
	return response
