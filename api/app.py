from wsgiref.simple_server import make_server

import falcon

class CheckpointResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_JSON  # Default is JSON, so override
        resp.media = {"message": "Falcon is serving"}

app = falcon.App()
checkpoint = CheckpointResource()
app.add_route('/checkpoint', checkpoint)


if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()