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