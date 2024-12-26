from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms.users.forms import UserForm, EditProfileForm, EditProfilePhotoForm
from .modelsProfile import Profile

@login_required
def get_user_profile(request):
    return render(request, "users/profile.html", {"user": request.user})


@login_required
def edit_user_profile(request):
    try:
        profile = request.user.profile  
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)  

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = EditProfilePhotoForm(request.POST, request.FILES, instance=profile)
        
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect('user_profile')
        else:
            messages.error(request, "Hubo un error al actualizar el perfil.")
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = EditProfilePhotoForm(instance=profile)

    return render(request, 'users/edit_profile.html', {'form': form, 'profile_form': profile_form})


@login_required
def change_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, "Tu contraseña ha sido cambiada correctamente.")
            return redirect('inicio')  
        else:
            messages.error(request, "Hubo un error al cambiar la contraseña.")
    else:
        password_form = PasswordChangeForm(request.user)  

    return render(request, 'users/change_password.html', {'form_password': password_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            messages.error(request, "Por favor, ingresa nombre de usuario y contraseña.")
            return render(request, "users/login.html")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("inicio")
            else:
                messages.error(request, "Tu cuenta está desactivada.")
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    
    return render(request, "users/login.html")

@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect("login")

def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data['password'])  
            user.save()  
            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect("inicio")  
        else:
            messages.error(request, "Error en el formulario. Revisa los campos.")
    else:
        form = UserForm()  

    return render(request, "users/register.html", {"form": form})
