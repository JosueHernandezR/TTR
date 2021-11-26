# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.user import User  # noqa
from app.models.question import Question # noqa
from app.models.question_option import Question_option # noqa
from app.models.question_option_open import Question_option_open # noqa
from app.models.survey import Survey # noqa