from pydantic import BaseModel, field_validator, StringConstraints
from typing_extensions import Annotated, List
import pprint as pp

class Question(BaseModel):
    question_text: Annotated[str, StringConstraints(max_length=100)]
    answers: List[str] = []
    true_answer: int = 0
    explanation: Annotated[str, StringConstraints(max_length=200)] = ""


    @field_validator("question_text", mode="before")
    def validate_question_text(cls, value):
        value = value.title()
        if not value.endswith('?'):
            return f"{value} ?"

q1 = Question(question_text="what is the most subscribed YouTube channel")

pp.pprint(q1.schema())