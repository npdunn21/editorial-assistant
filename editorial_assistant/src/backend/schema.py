import enum
from uuid import UUID

from pydantic import BaseModel


class AddClientRequest(BaseModel):
    """
    Request body when adding a client to the database
    """
    name: str
    client_description: str


class AddClientResponse(BaseModel):
    """
    Returns the id of the new client that was added to the database
    """
    client_id: UUID


@enum.Enum
class PostType:
    """
    Different types of posts that GPT can create
    """
    LONG_FORM = "long_form"
    SHORT_FORM = "short_form"
    ENGAGEMENT = "engagement"
    INTERVIEW = "interview"


class PostMetrics(BaseModel):
    """
    All data associated with a post
    """
    comment_count: int = 0
    like_count: int = 0
    impression_count: int = 0


@enum.Enum
class ContentAuthor:
    """
    Different types of posts that GPT can create
    """
    CLIENT = "client"
    OTHER = "other"


class Post(BaseModel):
    """
    All data associated with a post
    """
    id: UUID
    client_id: UUID
    content: str
    metrics: PostMetrics
    post_type: PostType
    author: ContentAuthor


class GeneratePostRequest(BaseModel):
    """
    Request for using GPT to generate a post
    """
    post_type: PostType
    client_id: UUID
    post_prompt: str


class GeneratePostResponse(BaseModel):
    """
    Response with GPT generated post
    """
    post: Post


class UploadContentRequest(BaseModel):
    """
    Request for uploading a post
    """
    post_type: PostType
    client_id: UUID
    content: str
    author: ContentAuthor
    metrics: PostMetrics


class UploadContentResponse(BaseModel):
    """
    Response with GPT generated post
    """
    content_id: UUID


class AddMetricsToPostRequest(BaseModel):
    """
    Request for adding metrics to a post

    It replaces whatever is currently stored for metrics there unless the value sent is 0 and there's already a higher
    number stored
    """
    client_id: UUID
    post_id: UUID
    comment_count: int = 0
    like_count: int = 0
    impression_count: int = 0


class AddMetricsToPostResponse(BaseModel):
    """
    Returns current metrics
    """
    comment_count: int
    like_count: int
    impression_count: int


@enum.Enum
class UnitOfTime:
    """
    Units of time
    """
    DAY = "day"
    MONTH = "other"


class GetPostsForClientRequest(BaseModel):
    """
    Request for getting posts stored from the past x unit of time
    """
    client_id: UUID
    unit_of_time: UnitOfTime


class GetPostsForClientResponse(BaseModel):
    """
    Response with posts for a client over the past X unit of time
    """
    posts: list[Post]
