from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

from .models import Post
from .models import Comment
from .models import Category


def hello(request):
	return HttpResponse('hello world')

def hello_with_template(request):
	return render(request, 'hello.html')

def list_posts(request):
	per_page = 3
	current_page = request.GET.get('page',1)
	# current_page = int(request.GET['page']) 숫자를 문자열로 받아요
	#try:
		#current_page = int(request.GET['page'])
		#page인자 없는 것 대응
	#	current_page = int(request.GET.get('page',1))
	#except ValueError:
	#	current_page = 1

	all_posts = Post.objects.select_related().all().order_by('-pk')
	
	pagi = Paginator(all_posts, per_page)

	try:
		pg = pagi.page(current_page)
	except PageNotAnInteger:
		pg = pagi.page(1)
	except EmptyPage:
		pg = []

	#all_posts = all_posts[(current_page-1)*per_page:current_page*per_page]
	return render(request, 'list_posts.html', {
		'posts':pg,
		})

# 댓글 생성하기 전 버전
# def view_post(request, pk):
# 	# try execption하던가 
# 	the_post = get_object_or_404(Post, pk=pk)

# 	#the_post = Post.objects.get(pk=pk)
# 	return render(request, 'view_posts.html', {
# 		'post': the_post,

# 		})

# 댓글 추가 버전 
def view_post(request, pk):
	# try execption하던가 
	the_post = get_object_or_404(Post, pk=pk)

	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		new_comment = Comment()
		new_comment.content = request.POST.get('content')
		new_comment.post_id = pk
		new_comment.save()
		return redirect('view_post', pk=pk)

	#the_post = Post.objects.get(pk=pk)
	return render(request, 'view_posts.html', {
		'post': the_post,

		})


def create_post(request):
	categories = Category.objects.all()
	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		new_post = Post()
		new_post.title = request.POST.get('title')
		new_post.content = request.POST.get('content')

		category_pk = request.POST.get('category')
		category = get_object_or_404(Category, pk = category_pk)
		new_post.category = category
		new_post.save()

		return redirect('view_post', pk=new_post.pk)

	return render(request, 'create_post.html', {
		'categories':categories,
		})

def delete_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		#post.delete()
		return redirect('/')

	return render(request, 'delete_post.html',{
		'post':post,
		})

def delete_comment(request, pk, pk2):
	if request.method == 'GET':
		comment = get_object_or_404(Comment, pk=pk2)
		comment.delete()
		return redirect('view_post', pk)


