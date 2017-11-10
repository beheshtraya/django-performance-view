from django.db import connection
from profiling_app.models import RequestProfile


class ProfilingMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):

        response = self.get_response(request)

        sql = ""
        sql_time = float()
        for item in connection.queries:
            sql += item['sql']
            sql_time += float(item['time'])

        RequestProfile.objects.create(
            request=request.path,
            num_sql_queries=len(connection.queries),
            num_sql_joins=sql.count('JOIN'),
            sql_query_time=sql_time
        )

        return response
