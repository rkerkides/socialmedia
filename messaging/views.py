from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.decorators import login_required
from .forms import SendMessageForm


def index(request):
    return render(request, 'messaging/index.html')

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'messaging/inbox.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                sender=request.user,
                receiver=form.cleaned_data['receiver'],
                content=form.cleaned_data['content']
            )
            return redirect('inbox')  # Redirect to the inbox after sending
    else:
        form = SendMessageForm()

    return render(request, 'messaging/send_message.html', {'form': form})


def detail(request, message_id):
    return HttpResponse("You're looking at message %s." % message_id)
