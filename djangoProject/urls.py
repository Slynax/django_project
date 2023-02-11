from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Polls_and_surveys.views.DeleteQuiz import DeleteQuizView
from Polls_and_surveys.views.Sub_Categories import Sub_CategoriesView

from Polls_and_surveys.views.create_question import CreateQuestionView
from Polls_and_surveys.views.create_quiz import CreateQuizView
from Polls_and_surveys.views.index import IndexView
from Polls_and_surveys.views.login import LoginView
from Polls_and_surveys.views.logout import LogoutView
from Polls_and_surveys.views.my_questions import MyQuestionsView
from Polls_and_surveys.views.my_quiz import MyQuizView
from Polls_and_surveys.views.quiz import QuizView
from Polls_and_surveys.views.redirect_index import RedirectIndexView
from Polls_and_surveys.views.register_forms import RegisterFormView
from Polls_and_surveys.views.update_score import UpdateScoreView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('sub_categories/<int:pk>', Sub_CategoriesView.as_view(), name='sub_categories'),
    path('quiz/<int:pk>', QuizView.as_view(), name='quiz'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterFormView.as_view(), name='register'),
    path('update_score/', UpdateScoreView.as_view(), name='update_score'),
    path('create_question/', CreateQuestionView.as_view(), name='create_question'),
    path('create_quiz/', CreateQuizView.as_view(), name='create_quiz'),
    path('my_quiz/', MyQuizView.as_view(), name='my_quiz'),
    path('my_questions/<int:pk>', MyQuestionsView.as_view(), name='my_questions'),
    path('delete_quiz/<int:pk>', DeleteQuizView.as_view(), name='delete_quiz'),
    path('quiz/redirect_index/', RedirectIndexView.as_view(), name='redirect_index'),
    path('my_questions/redirect_index/', RedirectIndexView.as_view(), name='redirect_index'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)