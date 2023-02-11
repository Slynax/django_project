from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from Polls_and_surveys.models.myuser import MyUser
from Polls_and_surveys.models.score import Score


class UpdateScoreView(View, LoginRequiredMixin):

    def post(self, request):
        correct = request.POST.get('correct')
        user_id = request.POST.get('userid')

        user = MyUser.objects.get(username=user_id)
        score, created = Score.objects.get_or_create(user=user)

        if created:
            if correct == "True":
                score.score = 10
            else:
                score.score = 0
        else:
            if correct == "True":
                score.score += 10
            elif score.score >= 10:
                score.score -= 10
            else:
                score.score = 0
        score.save()

        return HttpResponse(str(score.score))
