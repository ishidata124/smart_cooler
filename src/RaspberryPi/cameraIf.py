# -*- coding: utf-8 -*-

import logging
import sys

import greengrasssdk

# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# sdk clientを作成
client = greengrasssdk.client("iot-data")

# 何かしらのイベントによって発火させるのであれば、この中に実行される関数を書く。
def function_handler(event, context):

    try:
        topic = context.client_context.custom['subject']

        client.publish(
            topic="camera/if", payload='Invoked on topic "%s"' % (topic)
        )

    except Exception as e:
        logger.error("Failed to publish message: " + repr(e))
    return
