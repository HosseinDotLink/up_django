from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import message, project
from django.contrib.auth.models import User
from django import template
from .forms import sendMessageForm, addProjectForm, editProjectForm
from django.db.models import Q
from functools import reduce
# Create your views here.
register = template.Library()




def index(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='دانشجو').exists():
            user = User.objects.filter(username=request.user)
            return render(request, 'panel/index.html', {'user': user})
        elif request.user.groups.filter(name='استاد').exists():
            user = User.objects.filter(username=request.user)
            return render(request,'panel/index.html',{'user':user})
        else:
            print("\nWe have a problem in user (" + request.user.username + ") groups!\n")
            data = {"body": "گروه کاری شما در سامانه درست وارد نشده است. لطفا موضوع را با مدیر سیستم در میان گذارید"}
            return render(request, 'panel/error.html', {'data':data})
    else:
        return  redirect('login/')

def msgList(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='دانشجو').exists():
            countMsg = []
            mastersList = User.objects.filter(groups=2).order_by('last_name', 'first_name')
            print(mastersList)
            for master in mastersList:
                countMsg.append(message.objects.filter(msg_master = master.id, msg_student = request.user).count())
            print(countMsg)
            return render(request, 'panel/chatList.html', {'masters': mastersList, 'cnt': countMsg})

        elif request.user.groups.filter(name='استاد').exists():
            countMsg = []
            studenWhoMessaged = []
            msgs = message.objects.filter(msg_master = request.user)
            for msg in msgs:
                # print(msg.msg_student)
                if msg.msg_student not in studenWhoMessaged:
                    studenWhoMessaged.append(msg.msg_student)
            # print(studenWhoMessaged)
            try:
                studentsList = User.objects.filter(reduce(lambda x, y: x | y, [Q(username=un) for un in studenWhoMessaged])).order_by('last_name', 'first_name')
                print(studentsList)
                for student in studentsList:
                    countMsg.append(message.objects.filter(msg_student=student.id).count())
                # print(countMsg)
                return render(request, 'panel/chatList.html', {'masters': studentsList, 'cnt': countMsg})
            except:
                return render(request, 'panel/chatListError.html')

        else:
            print("\nWe have a problem in user (" + request.user.username + ") groups!\n")
            data = {"body": "گروه کاری شما در سامانه درست وارد نشده است. لطفا موضوع را با مدیر سیستم در میان گذارید"}
            return render(request, 'panel/error.html', {'data':data})
    else:
        return  redirect('../login/')


def msgs(request, userID):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='دانشجو').exists():
            if request.method == 'GET':
                form = sendMessageForm()
                masterID = User.objects.filter(username=userID)
                master = message.objects.filter(msg_master=masterID[0].id).order_by('-msg_time')
                print(request.user)
                messages = master.filter(msg_student=request.user)
                return render(request, 'panel/chatroom.html', {'messages': messages, 'user': masterID})

            else:
                form = sendMessageForm(request.POST)
                print("you are in post")
                if form.is_valid():
                    print("form is valid")
                    masterID = User.objects.filter(username= userID)
                    msg = form.save(commit=False)
                    msg.msg_master = masterID[0]
                    msg.msg_student = request.user
                    print(msg)
                    msg.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
                else:
                    data = {
                        "body": "خطایی در تایید فرم بوجود آمده است. لطفا دوباره امتحان کنید"}
                    return render(request, 'panel/error.html', {'data': data})

        elif request.user.groups.filter(name='استاد').exists():
            if request.method == 'GET':
                form = sendMessageForm()
                studentID = User.objects.filter(username=userID)
                student = message.objects.filter(msg_student=studentID[0].id).order_by('-msg_time')
                print(request.user)
                print(student)
                messages = student.filter(msg_master=request.user)
                return render(request, 'panel/chatroom.html', {'messages': messages, 'user': studentID})
            
            else:
                form = sendMessageForm(request.POST)
                print("you are in post")
                if form.is_valid():
                    print("form is valid")
                    studentID = User.objects.filter(username= userID)
                    msg = form.save(commit=False)
                    msg.msg_master = request.user
                    msg.msg_student = studentID[0]
                    msg.msg_master_sender = True
                    print(msg)
                    msg.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
                else:
                    return render(request, 'panel/error.html')


        else:
            print("\nWe have a problem in user (" + request.user.username + ") groups!\n")
            data = {"body": "گروه کاری شما در سامانه درست وارد نشده است. لطفا موضوع را با مدیر سیستم در میان گذارید"}
            return render(request, 'panel/error.html', {'data':data})
    else:
        return  redirect('../../login/')


def projectsList(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='دانشجو').exists():
            have_accepted_project = False
            have_project = False
            if project.objects.filter(prj_student= request.user):
                if project.objects.filter(prj_student= request.user, prj_accept=True):
                    prj = project.objects.filter(prj_student= request.user, prj_accept=True)
                    master = User.objects.filter(username= prj[0].prj_master)
                    master_detail = master[0].first_name + " " + master[0].last_name
                    print(master_detail)
                    have_accepted_project = True
                    return render(request, 'panel/projectStudent.html', {'have_accepted_project': have_accepted_project, 'master':master_detail})
                else:
                    have_project = True
                    return render(request, 'panel/projectStudent.html', {'have_project': have_project})
            else:
                projects = project.objects.filter(prj_student = None).order_by('-prj_time')
                masterNames =[]
                for prj in projects:
                    masterNames.append(User.objects.filter(username = prj.prj_master))
                print(projects)
                return render(request, 'panel/projectStudent.html', {'projects': projects, 'master': masterNames})
        elif request.user.groups.filter(name='استاد').exists():
            studentNames = []
            accStudentNames = []
            prjRequested = project.objects.filter(~Q(prj_student= None),prj_master = request.user, prj_accept = False).order_by('-prj_time')
            for req in prjRequested:
                studentNames.append(User.objects.filter(username = req.prj_student))
            
            prjAccepted = project.objects.filter(prj_master = request.user, prj_accept = True).order_by('-prj_time')
            for acc in prjAccepted:
                accStudentNames.append(User.objects.filter(username = acc.prj_student))
            # print(accStudentNames[0][0].username)
            prjNotRequested = project.objects.filter(prj_master = request.user, prj_accept = False, prj_student = None)
            return render(request,'panel/projectMaster.html',{'requested':prjRequested, 'notRequested': prjNotRequested, 'accepted':prjAccepted, 'std': studentNames, 'accstd': accStudentNames})
        else:
            print("\nWe have a problem in user (" + request.user.username + ") groups!\n")
            data = {"body": "گروه کاری شما در سامانه درست وارد نشده است. لطفا موضوع را با مدیر سیستم در میان گذارید"}
            return render(request, 'panel/error.html', {'data':data})
    else:
        return  redirect('login/')


def addProject(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='دانشجو').exists():
            data = {"body": "شما به این قسمت دسترسی ندارید. برای اطلاعات بیشتر موضوع را با مدیر سیستم در میان گذارید"}
            return render(request, 'panel/noPermission.html', {'data':data})


        elif request.user.groups.filter(name='استاد').exists():
            if request.method == 'GET':
                form = addProjectForm()
                return render(request, 'panel/addProject.html')
            else:
                form = addProjectForm(request.POST)
                print("add project POST method")
                print(request.POST.get("prj_title", ""))
                if form.is_valid():
                    print("form is valid")
                    prj = form.save(commit=False)
                    prj.prj_master = request.user
                    prj.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
                else:
                    print("form is not valiiiiiiiiiiiiid")
                    # return render(request, 'panel/error.html')

        else:
            print("\nWe have a problem in user (" + request.user.username + ") groups!\n")
            data = {"body": "گروه کاری شما در سامانه درست وارد نشده است. لطفا موضوع را با مدیر سیستم در میان گذارید"}
            return render(request, 'panel/error.html', {'data':data})
    else:
        return  redirect('login/')

def acceptProject(request, prjID):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='دانشجو').exists():
            data = {"body": "شما به این قسمت دسترسی ندارید. برای اطلاعات بیشتر موضوع را با مدیر سیستم در میان گذارید"}
            return render(request, 'panel/noPermission.html', {'data': data})

        elif request.user.groups.filter(name='استاد').exists():
            prj = project.objects.filter(id = prjID, prj_master = request.user)

            print(prj)
            if prj:
                accept_project = project.objects.get(id=prjID)
                accept_project.prj_accept = True
                accept_project.save()
                return redirect('project')
            else:
                data = {
                    "body": "پروژه ای با این کد برای شما تعریف نشده است!"}
                return render(request, 'panel/noPermission.html', {'data':data})


        else:
            print("\nWe have a problem in user (" + request.user.username + ") groups!\n")
            data = {"body": "گروه کاری شما در سامانه درست وارد نشده است. لطفا موضوع را با مدیر سیستم در میان گذارید"}
            return render(request, 'panel/error.html', {'data':data})
    else:
        return  redirect('login/')


def declineProject(request, prjID):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='دانشجو').exists():
            data = {"body": "شما به این قسمت دسترسی ندارید. برای اطلاعات بیشتر موضوع را با مدیر سیستم در میان گذارید"}
            return render(request, 'panel/noPermission.html', {'data': data})

        elif request.user.groups.filter(name='استاد').exists():
            prj = project.objects.filter(id = prjID, prj_master = request.user)

            print(prj)
            if prj:
                decline_project = project.objects.get(id=prjID)
                decline_project.prj_accept = False
                decline_project.prj_student = None
                decline_project.save()
                return redirect('project')
            else:
                data = {
                    "body": "پروژه ای با این کد برای شما تعریف نشده است!"}
                return render(request, 'panel/noPermission.html', {'data':data})


        else:
            print("\nWe have a problem in user (" + request.user.username + ") groups!\n")
            data = {"body": "گروه کاری شما در سامانه درست وارد نشده است. لطفا موضوع را با مدیر سیستم در میان گذارید"}
            return render(request, 'panel/error.html', {'data':data})
    else:
        return  redirect('login/')
    
    
def deleteProject(request, prjID):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='دانشجو').exists():
            data = {"body": "شما به این قسمت دسترسی ندارید. برای اطلاعات بیشتر موضوع را با مدیر سیستم در میان گذارید"}
            return render(request, 'panel/noPermission.html', {'data': data})

        elif request.user.groups.filter(name='استاد').exists():
            prj = project.objects.filter(id = prjID, prj_master = request.user)

            print(prj)
            if prj:
                delete_project = project.objects.get(id=prjID)
                delete_project.delete()
                return redirect('project')
                # return HttpResponse(delete_project)
            else:
                data = {
                    "body": "پروژه ای با این کد برای شما تعریف نشده است!"}
                return render(request, 'panel/noPermission.html', {'data':data})


        else:
            print("\nWe have a problem in user (" + request.user.username + ") groups!\n")
            data = {"body": "گروه کاری شما در سامانه درست وارد نشده است. لطفا موضوع را با مدیر سیستم در میان گذارید"}
            return render(request, 'panel/error.html', {'data':data})
    else:
        return  redirect('login/')
    


def editProject(request,prjID):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='دانشجو').exists():
            data = {"body": "شما به این قسمت دسترسی ندارید. برای اطلاعات بیشتر موضوع را با مدیر سیستم در میان گذارید"}
            return render(request, 'panel/noPermission.html', {'data':data})


        elif request.user.groups.filter(name='استاد').exists():
            if request.method == 'GET':
                form = editProjectForm()
                prj = project.objects.get(id = prjID)
                return render(request, 'panel/editProject.html', {'prj':prj})
            else:
                form = addProjectForm(request.POST)
                print("add project POST method")
                print(request.POST.get("prj_title"))
                if form.is_valid():
                    print("form is valid")
                    prj = project.objects.get(id=prjID)
                    prj.prj_title = request.POST.get("prj_title")
                    prj.save()
                    return redirect('project')
                else:
                    print("form is not valiiiiiiiiiiiiid")
                    # return render(request, 'panel/error.html')

        else:
            print("\nWe have a problem in user (" + request.user.username + ") groups!\n")
            data = {"body": "گروه کاری شما در سامانه درست وارد نشده است. لطفا موضوع را با مدیر سیستم در میان گذارید"}
            return render(request, 'panel/error.html', {'data':data})
    else:
        return  redirect('login/')
    

def selectProject(request, prjID):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='استاد').exists():
            data = {"body": "شما به این قسمت دسترسی ندارید. برای اطلاعات بیشتر موضوع را با مدیر سیستم در میان گذارید"}
            return render(request, 'panel/noPermission.html', {'data': data})

        elif request.user.groups.filter(name='دانشجو').exists():
            prj = project.objects.filter(id = prjID, prj_student= None)

            print(prj)
            if prj:
                select_project = project.objects.get(id=prjID)
                select_project.prj_student = request.user.username
                select_project.save()
                return redirect('project')
            else:
                data = {
                    "body": "پروژه درخواستی تعریف نشده و یا توسط دانشجویی دیگر انتخاب شده است!"}
                return render(request, 'panel/noPermission.html', {'data':data})


        else:
            print("\nWe have a problem in user (" + request.user.username + ") groups!\n")
            data = {"body": "گروه کاری شما در سامانه درست وارد نشده است. لطفا موضوع را با مدیر سیستم در میان گذارید"}
            return render(request, 'panel/error.html', {'data':data})
    else:
        return  redirect('login/')