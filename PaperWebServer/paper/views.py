import datetime
import json
import math
import os

from django.shortcuts import render, HttpResponse
from paper.models import *
from django.http import JsonResponse, FileResponse, StreamingHttpResponse
from django.core import serializers
from django.db.models import Q
# from django.core.paginator import Paginator

# Create your views here.

# 查询论文
def get_paper(request):
    # page = 1 if request.GET.get('page') == None else request.GET.get('page')
    # per_page = 10
    try:
        title = request.GET.get('title')
        type = request.GET.get('type')
        isequal = request.GET.get('isequal')
        req_key = title.split(';')
        q = Q()
        if isequal == '0':
            if type == 'author':
                for item in req_key:
                    q.children.append(('paper_author__iexact', item))
            elif type == 'source':
                if len(req_key) != 1:
                    raise Exception('输入查询条件过多，请减少查询条件')
                # print(req_key[0])
                q.children.append(('paper_source__source_name__iexact', req_key[0]))
            elif type == 'keywords':
                for item in req_key:
                    q.children.append(('paper_keywords__iexact', item))
            elif type == 'abstract':
                for item in req_key:
                    q.children.append(('paper_abstract__iexact', item))
            elif type == 'title':
                for item in req_key:
                    q.children.append(('paper_title__iexact', item))
            else:
                raise Exception('查询类型选择错误')

        else:
            if type == 'author':
                for item in req_key:
                    q.children.append(('paper_author__icontains', item))
            elif type == 'source':
                if len(req_key) != 1:
                    raise Exception('输入查询条件过多，请减少查询条件')
                q.children.append(('paper_source__source_name__icontains', req_key[0]))
            elif type == 'keywords':
                for item in req_key:
                    q.children.append(('paper_keywords__icontains', item))
            elif type == 'abstract':
                for item in req_key:
                    q.children.append(('paper_abstract__icontains', item))
            elif type == 'title':
                for item in req_key:
                    q.children.append(('paper_title__icontains', item))
            else:
                raise Exception('查询类型选择错误')
        papers = PaperMainInfoModel.objects.filter(q).filter(data_status=True)
        # print(papers)
        res = {
            'status': True,
            'main_data': [],
            'msg': ''
        }
        if len(papers) == 0:
            raise Exception('没有找到相关数据，请更换关键字')

        for paper in papers:
            cited = 0
            download = 0
            try:
                cited = paper.papercitedcountmodel.cited_times
            except Exception as e:
                print(str(e))
            try:
                download = paper.paperdownloadcountmodel.download_count
            except Exception as e:
                print(str(e))

            res['main_data'].append({
                'pk': paper.pk,
                'title': paper.paper_title,
                'author': paper.paper_author,
                'source': paper.paper_source.source_name,
                'publish_year': paper.paper_publish_year,
                'cited': cited,
                'download': download
            })
            res['msg'] = '获取信息成功'
        return JsonResponse(res)
    except Exception as e:
        return JsonResponse({
            'status': False,
            'main_data': [],
            'msg': str(e)
        })

# 查询论文数量
def get_paper_count(request):
    res = []
    try:
        # now = datetime.datetime.now()
        # six_month_ago = now - datetime.timedelta(days=180)
        total_count = PaperMainInfoModel.objects.all().count()
        # recent_count = PaperMainInfoModel.objects.filter(edit_date__gte=six_month_ago)
        if total_count > 0:
            res.append({
                'status': True,
                'count': total_count,
                'recount': 0,
                'msg': '获取论文数量成功'
            })
        else:
            res.append({
                'status': False,
                'count': 0,
                'recount': 0,
                'msg': '获取论文数量为0'
            })
    except Exception as e:
        res.append({
            'status': False,
            'count': 0,
            'recount': 0,
            'msg': str(e)
        })
    return JsonResponse(res, safe=False)

# 查询单篇论文详细信息
def get_paper_detail_data(request):
    # 要考虑到两种情况
    #  第一种是url没有传参
    #  第二种是传参没有找到对象
    res = {
        'status': True,
        'detail_data': {},
        'msg': '获取数据成功'
    }
    pk = request.GET.get('pk')
    print('主键:',pk)
    if pk == None:
        return JsonResponse({
        'status': False,
        'detail_data': {},
        'msg': '查询条件不足'
    })
    try:

        paper = PaperMainInfoModel.objects.filter(id=pk).filter(data_status=True)
        if len(paper) == 0:
            res['status'] = False
            res['msg'] = '查询文章不存在'
        else:
            paper_info = paper[0]
            file_path = paper_info.paperfilepathmodel_set.all().filter(data_status=True)
            # print(file_path)
            file_path_list = []
            for item in file_path:
                file_path_list.append(str(item.file_path))
                # print(str(item.file_path))
            print(file_path_list)
            res['detail_data'] = {
                'pk': paper_info.id,
                'title': paper_info.paper_title,
                'author': paper_info.paper_author,
                'publish_year': paper_info.paper_publish_year,
                'keywords': paper_info.paper_keywords.split(';'),
                'abstract': paper_info.paper_abstract,
                'affiliations': paper_info.paper_affiliations,
                'source': paper_info.paper_source.source_name,
                'language': paper_info.paperdetailinfomodel.paper_language,
                'volume': paper_info.paperdetailinfomodel.paper_volume,
                'issue': paper_info.paperdetailinfomodel.paper_issue,
                'page': paper_info.paperdetailinfomodel.paper_page,
                'doi': paper_info.paperdetailinfomodel.paper_doi,
                'ids': paper_info.paperdetailinfomodel.paper_ids,
                'wos': paper_info.paperdetailinfomodel.paper_wos,
                'cited_reference': paper_info.papercitedcountmodel.cited_reference_count,
                'cited_times': paper_info.papercitedcountmodel.cited_times,
                'download': paper_info.paperdownloadcountmodel.download_count,
                'file_path': file_path_list
            }
    except Exception as e:
        res['status'] = False
        res['msg'] = str(e)

    return JsonResponse(res)

# 保存意见
def send_comment(request):
    res = {
        'status': True,
        'msg': '提交成功，我们已经收到您的意见和建议，我们将尽快处理。已跳转至首页！'
    }
    try:
        name_send = request.GET.get('name')
        email_send = request.GET.get('email')
        comment_send = request.GET.get('comment')
        comment = CommentAndSuggestModel()
        comment.name = name_send
        comment.email = email_send
        comment.comment = comment_send
        comment.save()
        print(name_send, email_send, comment_send)
    except Exception as e:
        res = {
            'status': False,
            'msg': str(e)
        }
    return JsonResponse(res)


# 下载文件
def download_file(request):
    pk = request.GET.get('pk')
    print("pk:", pk)
    try:
        print("开始")
        file_path = PaperFilePathModel.objects.get(paper_id=pk).file_path
        path = str(file_path)

        paper_download = PaperDownloadCountModel.objects.get(paper_id=pk)
        print("文件下载次数：", paper_download.download_count)
        paper_download.download_count = paper_download.download_count + 1
        paper_download.save()

        return JsonResponse({
            'status': True,
            'data': {
                'filename': str(pk) + '.pdf',
                'filepath': path
            },
            'msg': '获取成功'
        })
    except Exception as e:
        return JsonResponse({
            'status': True,
            'data': {},
            'msg': str(e)
        })

