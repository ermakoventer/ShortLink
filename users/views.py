from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(
        request,
        'users/register.html', 
        {
            'title': 'Страница регистрации',
            'form': form
            }
        )

        
@login_required
def profile(request):
    if request.method == "POST":
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if updateUserForm.is_valid():
            updateUserForm.save()
            return redirect('profile')

    else:
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'updateUserForm': updateUserForm
    }
    return render(request, 'users/profile.html', data)


# @login_required
# def index(request):
#     if request.method == "POST":
#         tut = Url(request.POST)
#         if tut.is_valid():
#             url = tut.cleaned_data["url"]
#             slug = tut.cleaned_data['slug']
#             new_url = UrlData(url=url, slug=slug)
#             new_url.save()
#             return redirect('links')
#     else:
#         tut = Url()

#     data = {
#         'news': UrlData.objects.all()
        
#     }
#     return render(
#         request,
#         'users/links.html', 
#         {
#             'tut': tut,
#             'news': UrlData.objects.all()
#             }
#         )