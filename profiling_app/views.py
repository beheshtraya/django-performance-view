from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from profiling_app.models import RequestProfile
from django.db.models import Avg
import json


class PerformanceView(View):
    def get(self, request):
        average_db_time = RequestProfile.objects.all().aggregate(Avg('sql_query_time'))
        average_db_num_queries = RequestProfile.objects.all().aggregate(Avg('num_sql_queries'))
        average_db_joins = RequestProfile.objects.all().aggregate(Avg('num_sql_joins'))

        output = dict()
        output['time'] = average_db_time
        output['sql'] = average_db_num_queries
        output['joins'] = average_db_joins

        return HttpResponse(json.dumps(output))
