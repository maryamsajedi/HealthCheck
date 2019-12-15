import graphene
# import graphql_jwt

from services.schema  import ServiceMutation, ServiceQuery

class Query(
    ServiceQuery,
    graphene.ObjectType
):
    pass

class Mutations(
    ServiceMutation,
):
    pass

schema = graphene.Schema(query = Query, mutation = Mutations)
