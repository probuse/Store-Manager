from flask import Blueprint

apcn_v1 = Blueprint('apcn', __name__, url_prefix='/api/v1')
apsn_v1 = Blueprint('apsn_v1', __name__, url_prefix='/api/v1')
auth_v1 = Blueprint('auth_v1', __name__, url_prefix='/api/v1')


from .sales import *
from .registration import *
from  .products import *