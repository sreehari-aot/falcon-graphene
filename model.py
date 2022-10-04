from mongoengine import Document, ListField, StringField, IntField, DictField, FloatField


class Country(Document):
    """Defines fields for the country."""
    
    name = DictField(required=True)
    currencies = DictField(required=False)
    capital = ListField(StringField(), required=False)
    language = DictField(required=False)
    latlng = ListField(FloatField(), required=True)
    maps = DictField(required=True)
    population = IntField(required=True)
    continents = ListField(StringField(), required=True)
    flags = DictField(required=True)
    postal_code = DictField(required=False)