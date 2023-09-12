from django.contrib import admin
from paper.models import *
# Register your models here.

admin.site.register(SourceDetailInfoModel)
admin.site.register(PaperMainInfoModel)
admin.site.register(PaperDetailInfoModel)
admin.site.register(PaperFilePathModel)
admin.site.register(PaperCitedCountModel)
admin.site.register(PaperDownloadCountModel)
admin.site.register(CommentAndSuggestModel)
