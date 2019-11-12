from app.api.create_app import db
from ..db_model import BlacklistToken


class TokenService:

  def save_token(token):
    blacklist_token = BlacklistToken(token=token)
    try:
        # insert the token
        db.session.add(blacklist_token)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully logged out.'
        }
        return response_object, 200
    except Exception as e:
      print(e)
      response_object = {
          'status': 'fail',
          'message': e
      }
      return response_object, 200