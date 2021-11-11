from django.conf.urls import url

from web.views.achievement_view import AchievementView
from web.views.auth_view import UserRegistrationView, UserLoginView, UserProfileView
from web.views.base_view import BaseView
from web.views.comment_view import CommentView
from web.views.payment_view import PaymentView, PostPaymentView
from web.views.submission_view import SubmissionView
from web.views.task_view import TaskView
from web.views.topic_view import TopicView

urlpatterns = [
    url(r'^$', BaseView.as_view()),
    url(r'^signUp/?$', UserRegistrationView.as_view()),
    url(r'^signIn/?$', UserLoginView.as_view()),
    url(r'^profile/?$', UserProfileView.as_view()),
    url(r'^topics/?$', TopicView.as_view()),
    url(r'^topics/(?P<primary_key>\d+)/?$', TopicView.as_view()),
    url(r'^tasks/?$', TaskView.as_view()),
    url(r'^tasks/(?P<primary_key>\d+)/?$', TaskView.as_view()),
    url(r'^comments/?$', CommentView.as_view()),
    url(r'^comments/(?P<primary_key>\d+)/?$', CommentView.as_view()),
    url(r'^submissions/?$', SubmissionView.as_view()),
    url(r'^submissions/(?P<primary_key>\d+)/?$', SubmissionView.as_view()),
    url(r'^achievements/?$', AchievementView.as_view()),
    url(r'^payment/(?P<primary_key>\d+)/?$', PaymentView.as_view()),
    url(r'^postpayment/(?P<email>[\w.@-]+)/(?P<session_id>[\w.-]+)/?$', PostPaymentView.as_view()),
]
