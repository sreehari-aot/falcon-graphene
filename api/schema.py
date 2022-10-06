import graphene

from math import inf
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from model import Country as CountryModel
from utils import nearest


class Country(MongoengineObjectType):
    class Meta:
        model=CountryModel

class Query(graphene.ObjectType):
    node=Node.Field()
    countries=graphene.List(Country)
    country=graphene.Field(Country, id=graphene.String(), required=True)
    nearby=graphene.List(Country, coordinates=graphene.List(graphene.Float), required=True)
    lang=graphene.List(Country, language=graphene.String(), required=True)

    def resolve_countries(root, info):
        return list(CountryModel.objects.all())

    def resolve_country(root, info, id):
        try:
            return CountryModel.objects.get(id=id)
        except Exception as err:
            raise err
    def resolve_nearby(root, info, coordinates):
        countries = [country for country in CountryModel.objects.all()]
        countries.sort(key=lambda country: nearest(coordinates, country) or inf)
        return list(countries[0:3])
    def resolve_lang(root, info, language):
        countries = CountryModel.objects.all()
        def lang_filter(object):
            if object.language is not None:
                for key in object.language:
                    if object.language[key] == language:
                        return True
            return False
        lang_filter = filter(lang_filter, countries)
        return lang_filter

class CountryMutation(graphene.Mutation):

    class Arguments:
        id = graphene.String(required=True)
        population = graphene.Int(required=True)

    ok = graphene.Boolean()
    country = graphene.Field(Country)
    
    def mutate(root, info, id, population):
        country = CountryModel.objects.get(id=id)
        country.population = population
        country.save()
        ok=True

        return CountryMutation(country=country, ok=ok)

class Mutations(graphene.ObjectType):
    update_country = CountryMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
