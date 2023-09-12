from django.db import models
from django.utils.timezone import now, utc
from utils import *


# 期刊/会议/图书等 详细信息
class SourceDetailInfoModel(models.Model):
    # 来源名称
    source_name = models.CharField(max_length=255, unique=True)
    # 来源类型：期刊/会议/图书等
    source_type = models.CharField(max_length=2, default='J')
    # 会议专用 - 会议日期
    source_date = models.CharField(max_length=50, null=True, blank=True)
    # 举办地：
    #   会议 - 会议举办地
    #   期刊 - 期刊举办地
    source_location = models.CharField(max_length=255, null=True, blank=True)
    # 出版商
    source_publisher = models.CharField(max_length=1024, null=True, blank=True)
    # ISSN
    source_issn = models.CharField(max_length=255, null=True, blank=True)
    # eISSN
    source_eissn = models.CharField(max_length=255, null=True, blank=True)
    # ISBN
    source_isbn = models.CharField(max_length=255, null=True, blank=True)
    # 缩写
    source_abbreviation = models.CharField(max_length=255, null=True, blank=True)
    # 文章状态
    # 1 :   启用
    # 0 :   禁用
    data_status = models.BooleanField(default=True)
    # 编辑日期
    edit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'db_source_detail_info'

    def __str__(self):
        return self.source_name

    def __repr__(self):
        return self.source_name


# 文章主要信息 - 主要用于首页查询和展示文章
class PaperMainInfoModel(models.Model):
    # # paper_id 由10位组成
    # #   1   :   'P'
    # #   2   :   出版商首字母
    # #   3   :   期刊首字母
    # #   4   :   文章首字母
    # #   5   :   作者首字母
    # #   6-9 :   出版年份
    # #   10  :   0-9的循环
    # paper_id = models.CharField(max_length=10, primary_key=True)
    # 文章标题
    paper_title = models.CharField(max_length=255)
    # 文章作者
    paper_author = models.CharField(max_length=255)
    # 出版年份
    paper_publish_year = models.IntegerField(null=True, blank=True)
    # 文章关键字
    paper_keywords = models.CharField(max_length=1024, null=True, blank=True)
    # 文章摘要
    paper_abstract = models.TextField(null=True, blank=True)
    # 文章所属单位
    paper_affiliations = models.CharField(max_length=1024, null=True, blank=True)
    # 文章来源期刊/会议/书籍等的名称
    paper_source = models.ForeignKey(SourceDetailInfoModel, on_delete=models.PROTECT, db_column='source_id')
    # 文章状态
    # 1 :   启用
    # 0 :   禁用
    data_status = models.BooleanField(default=True)
    # 编辑日期
    edit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'db_paper_main_info'

    def __str__(self):
        return f'{self.paper_title} -- {self.paper_publish_year}'

    def __repr__(self):
        return f'{self.paper_title} -- {self.paper_publish_year}'


# 文章详细信息 - 主要用于文章详细页信息展示
class PaperDetailInfoModel(models.Model):
    # 与文章主要信息一对一
    paper_id = models.OneToOneField(PaperMainInfoModel, on_delete=models.PROTECT, db_column='paper_id', unique=True)
    # 文章语言
    paper_language = models.CharField(max_length=20, default='English', null=True, blank=True)
    # Volume
    paper_volume = models.CharField(max_length=10, null=True, blank=True)
    # Issue
    paper_issue = models.CharField(max_length=10, null=True, blank=True)
    # Pages
    paper_page = models.CharField(max_length=255, null=True, blank=True)
    # DOI
    paper_doi = models.CharField(max_length=255, null=True, blank=True)
    # IDS
    paper_ids = models.CharField(max_length=255, null=True, blank=True)
    # WOS
    paper_wos = models.CharField(max_length=255, null=True, blank=True)
    # 状态
    # 1 :   启用
    # 0 :   禁用
    data_status = models.BooleanField(default=True)
    # 编辑日期
    edit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'db_paper_detail_info'


# 文章其他信息
# 文章原始信息


# 文件存储链接
class PaperFilePathModel(models.Model):
    # 文件路径
    file_path = models.FileField(upload_to='static/papers', null=True)
    # 对应文章 id
    #   文章与文件存在一对多的关系，一篇文章可能对应多个文件
    paper_id = models.ForeignKey(PaperMainInfoModel, on_delete=models.PROTECT, db_column='paper_id')
    # 状态
    # 1 :   启用
    # 0 :   禁用
    data_status = models.BooleanField(default=True)
    # 编辑日期
    edit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'db_paper_file_path'

    def __str__(self):
        return f'{self.paper_id.id}'

    def __repr__(self):
        return f'{self.paper_id.id}'

# 文章下载计数
class PaperDownloadCountModel(models.Model):
    # 下载计数
    download_count = models.IntegerField(default=0)
    # 对应文章
    paper_id = models.OneToOneField(PaperMainInfoModel, on_delete=models.CASCADE, db_column='paper_id', unique=True)
    # 状态
    # 1 :   启用
    # 0 :   禁用
    data_status = models.BooleanField(default=True)
    # 编辑日期
    edit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'db_paper_download_count'


# 文章引用文献数与被引次数
class PaperCitedCountModel(models.Model):
    # 引用文章数
    cited_reference_count = models.IntegerField(default=0)
    # 被引次数
    cited_times = models.IntegerField(default=0)
    # 对应文章
    paper_id = models.OneToOneField(PaperMainInfoModel, on_delete=models.CASCADE, db_column='paper_id', unique=True)
    # 状态
    # 1 :   启用
    # 0 :   禁用
    data_status = models.BooleanField(default=True)
    # 编辑日期
    edit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'db_paper_cited_count'


# 文章配置


# 意见与建议
class CommentAndSuggestModel(models.Model):
    name = models.CharField(max_length=100, default='ICost')
    email = models.EmailField(null=True, blank=True)
    comment = models.TextField(max_length=1024)
    unsolved = models.BooleanField(default=True)
    create_date = models.DateTimeField(default=utcnow)
    edit_date = models.DateTimeField(auto_now=True)

    class Mete:
        db_table = 'db_comment_and_suggest'

    def __str__(self):
        return f'{self.name} -- {self.email}'

    def __repr__(self):
        return f'{self.name} -- {self.email}'



