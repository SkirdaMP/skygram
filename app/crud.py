import json
from typing import (
    List, 
    Union
)

from models import Post


def get_all_posts() -> Union[List[Post], None]:
    pass

def get_post_by_id(post_id: int) -> Union[Post, None]:
    pass
