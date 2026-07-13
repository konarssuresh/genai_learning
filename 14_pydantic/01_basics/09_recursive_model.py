from typing import List,Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

# required after self referencing models
Comment.model_rebuild()


comment = Comment(
    id=1,
    content='First',
    replies=[
        Comment(id=2,content='Second'),
        Comment(id=3,content='Third'),
        Comment(id=4,content='Fourth'),
    ]
)