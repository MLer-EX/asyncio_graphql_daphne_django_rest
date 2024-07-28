# my_app/schema.py

import graphene
from graphene_django import DjangoObjectType
from .models import Item


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


class Query(graphene.ObjectType):
    all_items = graphene.List(ItemType)

    def resolve_all_items(root, info):
        return Item.objects.all()


class CreateItem(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    item = graphene.Field(ItemType)

    def mutate(self, info, name, description):
        item = Item(name=name, description=description)
        item.save()
        return CreateItem(item=item)


class UpdateItem(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        description = graphene.String()

    item = graphene.Field(ItemType)

    def mutate(self, info, id, name=None, description=None):
        item = Item.objects.get(pk=id)
        if name:
            item.name = name
        if description:
            item.description = description
        item.save()
        return UpdateItem(item=item)


class Mutation(graphene.ObjectType):
    create_item = CreateItem.Field()
    update_item = UpdateItem.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
