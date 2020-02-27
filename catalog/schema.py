import graphene

from graphene_django.types import DjangoObjectType

from catalog.models import Category, Product

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class Query:
    all_categories = graphene.List(CategoryType)
    all_products = graphene.List(ProductType)

    category = graphene.Field(CategoryType, id=graphene.Int(), name=graphene.String())
    product = graphene.Field(ProductType, id=graphene.Int())

    def resolve_category(self, info, **kwargs):
        if 'id' in kwargs:
            return Category.objects.get(id=kwargs['id'])
        if 'name' in kwargs:
            return Category.objects.get(name=kwargs['name'])
        return None

    def resolve_product(self, info, **kwargs):
        if 'id' in kwargs:
            return Product.objects.get(id=kwargs['id'])
        if 'name' in kwargs:
            return Product.objects.get(name=kwargs['name'])
        return None


    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()



