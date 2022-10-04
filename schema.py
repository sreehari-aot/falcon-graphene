from marshmallow import Schema, fields, EXCLUDE


class CountrySchema(Schema):
    """Schema for the individual country details."""
    
    class Meta:
        """Exclude unknown fields from the deserialized output."""
        unknown = EXCLUDE

    name = fields.Dict(data_key="name", required=True)
    currencies = fields.Dict(data_key="currencies", required=False)
    capital = fields.List(fields.Str(), data_key="capital", required=False)
    language = fields.Dict(data_key="languages", required=False)
    latlng = fields.List(fields.Float(), data_key="latlng", required=True)
    maps = fields.Dict(data_key="maps", required=True)
    population = fields.Int(data_key="population", required=True)
    continents = fields.List(fields.Str(), data_key="continents", required=True)
    flags = fields.Dict(data_key="flags", required=True)
    postal_code = fields.Dict(data_key="postalCode", required=False)
