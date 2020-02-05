import graphene

from services.schema  import ServiceMutation


class Mutations(
    ServiceMutation,
):
    pass

schema = graphene.Schema(mutation = Mutations)
