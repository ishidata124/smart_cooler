# Arduinoの使い方について
Arduinoの使い方について記載します。
## Arduinoとブレッドボード
### 1.この作業の使用物品
![ブレッドボード](../image/arduino/breadboard1.jpg "ブレッドボード")
ブレッドボード

![配線(2本)](../image/arduino/breadboard2.jpg "配線(2本)")
配線(2本)

![LED（1個）](../image/arduino/breadboard3.jpg "LED（1個）")
LED（1個）

![抵抗（1kΩ1本）](../image/arduino/breadboard4.jpg "抵抗（1kΩ1本）")
抵抗（1kΩ1本）

### 2.出力について
![出力説明用](../image/arduino/breadboard5.png "出力説明用")
pin番号の部分から電気出力し、GNDへ返っていきます。

### 3.部品知識
![部品知識説明用ブレッドボード](../image/arduino/breadboard6.jpg "部品知識説明用ブレッドボード")
同じレーンの連結部分(縦5列の部分等)は内部でつながっています。

![部品知識説明用紙](../image/arduino/breadboard7.jpg "部品知識説明用紙")
抵抗は今回1KΩを使います。使わないとLEDがダメージかなり食らいます。(破損します。)

<img src="../image/arduino/breadboard8.jpg" width="40">

LEDは長い方が＋で短い方が－。－がGND側になるように使用します。

### 4.コーディング
![エディタ](../image/arduino/breadboard9.png "エディタ")
エディタを起動し、下記コードエディタにを記載します。
```
void setUp() {
  pinMode(2,OUTPUT); // デジタルpin2に出力
}

void loop() {
  digitalWrite(2,HIGH); // デジタルpin2に出力ON
  delay(1000); // 1秒待つ
  digitalWrite(2,LOW); // デジタルpin2に出力OFF
  delay(1000); // 1秒待つ
}
```
左上にボタンがあります。  
そこの左のボタンがコンパイル、右のボタンがアップロード（書き込み）です。アップロードは組み立て作業後にやるので今は実行しません。  
下側にあるのがコンソールです。

### 5.組み立て
![組み立てアルディーノ](../image/arduino/breadboard10.jpg "組み立てアルディーノ")
コーディング内容通り、2pinより出力し、GNDで受け取るように接続します。

![組み立てブレッドボード](../image/arduino/breadboard11.jpg "組み立てブレッドボード")
右側端子から出力→抵抗で威力を弱める→LEDで電気を受け取る→左側の端子で電気を受け取る の流れで回線を組みます。

### 6.結果確認
![ライト点灯](../image/arduino/breadboard12.jpg "ライト点灯")
コーディング内容通り1秒ごとに点灯動作を繰り返していれば成功です。

