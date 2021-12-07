# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.user import User  # noqa
from app.models.question import Question # noqa
from app.models.question_option import Question_option # noqa
from app.models.question_option_open import Question_option_open # noqa
from app.models.survey import Survey # noqa
from app.models.answer_option import Answer_Option # noqa
from app.models.answer_option_open import Answer_Option_Open # noqa
from app.models.results import Survey_Results # noqa
from app.models.predictions import Prediction_Manual # noqa
from app.models.survey_aceptacion import Survey_Aceptacion # noqa