import logging as log
import sys

import asyncio
from grpc.experimental import aio

import recsys_pb2
import recsys_pb2_grpc


async def send_request():
    log.basicConfig(level=log.DEBUG, stream=sys.stdout)

    log.info("initiating request")
    channel = aio.insecure_channel("server:50051")
    log.info("obtained channel")
    log.info("waiting for channel to be ready")
    await channel.channel_ready()
    log.info("creating stub")
    stub = recsys_pb2_grpc.RecommenderStub(channel)

    log.info("awaiting recommendation")
    response = await stub.recommend(
        recsys_pb2.RecommenderRequest(exampleids=[1, 2, 3], context="some-user",)
    )
    log.info(dir(response.outputs))
    log.info(f"received: {list(response.outputs)}")
    for x in response.outputs:
        log.info(x)
    return response


def main():
    asyncio.run(send_request())


if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG, stream=sys.stdout)
    main()
