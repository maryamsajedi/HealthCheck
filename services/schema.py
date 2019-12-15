import os
import graphene
import logging
import urllib.request
from graphene_django.types      import DjangoObjectType
from services.models            import Service
from celery.decorators          import task


class ServiceNode(DjangoObjectType):
    class Meta:
        model = Service
        interfaces = (graphene.relay.Node, )

class ServiceQuery(graphene.ObjectType):
    retrieve_service = graphene.Field(ServiceNode)

class HealthCheck(graphene.Mutation):
    class Arguments:
        url = graphene.String()
        status_code = graphene.Int()
        # port = graphene.Int()
        delay = graphene.Float()

    error = graphene.String()
    result = graphene.Boolean()

    def mutate(self, info, **kwargs):
        url = kwargs.get('url', None)
        status_code = kwargs.get('status_code', None)
        try:
            req = urllib.request.urlopen(url)
        except Exception as e:
            return HealthCheck(
                result = False,
                error = "url is not valid"
            )
        print(req.status)
        if req.status == 200:
            print("ok")

class ServiceMutation(graphene.ObjectType):
    health_check = HealthCheck.Field()