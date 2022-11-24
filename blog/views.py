from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import Post,UndoPost
from .forms import PostForm
from django.contrib.auth.decorators import login_required


# REGISTER PAGE
def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        ps1 = request.POST['password1']
        ps2 = request.POST['password2']
        print(username,ps1,ps2)
        if ps1 != ps2:
            messages.info(request,'Password does not match!')
            return redirect('/register/')
        else:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken!!')
                return redirect('/register/')
            reg = User.objects.create_user(username=username,password=ps2)
            reg.save()
            messages.info(request,'Account Created Sunccessfully!!')
    fm = UserCreationForm()
    return render(request,'register.html',{'form':fm})


# LOGIN PAGE
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        ps = request.POST['password']
        user = authenticate(request,username=username,password=ps)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('/blog_home_page/')
        print(user)
        messages.info(request,'Invalid User')
        return redirect('/login/')
    return render(request,'login.html')


# BLOG_HOME PAGE
@login_required
def blog_home_page(request):
    posts = Post.objects.order_by('-timestamp')
    return render(request,'blog_home_page.html',{'posts':posts})


# USER PROFILE PAGE
@login_required
def user_profile(request):
    logged_in_user = request.user
    logged_in_user_posts = Post.objects.filter(blog_user=logged_in_user)
    return render(request,'user_profile.html',{'posts':logged_in_user_posts})


# NEW POST BY USER
@login_required
def new_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.blog_user = request.user
            post_form.save()
            # messages.info(request,"New Post Created!")
            return redirect('/user_profile/')
    form = PostForm()
    return render(request,'new_post.html',{'form':form})


# EDIT POST BY USER 
@login_required
def edit_post(request,id):
    if request.method == 'POST':
        data = Post.objects.get(pk=id)
        form = PostForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    data = Post.objects.get(pk=id)
    form = PostForm(instance=data)
    return render(request,'edit_post.html',{'form':form})

# DELETE POST
@login_required
def delete_post(request,id):
    if request.method == 'POST':
        post_data = Post.objects.get(id=id)
        print(post_data, "id: ",id)

        # # To store Post in UndoPost
        # username = post_data.blog_user.username
        # title = post_data.title
        # content = post_data.content
        # u = UndoPost.objects.create(username=username, title=title, content=content)
        # u.save()

        # Post Delete
        post_data.delete()
        print("Post delete successfully")

        # # Get UndoPost ID
        # id = UndoPost.objects.get(content=content)
        # undo_id = id.undo_id
        # print("Undo ID: ",undo_id)

        # # Save UndoID in session
        # request.session['undo_id'] = undo_id
        # print("undo ID saved in session")

        messages.info(request,"Post Deleted")
        return redirect('/user_profile/')

    return render(request,'delete_post.html')


# UNDO POST
@login_required
def undo_post(request):
    print("In undo_post View")
    if request.method == 'POST':
        print("post")
        get_data = request.session.get('undo_id')
        print(get_data)
        d = UndoPost.objects.get(undo_id=get_data)
        print("-------d------ ",d)
        data = Post.objects.create(blog_user=request.user, title=d.title, content=d.content)
        data.save()
        print("Post Restored")
        # return JsonResponse({'messages':'undo'})
        # return redirect('/user_profile/')
        return HttpResponse('post undo')
    return redirect('/user_profile/')

# LOG OUT BY USER
def user_logout(request):
    print("jh")
    logout(request)
    return render(request,'logout.html')


