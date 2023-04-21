from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import correlation_paths

logger = Logger(service="APP")

app = APIGatewayRestResolver()

@app.get("/hello/<name>")
def hello_name(name):
    logger.info(f"Request from {name}")
    return {"message": f"hello {name}!"}

@app.get("/hello")
def hello():
    logger.info(f"Request from unknown")
    return {"message": "hello unknown!"}

@app.get("/goodbye")
def goodbye():
    logger.info(f"Request from unknown")
    return {"message": "goodbye unknown!"}


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST, log_event=True)
def lambda_handler(event, context):
    return app.resolve(event, context)
