from paper.views import *
from django.urls import path, include

urlpatterns = [
    path('get_paper', get_paper),
    path('get_paper_count', get_paper_count),
    path('get_paper_detail_data', get_paper_detail_data),
    path('send_comment', send_comment),
    path('download_file', download_file)
]
