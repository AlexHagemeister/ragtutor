from typing import Optional

from pydantic import BaseModel


class QandA(BaseModel):
    """Question and Answer pair"""

    user_text: str
    bot_text: str


class UserQuery(BaseModel):
    """User query"""

    user_query: str
    context: Optional[list[QandA]] = None
