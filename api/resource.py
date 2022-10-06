import falcon
import json
from schema import schema


class CountryResource:
    """Resource for countries."""

    def on_post(self, req, resp):
        """Handles POST requests"""
        query = req.media.get("query")
        if not query:
            raise falcon.HTTPError(falcon.HTTP_404,"query not provided")
        result = schema.execute(query)

        #TODO: Pagination
        #pagination should be done at the database layer
        if result.errors:
            print(result.errors[0])
            error = {"error": "Invalid request"}
            resp.status = falcon.HTTP_404
            resp.text = json.dumps(error, separators=(",", ":"))
    
        if result.data:
            data_ret = {"data": result.data}
            resp.status = falcon.HTTP_200
            resp.text = json.dumps(data_ret, separators=(",", ":"))
