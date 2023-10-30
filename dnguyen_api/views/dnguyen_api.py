# coding=utf-8
from django import http

def test(request):
	response = http.HttpResponse('{"result": "OK", "reply": "kết quả trả về nè"}')
	response['content-type'] = 'application/json; charset=utf-8'
	return response
