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
	response = requests.get('http://172.17.0.1:7000/chiencon')
	# response = http.HttpResponse('{"result": "OK", "reply": "docker api trả về kết quả"}')
	# response['content-type'] = 'application/json; charset=utf-8'
	return response

def chiencon(request):
	response = http.HttpResponse('{"result": "OK", "reply": "api chiencon trả kết quả về cho deeper api"}')
	response['content-type'] = 'application/json; charset=utf-8'
	return response
