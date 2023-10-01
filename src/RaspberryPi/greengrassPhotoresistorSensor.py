# -*- coding: utf-8 -*-

import logging
import platform
import sys
from threading import Timer

import greengrasssdk

# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# sdk clientを作成
client = greengrasssdk.client("iot-data")

# Greengrass Coreが入っているデバイスの情報を取得
my_platform = platform.platform()

# このLambda関数がデプロイされ、ラズパイが起動すると、1秒おきにずっと動き続ける。
# "topicをAWS IoT上でサブスクライブすると、メッセージが返ってくる
def greengrassPhotoresistorSensorRun():
    bus = smbus.SMBus(1)    ##I2C通信するためのモジュールsmbusのインスタンスを作成
    adress = 0x04           #arduinoのサンプルプログラムで設定したI2Cチャンネル
    openStatus = False      #開閉状態判断

    try:

        #Arduinoへ文字『R』を送る、ordはアスキーコードを取得
        bus.write_byte(adress, ord('R'))

        #Arduinoからのメッセージを取得し表示する
        lightMsg = chr(bus.read_byte(adress))
        print(lightMsg)

        # ドア開いたとき
        if lightMsg == "O" and not openStatus:

            client.publish(
                topic="door/message", payload="ドアが開きました。"
            )
            openStatus = True
        # ドア閉じたとき
        elif lightMsg == "C" and openStatus:

            client.publish(
                topic="door/message", payload="ドアが閉まりました。"
            )
            openStatus = False

    except Exception as e:
        logger.error("Failed to publish message: " + repr(e))

    # 1秒ごとに非同期にこの関数を実行する
    Timer(1, greengrassPhotoresistorSensorRun).start()


# 上記の関数を実行する(ラズパイが起動している限り、実行される様になっている)
greengrassPhotoresistorSensorRun():


# 何かしらのイベントによって発火させるのであれば、この中に実行される関数を書く。
# 今回は無条件に関数を実行なので、外に書いてある。
def function_handler(event, context):
    return
