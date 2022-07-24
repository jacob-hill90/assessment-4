from django.shortcuts import render
from .models import Category, Post
from django.views.decorators.csrf import csrf_exempt
import json

def list_categories(request):
    categories = Category.objects.all()
    print(categories)
    data = {"categories" : categories}
    return render(request, 'clj_app/list_categories.html', data)

def list_posts(request, category_id):
    category_posts = Post.objects.all().filter(category_id = category_id)
    category_name = Category.objects.all().get(id = category_id)
    data = {"posts": category_posts, "category": category_name}
    return render(request, 'clj_app/list_posts.html', data)


def post_info(request, category_id, post_id):
    post = Post.objects.all().get(id = post_id)
    data = {"post" : post}
    return render(request, 'clj_app/post_info.html', data)

@csrf_exempt
def add_post(request, category_id):
    if request.method == "POST":
        body = json.loads(request.body)
        newPost = Post(title = body["title"], description = body["description"], price = body["price"], seller = body["seller"], category_id = category_id)
        newPost.save()
    return render(request, "clj_app/add_post.html")

@csrf_exempt
def edit_post(request, category_id, post_id):
    if request.method == "POST":
        body = json.loads(request.body)

        post = Post.objects.all().get(id = post_id)

        post.title = body['title']
        post.description = body['description']
        post.price = body['price']
        post.seller = body['seller']

        post.save()
    data = {"post": Post.objects.all().get(id = post_id)}
    return render(request, "clj_app/edit_post.html", data)