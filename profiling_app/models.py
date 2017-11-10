from django.db import models


class RequestProfile(models.Model):
    request = models.CharField(max_length=255)
    num_sql_queries = models.IntegerField(default=0)
    num_sql_joins = models.IntegerField(default=0)
    sql_query_time = models.FloatField(default=0)
