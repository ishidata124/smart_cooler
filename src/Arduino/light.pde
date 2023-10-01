#include <Wire.h>

int SLAVE_ADDRESS = 0x04;   //I2Cのアドレス『0x04』
int lightVal = 0; //入力される値を格納する為の変数

/*setupは起動後ときに最小に呼び出される関数でここで初期化の処理を行います*/
void setup() {
   //シリアル通信の初期化しシリアルモニタへ文字列を出力できるようにする　9600はボーレート(通信速度)
   Serial.begin(9600);

  //I2C接続を開始する
  Wire.begin(SLAVE_ADDRESS);

  //I2Cで受信したときに呼び出す関数を登録する
  Wire.onReceive(ReceiveMassage);

  //I2Cでリクエスト受信したときに呼び出す関数を登録する
  Wire.onRequest(RequestMassage);
}

/*setupの後、終了するまで繰り返し呼び出される関数です*/
void loop() {
  lightVal = analogRead(0); //入力された値を設定(アナログピンの入力値は0～1023)
  Serial.println(lightVal); //モニターに出力(アナログピンの入力値は0～1023)
  delay(500);
}

/*setupの後、終了するまで繰り返し呼び出される関数です*/
void ReceiveMassage(int n){
  char cmd = Wire.read();     //文字を読む
  Serial.println(cmd);       //シリアルポートにcmdを出力し表示する
}

//リクエスト要求を受けたときに光センサーでの取得値を送信する。
void RequestMassage(){
  //ドアの開閉判断
   if ( lightVal <= 900 ) {
      Wire.write("O"); //送信(ドアが開いた状態)
  } else {
      Wire.write("C"); //送信(ドアが閉じた状態)
  }
}