from .crud_user import user
from .crud_question_option import question_option
from .crud_question_option_open import question_option_open
from .crud_question import question
from .crud_survey import survey
from .crud_answer_option import answer_option
from .crud_answer_option_open import answer_option_open
from .crud_prediction import prediction_manual
from .crud_results import survey_result

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
