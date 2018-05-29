from django.contrib.auth import admin
from django.urls import include, path

from classroom.views import classroom, students, teachers

urlpatterns = [
    path('', include('classroom.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', classroom.SignUpView.as_view(), name='signup'),
    path('signup/estudiante/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('signup/maestro/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
]
