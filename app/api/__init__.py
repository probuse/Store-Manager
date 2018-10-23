from flask import Blueprint

apcn_v1 = Blueprint('apcn', __name__, url_prefix='/api/v1')
auth_v1 = Blueprint('auth_v1', __name__, url_prefix='/api/v1')

from .products import *
from .registration import *
