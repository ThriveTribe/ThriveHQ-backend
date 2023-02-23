from django.shortcuts import render
from .models import Thrive


def my_tasks(request):
    # Get the current user
    current_user = request.user

    # Filter the tasks by the current user
    tasks = Thrive.objects.filter(user=current_user)

    # Render the template with the tasks
    return render(request, 'my_tasks.html', {'tasks': tasks})
