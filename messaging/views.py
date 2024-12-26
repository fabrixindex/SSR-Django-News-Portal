from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Message

@login_required(login_url="login")
def send_message(request):
    if request.method == "POST":
        receiver_username = request.POST.get("receiver")
        content = request.POST.get("content")

        if not content.strip():
            messages.error(request, "El contenido del mensaje no puede estar vacío.")
            return redirect("send_message")

        receiver = get_object_or_404(User, username=receiver_username)

        if receiver == request.user:
            messages.error(request, "No puedes enviarte un mensaje a ti mismo.")
            return redirect("send_message")

        Message.objects.create(sender=request.user, receiver=receiver, content=content)
        messages.success(request, f"Mensaje enviado a {receiver.username}.")
        return redirect("inicio")

    users = User.objects.exclude(username=request.user.username)
    return render(request, "messaging/send_message.html", {"users": users})

@login_required(login_url="login")
def show_messages(request):
    messages = Message.objects.filter(receiver=request.user).order_by("-shipping_date")

    return render(request, "messaging/show_messages.html", {
        "messages": messages,
    })

