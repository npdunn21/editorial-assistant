import uuid

from backend.postgres import get_async_engine, get_client_table
from backend.schema import AddClientRequest, AddClientResponse, GeneratePostRequest, GeneratePostResponse, \
    UploadContentRequest, UploadContentResponse, AddMetricsToPostResponse, AddMetricsToPostRequest, \
    GetPostsForClientResponse, GetPostsForClientRequest
from backend.service import app
from sqlalchemy import insert


@app.post("client/add", AddClientResponse)
async def add_client(request: AddClientRequest):
    engine = get_async_engine()
    async with engine.begin() as conn:
        client_table = get_client_table()
        client_id = uuid.uuid4()
        insert_statement = (
            insert(client_table).
            values(id=uuid.uuid4(), name=request.name, description=request.client_description)
        )
        conn.execute(insert_statement)
    return AddClientResponse(client_id=client_id)


@app.post("post/generate", GeneratePostResponse)
async def generate_post(request: GeneratePostRequest):
    # TODO: fill this in
    return GeneratePostResponse()


@app.post("content/add", UploadContentResponse)
async def upload_content(request: UploadContentRequest):
    # TODO: fill this in
    return UploadContentResponse()


@app.post("post/metrics/add", AddMetricsToPostResponse)
async def add_metrics_to_post(request: AddMetricsToPostRequest):
    # TODO: fill this in
    return AddMetricsToPostResponse()


@app.post("post/get", GetPostsForClientResponse)
async def add_metrics_to_post(request: GetPostsForClientRequest):
    # TODO: fill this in
    return GetPostsForClientResponse()

