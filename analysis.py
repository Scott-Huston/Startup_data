from crunchbase import CrunchBase
from config import USER_KEY

cb_api = CrunchBase(USER_KEY)
facebook = cb_api.get_organizations(name='facebook')