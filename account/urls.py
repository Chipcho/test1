from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView   #内置登陆 有问题

app_name = 'account'
urlpatterns = [
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('register/',views.register,name='user_register'),
    # url('login/',auth_views.LoginView,name='user_login'),  内置登陆 参数问题 未搞懂 先放一放
    # # url('new-login/',auth_views.LoginView,{"template_name":"account/login.html"}), 内置登陆 参数问题 未搞懂 先放一放
    path('password-change/',PasswordChangeView.as_view(success_url="/account/password-change-done"),name='password_change'), #内置修改密码视图,这里始终报错，未解决；实际上是密码修改成功，只是无法跳转到相应的网页
    path('password-change-done/',PasswordChangeDoneView.as_view(),name='password_change_done'), #内置修改密码视图
    path('password-reset/',PasswordResetView.as_view(template_name="account/password_reset_form.html",
    	email_template_name="account/password_reset_email.html",
    	subject_template_name="account/password_reset_subject.txt",
    	success_url="account/password-reset-done",
    	from_email="1157359564@qq.com"),name="password_reset"),
    path('password-reset-done',PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"),name="password_reset_done"),
    path('password-reset-confirm/<uid64>/<token>/',PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html",success_url="password_reset_complete"),name="password_reset_confirm"),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"),name="password_reset_complete"),
    path('my-information/',views.myself,name="my_information"),
    path('edit-my-information/',views.myself_edit,name="edit_my_information"),
    path('my-image/',views.my_image,name="my_image"),



]