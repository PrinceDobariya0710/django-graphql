import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Book


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"
        filter_fields = {
            "title": ["exact", "icontains", "istartswith"],
            "author": ["exact", "icontains"],
            "published_date": ["exact", "gt", "lt"],
        }
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    book = graphene.relay.Node.Field(BookType)
    all_books = DjangoFilterConnectionField(BookType)


schema = graphene.Schema(query=Query)
