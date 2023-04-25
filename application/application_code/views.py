from django.shortcuts import render, redirect,get_object_or_404

from .django_forms import MemberCreationForm,MemberChangeForm,MemberTasksForm,CategoryForm

from django.contrib import messages

from .models import Category,Member


def create_new_member_view(request):
    url_path = request.path
    if request.user.is_active and "logout" not in url_path:
        return redirect('member_dashboard')

    if request.method == 'POST':
        print("posting")
        member_form = MemberCreationForm(request.POST)
        if member_form.is_valid():
            print("valid form")
            member_first_name = member_form.cleaned_data["first_name"]
            member_last_name = member_form.cleaned_data["last_name"]
            password = member_form.cleaned_data["password"]
            member_email = member_form.cleaned_data["email"]
            member_mobile_number = member_form.cleaned_data["mobile_number"]
            member = Member.objects.create(first_name=member_first_name,last_name=member_last_name,email=member_email,username=member_mobile_number,mobile_number=member_mobile_number)
            member.set_password(password)
            member.save()

            from allauth.account.utils import perform_login
            from allauth.account import app_settings as allauth_settings
            perform_login(request, member, allauth_settings.EMAIL_VERIFICATION, signup=False,
                          redirect_url=None, signal_kwargs=None)
            return redirect('member_dashboard')
        else:
            print(member_form.errors)
            return render(request, 'create_member.html', {'member_form': member_form, 'errors': member_form.errors})
    else:
        member_form = MemberCreationForm()
    return render(request, 'create_member.html', {'member_form': member_form})

def member_profile(request):
    member = request.user
    if not member.is_active:
        return redirect('create_member')
    context = {
        'member': member,
    }
    return render(request, 'member_profile.html', context)


def member_dashboard(request):
    member = request.user
    if not member.is_active:
        return redirect('create_member')
    context = {
        'member': member,
    }
    return render(request, 'member_dashboard.html', context)


def update_member_profile(request):
    member = request.user
    if not member.is_active:
        return redirect('create_member')
    if request.method == 'POST':
        form = MemberChangeForm(request.POST)
        if form.is_valid():
            member_first_name = form.cleaned_data["first_name"]
            member_last_name = form.cleaned_data["last_name"]
            member_email = form.cleaned_data["email"]
            member_mobile_number = form.cleaned_data["mobile_number"]
            member.first_name = member_first_name
            member.last_name = member_last_name
            member.email = member_email
            member.mobile_number = member_mobile_number
            member.save()
            messages.add_message(request,messages.SUCCESS,"Your profile details updated successfully.")
            return redirect('profile')
    else:
        form = MemberChangeForm()
        form.fields["first_name"].initial = member.first_name
        form.fields["last_name"].initial = member.last_name
        form.fields["email"].initial = member.email
        form.fields["mobile_number"].initial = member.mobile_number
    context = {
        'form': form,
    }
    return render(request, 'update_profile.html', context)


def delete_member_profile(request):
    member = request.user
    if not member.is_active:
        return redirect('create_member')
    member.is_active = False
    member.save()
    return redirect('create_member')

from .models import MemberTasks
from .django_forms import MemberTasksForm


def add_task(request):
    if request.method == 'POST':
        form = MemberTasksForm(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data["name"]
            due_date = form.cleaned_data["due_date"]
            is_task_completed = form.cleaned_data["is_task_completed"]
            description = form.cleaned_data["description"]
            MemberTasks.objects.create(member=request.user, name=task_name, due_date=due_date,
                                       is_task_completed=is_task_completed, description=description)
            messages.add_message(request,messages.SUCCESS,"You are successfully added the task.")
            return redirect('show_tasks')
    else:
        form = MemberTasksForm()
    return render(request, 'add_task.html', {'form': form})


def edit_task(request, task_id):
    task = get_object_or_404(MemberTasks, pk=task_id, member_id=request.user.pk)
    if request.method == 'POST':
        form = MemberTasksForm(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data["name"]
            due_date = form.cleaned_data["due_date"]
            is_task_completed = form.cleaned_data["is_task_completed"]
            description = form.cleaned_data["description"]
            task.name = task_name
            task.due_date = due_date
            task.is_task_completed = is_task_completed
            task.description = description
            task.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Your task " + str(task_id) + " details updated successfully.")
            return redirect('show_tasks')
    else:
        form = MemberTasksForm()
        form.fields["name"].initial = task.name
        form.fields["description"].initial = task.description
        if task.is_task_completed:
            form.fields["is_task_completed"].initial = task.is_task_completed
        from datetime import datetime
        due_date = datetime.strptime(str(task.due_date), '%Y-%m-%d').strftime('%m/%d/%Y')
        form.fields["due_date"].initial = due_date
    return render(request, 'edit_task.html', {'form': form, 'task': task,'task_id':task_id})

def delete_task(request, task_id):
    task = get_object_or_404(MemberTasks, pk=task_id)
    task.delete()
    messages.add_message(request,messages.SUCCESS,"Your task " + str(task_id) + " deleted successfully.")
    return redirect('show_tasks')

def show_tasks(request):
    tasks = MemberTasks.objects.filter(member=request.user)
    return render(request,'show_tasks.html',{'tasks':tasks})

def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            Category.objects.create(member=request.user,name=name,description=description)
            messages.success(request, 'Category has been added successfully!')
            return redirect('show_categories')
    context = {
        'form': form
    }
    return render(request, 'add_category.html', context)


def edit_category(request, category_id):
    category = Category.objects.get(category_id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            category.name = name
            category.description = description
            category.save()
            messages.success(request, 'Category has been updated successfully!')
            return redirect('show_categories')
    else:
        form = CategoryForm()
        form.fields["name"].initial = category.name
        form.fields["description"].initial = category.description
    return render(request, 'update_category.html', {'form':form})

def delete_category(request, category_id):
    task = get_object_or_404(Category, category_id=category_id)
    task.delete()
    return redirect('show_categories')

def show_categories(request):
    categories = Category.objects.filter(member=request.user)
    return render(request,'show_categories.html',{'categories':categories})