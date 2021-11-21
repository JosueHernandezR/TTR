from .crud_item import item
from .crud_user import user
from .crud_answer import answer
from .crud_question_option import question_option
from .crud_question_option_open import question_option_open
from .crud_question import question
from .crud_survey import survey

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
