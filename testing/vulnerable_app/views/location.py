"""
These endpoints focus on accepting input from a variety of different locations.
"""
from flask_restplus import Resource

from ..core.extensions import api
from ..models.basic import string_model
from ..parsers.basic import location_parser
from ..util import get_name


ns = api.namespace(
    get_name(__name__),
    url_prefix='/{}'.format(get_name(__name__)),
)


@api.marshal_with(string_model.format)
@ns.route('/<path_id>')
class VariousLocations(Resource):
    @api.expect(location_parser)
    def post(self, path_id):
        return string_model.output()