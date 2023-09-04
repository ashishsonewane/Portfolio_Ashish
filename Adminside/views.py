from .models import *
from imaplib import _Authenticator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib import auth


# Create your views here.
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if user.is_superuser == True and user.is_staff == True:
                auth.login(request, user)
                return redirect('index')
            else:
                return redirect('/')
        else:
            return redirect('/')
    return render(request, 'login.html')


def adminlogout(request):
    user = request.user
    logout(request)
    return redirect('login')


def index(request):
    return render(request, 'index.html')


def settings(request):
    return render(request, 'settings.html')


def gallary_table(request):
    data = PersonalInformation.objects.filter(user=request.user.id)
    return render(request, 'gallary_table.html', {'data': data})


def add_gallary(request):
    try:
        user = User.objects.get(id=request.user.id)

        if request.method == 'POST':
            name_complete = request.POST['name_complete']
            avatar = request.FILES.get('avatar')
            mini_about = request.POST['mini_about']
            address = request.POST['address']
            phone = request.POST['phone']
            email = request.POST['email']
            cv = request.FILES.get('cv')
            linkedin = request.POST['linkedin']
            github = request.POST['github']
            facebook = request.POST['facebook']
            twitter = request.POST['twitter']
            instagram = request.POST['instagram']
            mycv = request.FILES.get('mycv')

            gallaryobj = PersonalInformation.objects.create(user=user, name_complete=name_complete, avatar=avatar, mini_about=mini_about, address=address,
                                                            email=email, phone=phone, cv=cv, github=github, linkedin=linkedin, twitter=twitter, instagram=instagram, facebook=facebook, mycv=mycv)
            return redirect('gallary_table')
    except:
        return redirect('gallary_table')


def delete_gallary(request, id):
    data = PersonalInformation.objects.get(id=id)
    data.delete()
    return redirect('gallary_table')


def gallary_update(request, id):
    gallaryobj = PersonalInformation.objects.get(id=id)
    if request.method == 'POST':
        name_complete = request.POST['name_complete']
        avatar = request.FILES.get('avatar')
        if avatar:
            gallaryobj.avatar = avatar
        else:
            pass
        mini_about = request.POST['mini_about']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        cv = request.FILES.get('cv')
        linkedin = request.POST['linkedin']
        github = request.POST['github']
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']
        instagram = request.POST['instagram']
        mycv = request.FILES.get('mycv')

        gallaryobj.cv = cv
        gallaryobj.linkedin = linkedin
        gallaryobj.github = github
        gallaryobj.facebook = facebook
        gallaryobj.twitter = twitter
        gallaryobj.instagram = instagram
        gallaryobj.mycv = mycv
        gallaryobj.name_complete = name_complete
        gallaryobj.mini_about = mini_about
        gallaryobj.address = address
        gallaryobj.phone = phone
        gallaryobj.email = email
        gallaryobj.save()
        print(gallaryobj)
        return redirect('gallary_table')
    return render(request, 'gallary_update.html', {'gallaryobj': gallaryobj})


def about_table(request):
    data = About.objects.all()
    return render(request, 'about_table.html', {'data': data})


def add_about(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description1 = request.POST.get('description1')
        description2 = request.POST.get('description2')
        about_avatar = request.FILES.get('about_avatar')
        aboutobj = About.objects.create(
            title=title, description1=description1, description2=description2, about_avatar=about_avatar)
        return redirect('about_table')


def delete_about(request, id):
    aboutobj = About.objects.get(id=id)
    aboutobj.delete()
    return redirect('about_table')


def update_about(request, id):
    aboutobj = About.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description1 = request.POST.get('description1')
        description2 = request.POST.get('description2')
        about_avatar = request.FILES.get('about_avatar')
        if about_avatar:
            aboutobj.about_avatar = about_avatar
        else:
            pass
        aboutobj.title = title
        aboutobj.description1 = description1
        aboutobj.description2 = description2

        aboutobj.save()
        return redirect('about_table')
    return render(request, 'update_about.html', {'aboutobj': aboutobj})


def projects_table(request):
    data = Projects.objects.all()
    return render(request, 'projects_table.html', {'data': data})


def projects_add(request):
    if request.method == 'POST':

        title = request.POST.get('title')
        skill = request.POST.get('skill')
        link = request.POST.get('link')
        image = request.FILES.get('image')
        projectobj = Projects.objects.create(
            title=title, skill=skill, image=image, link=link)
        return redirect('projects_table')


def project_delete(request, id):
    projectobj = Projects.objects.get(id=id)
    projectobj.delete()
    return redirect('projects_table')


def project_edit(request, id):
    projectobj = Projects.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        skill = request.POST.get('skill')
        link = request.POST.get('link')
        image = request.FILES.get('image')
        if image:
            projectobj.image = image
        else:
            pass

        projectobj.title = title
        projectobj.skill = skill
        projectobj.link = link
        projectobj.image = image
        projectobj.save()
        return redirect('projects_table')
    return render(request, 'project_edit.html', {'projectobj': projectobj})


def contact_table(request):
    contactobj = Contact.objects.all()
    return render(request, 'contact_table.html', {'contactobj': contactobj})


def contact_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        email = request.POST.get('email')
        print(email)
        location = request.POST.get('location')
        print(location)
        msg = request.POST.get('msg')
        print(msg)
        link = request.POST.get('link')
        print(link)
        github = request.POST.get('github')
        print(github)
        linkedin = request.POST.get('linkedin')
        print(linkedin)
        facebook = request.POST.get('facebook')
        print(facebook)
        twitter = request.POST.get('twitter')
        print(twitter)
        instagram = request.POST.get('instagram')
        print(instagram)
        contactobj = Contact.objects.create(title=title, email=email, location=location, msg=msg, facebook=facebook,
                                            twitter=twitter, instagram=instagram, linkedin=linkedin, github=github, link=link)
        return redirect('contact_table')


def contact_delete(request, id):
    contactobj = Contact.objects.get(id=id)
    contactobj.delete()
    return redirect('contact_table')


def contact_edit(request, id):
    contactobj = Contact.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        email = request.POST.get('email')
        location = request.POST.get('location')
        msg = request.POST.get('msg')
        link = request.POST.get('link')
        github = request.POST.get('github')
        linkedin = request.POST.get('linkedin')
        facebook = request.POST.get('facebook')
        twitter = request.POST.get('twitter')
        instagram = request.POST.get('instagram')

        contactobj.title = title
        contactobj.email = email
        contactobj.location = location
        contactobj.location = location
        contactobj.msg = msg
        contactobj.link = link
        contactobj.github = github
        contactobj.linkedin = linkedin
        contactobj.facebook = facebook
        contactobj.twitter = twitter
        contactobj.instagram = instagram
        contactobj.save()
        return redirect('contact_table')
    return render(request, 'contact_edit.html', {'contactobj': contactobj})


def skill_table(request):
    data = Skills.objects.all()
    user = User.objects.all()
    return render(request, 'skill_table.html', {'data': data, "user": user})


def add_skill(request):
    userobj = User.objects.all()
    if request.method == 'POST':
        user_id = request.POST['username']
        userobj = User.objects.get(id=user_id)
        skill = request.POST['skill']
        num = request.POST['num']
        # colorobj = request.POST['color']
        skillobj = Skills.objects.create(skill=skill, num=num, user=userobj)
        return redirect('skill_table')


def skill_delete(request, id):
    skillobj = Skills.objects.get(id=id)
    skillobj.delete()
    return redirect('skill_table')


def skill_update(request, id):
    skillobj = Skills.objects.get(id=id)
    if request.method == 'POST':
        skill = request.POST['skill']
        num = request.POST['num']

        skillobj.skill = skill
        skillobj.num = num
        skillobj.save()
        return redirect('skill_table')
    return render(request, 'skill_update.html', {'skillobj': skillobj})
