from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, utils, survey, question, question_option, question_option_open, answer_option, answer_option_open, predictions, results

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(survey.router, prefix="/surveys", tags=["surveys"])
api_router.include_router(question.router, prefix="/questions", tags=["questions"])
api_router.include_router(question_option.router, prefix="/question_option", tags=["question option"])
# api_router.include_router(question_option_open.router, prefix="/question_option_open", tags=["question option open"])
api_router.include_router(answer_option.router, prefix="/answer_option", tags=["answer option"])
# api_router.include_router(answer_option_open.router, prefix="/answer_option_open", tags=["answer option open"])
api_router.include_router(results.router, prefix="/results", tags=["survey results"])
api_router.include_router(predictions.router, prefix="/predictions", tags=["predictions"])