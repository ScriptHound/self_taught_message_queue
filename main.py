from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.params import Depends

from schemas.responses import CreateTopicResponse, DeleteTopicResponse, PublishMessageResponse, ReadMessageResponse
from storage import get_topics_handler, TopicsHandler

app = FastAPI()


@app.post("/topic/create")
async def create_topic(topic_name: str, topic_handler: TopicsHandler = Depends(get_topics_handler)) -> CreateTopicResponse:
    topic = topic_handler.create_topic(topic_name)
    return CreateTopicResponse(name=topic.name)


@app.delete("/topic/delete")
async def delete_topic(topic_name: str, topic_handler: TopicsHandler = Depends(get_topics_handler)) -> DeleteTopicResponse:
    topic_handler.delete_topic(topic_name)
    return DeleteTopicResponse(name=topic_name)


@app.post("/message/publish")
async def publish_message(topic_name: str, data: dict, topic_handler: TopicsHandler = Depends(get_topics_handler)) -> PublishMessageResponse:
    topic_handler.publish_messsage(data, topic_name)
    return PublishMessageResponse()


@app.get("/message/read")
async def read_message(topic_name: str, topic_handler: TopicsHandler = Depends(get_topics_handler)) -> ReadMessageResponse:
    message = topic_handler.read_message(topic_name)
    if message is None:
        return JSONResponse(status_code=404, content={"message": "No message found"})
    return ReadMessageResponse(message=message)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
