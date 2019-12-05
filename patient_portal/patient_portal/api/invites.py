from flask_restplus import Namespace, Resource, fields
from flask import request, render_template
from datetime import datetime, timedelta
from .. import services

nsp = Namespace('invites', description="Patient Portal's invite API")

invite_fields = nsp.model('Invite', {
    'invite_id': fields.String(required=True, description='Invite unique id.'),
    'invited_by': fields.String(required=True, description='User having created the invite.'),
    'user_role_id': fields.String(required=True, description='Assigned user role to invite.'),
    'invited_email': fields.String(required=True, description="Invitee's email."),
    'invited_forename': fields.String(required=True, description="Invitee's first name."),
    'invited_surname': fields.String(required=True, description="Invitee's first name."),
    'invited_on_utc': fields.DateTime(required=True),
    'assign_to_location': fields.String(required=True),
    'expiration_date_utc': fields.DateTime(required=True),
    'is_consumed': fields.Boolean(required=True, default=False),
})

@nsp.route('/')
@nsp.response(200, 'Invite query executed successfully.')
@nsp.response(500, 'Internal server error.')
@nsp.response(403, 'Not authorized.')
class Invites(Resource):
    @nsp.marshal_list_with(invite_fields)
    def get(self):
        """Get all invitations created in the platform"""
        try:
            return services.invite_service().get_all_invites(), 200
        except Exception as e:
            nsp.abort(500, "An internal server error has occurred: {}".format(e))

    @nsp.doc(body=invite_fields, response={201: 'Invite successfully created.'})
    def post(self):
        """ Create a new invite """
        try:
            invite = request.json
            services.invite_service().upsert_invite(invite)
            
            services.email_service().send_user_invite(invite)
    
            return invite, 201
        except Exception as e:
            nsp.abort(500, 'An internal server error has occurred: {}'.format(e))
    
@nsp.route('/<string:invite_id>')
class Invite(Resource):
    @nsp.marshal_with(invite_fields)
    def get(self, invite_id):
        """Get an invite by id"""
        try:
            return services.invite_service().get_invite_by_id(invite_id);
        except Exception as e:
            nsp.abort(500, 'An internal server error has occurred: {}'.format(e))
            print(e)
            
    @nsp.doc(body=invite_fields, responses={204: 'Invite updates successfully.'})
    def put(self, invite_id):
        """Update an invite by id"""
        try:
            invite = request.json
            return invite, 204
        except Exception as e:
            nsp.abort(500, 'An internal server error has occurred: {}'.format(e))
    
    @nsp.doc(responses={202: 'Invite has been flagged for deletion.'})
    def delete(self, invite_id):
        """Flag an invite for deletion by it's id"""
        try:
            services.invite_service().delete_invite(invite_id);
            return 202
        except Exception as e:
            nsp.abort(500, "An internal error has occurred: {}".format(e))
    
