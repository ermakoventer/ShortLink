from django.contrib import admin
from django.urls import path, include
from users import views as userView
from django.contrib.auth import views as authViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('short_app.urls')),

    path('reg', userView.register, name='reg'),
    # path('user', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),


    path('', include('users.urls'))
]
