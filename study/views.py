from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader


POST_FORM = """
<form method='post' action='test_get_post'>
	<p>用户名:<input type='text' name='name'/></p>
	<p>密 码:<input type='password' name='password'/></p>
	<input type='submit' value='提交'>
</form>
"""

def page_2003_view(request):
	html="<h1>这是Django的第一个页面</h1>"
	return HttpResponse(html)

def html_view(request):
	html = "这是我的首页~"
	return HttpResponse(html)

def page1_view(request):
	html = "这是我的第一个页面"
	return HttpResponse(html)

def page2_view(request):
	html = "这是我的第一个页面"
	return HttpResponse(html)

def page3_view(request):
	html = "这是我的第一个页面"
	return HttpResponse(html)

def pagen_view(request,n):
	html = "这是我第%s个页面！！！"%(n)
	return HttpResponse(html)

def pagem_view(request,m,t,n):
	if t == "-":
		result = m-n
		html = "计算结果为%s"%(result)
	elif t == "+":
		result = m + n
		html = "计算结果为%s"%(result)
	elif t == "*":
		result = m * n
		html = "计算结果为%s"%(result)
	elif t == "/":
		result = m / n
		html = "计算结果为%s"%(result)
	else:
		html = "暂不支持该运算！"
	return HttpResponse(html)

def pagep_view(request,x,op,y):
	if op == "-":
		result = x-y
		html = "re_path计算结果为%s"%(result)
	elif op == "+":
		result = x + y
		html = "re_path计算结果为%s"%(result)
	elif op == "*":
		result = x * y
		html = "re_path计算结果为%s"%(result)
	elif op == "/":
		result = x / y
		html = "re_path计算结果为%s"%(result)
	else:
		html = "re_path暂不支持该运算！"
	return HttpResponse(html)

def test_request(request):
	print("path_info:",request.path_info)
	print("method:",request.method)
	print("GET请求所有数据:",request.GET)
	print("POST请求所有数据:",request.POST)
	#return HttpResponse("test request is ok")
	#请求重定向
	return HttpResponseRedirect("html/page/1")

def test_get_post(request):
	if request.method =="GET":
		#print(request.GET["a"])
		print(request.GET.getlist("a"))      #用于获取多个同名参数的值
		print(request.GET.get("c","no c"))   #get("参数名","默认值")
		return HttpResponse(POST_FORM)
	elif request.method =="POST":
		print(request.POST["name"])
		print(request.POST.get('phone','没有密码'))
		print(request.POST)
		return HttpResponse("test is ok")
	else:
		pass

def test_html(request):
	#方案1
	# from django.template import loader
	# t = loader.get_template("test_html.html")
	# return HttpResponse(t)

	#方案2
	dic = {
		"name":"hello,world",
		"phone":"1234567890"
	}
	from django.shortcuts import render
	return render(request,"test_html.html",dic)

def test_request_html(request):
	if request.method =="GET":
		name = request.GET.get("name","用户未输入用户名！！！")
		password = request.GET.get("password","用户未输入密码！！！")
		print(request.method)
		html=loader.get_template("test_get_post.html")
		rsp = html.render()
		return HttpResponse(rsp)
	elif request.method == "POST":
		name = str(request.POST.get("name","用户未输入用户名！！！"))
		password = str(request.POST.get("password","用户未输入密码！！！"))
		userinfo = {}
		userinfo["name"] = name
		userinfo["password"] = password
		return render(request,"test_request_html_rsp.html",userinfo)
	else:
		return HttpResponse("您访问的页面不存在~~~")

def test_param_html(request):
	dic = {}
	dic["int"]="6688"
	dic["str"]="I'm a str"
	dic["list"] = [1,2,3,4,5,6]
	dic["dict"] = {"name":"tom","age":"18"}
	dic["func"]=say_hi
	dic["class_job"] = Dog()
	dic["script"]="<script>alert(html转义)</script>"
	return render(request,"test_param_html.html",dic)

def say_hi():
	return "I'm a func !"

class Dog:
	def say(self):
		return "I'm a class job"

def test_if_for(request):
	dic = {}
	dic["x"] = 100
	dic["list"] = ["Tom","Lily","Jimi","Tomas"]
	return render(request,"test_if_for.html",dic)

def	test_calculator_html(request):
	if request.method == "GET":
		return render(request,"test_calculator_html.html")
	elif request.method == "POST":
		num1 = int(request.POST.get("num1"))
		num2 = int(request.POST.get("num2"))
		op = request.POST.get("op")
		result=0
		if op == "add":
			result = num1+num2
		elif op == "sub" :
			result = num1-num2
		elif op == "mul":
			result = num1 * num2
		elif op == "div":
			result = num1/num2
		else:
			return "您的输入有误"
		return render(request,"test_calculator_html.html",locals()) #locals局部变量自动构造成字典

def base_view(request):

	return render(request,"base.html")

def music_view(request):

	return render(request,"music.html")

def sport_view(request):

	return render(request,"sport.html")

def test_url(request):

	return render(request,"test_url.html")

def test_url_result(request,age):

	return HttpResponse("~~~test is OK ~~~~")

def test_static(request):

	return render(request,"test_static.html")