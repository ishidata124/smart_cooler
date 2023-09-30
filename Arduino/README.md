# Arduinoの使い方について
Arduinoの使い方について記載します。

## Arduinoの初期設定
Arduinoの初期設定方法について説明します。

### 1.構築イメージ
![構築イメージ](../image/arduino/Initialset1.png "構築イメージ")
PCにIDEをインストールし、 Arduinoへ処理の書き込みができる状態にします。

### 2.Arduino組み立て
![Arduino組み立て](../image/arduino/Initialset2.png "Arduino組み立て")
ArduinoにUSBの部品をさすだけです。

### 3.IDEインストール手順
[公式ページ](https://www.arduino.cc/en/Guide/Windows)へアクセスします。

![インストール1](../image/arduino/Initialset3.png "インストール1")
対象のPCにあったリンクを押します。  
画像はWindows用のものを選択しています。

![インストール2](../image/arduino/Initialset4.png "インストール2")
赤四角で囲んであるところをクリックするとダウンロードが始まります。

![インストール3](../image/arduino/Initialset5.png "インストール3")
exeファイルを実行するとインストールが始まります。

![インストール4](../image/arduino/Initialset6.png "インストール4")
設定はデフォルトで問題ないので進んでいきます。  
必要時カスタムしてください。

![インストール5](../image/arduino/Initialset7.png "インストール5")

![インストール6](../image/arduino/Initialset8.png "インストール6")

![インストール7](../image/arduino/Initialset9.png "インストール7")

![アルディーノアイコン](../image/arduino/Initialset10.png "アルディーノアイコン")

インストール後、ディスクトップにアイコンが出現します。(設定を変えなかった場合。)  
こちらをクリックするとエディタが起動します。

![エディタ1](../image/arduino/Initialset11.png "エディタ1")

無事起動できたらインストール作業は完了です。  
先ほど組み立てたArduinoをPCに接続します。

![アルディーノランプ](../image/arduino/Initialset12.jpg "アルディーノランプ")
接続するとランプが光ります。

### 4.IDEの設定
![設定変更](../image/arduino/Initialset13.png "設定変更")
接続の設定をします。  
ツール→シリアルポート→接続先の設定を押せばOKです。  

### 5. Arduinoへデータ書き込み
![サンプルコード](../image/arduino/Initialset14.png "サンプルコード")
サンプルコードを表示させます。  
スケッチ例→01.Basics→Blinkを選択します。

![サンプルコード2](../image/arduino/Initialset15.png "サンプルコード2")
サンプルコードが表示されます。
```
void setUp() {
  pinMode(LED_BUILIN,OUTPUT); // 組み込みLEDに出力
}

void loop() {
  digitalWrite(LED_BUILIN,HIGH); // 組み込みLEDに出力ON
  delay(1000); // 1秒待つ
  digitalWrite(LED_BUILIN,LOW); // 組み込みLEDに出力OFF
  delay(1000); // 1秒待つ
}
```

![書き込み方法](../image/arduino/Initialset16.png "書き込み方法")
スケッチ→マイコンボードに書き込む で書き込み作業は終わりです。  
Delayに指定されている1秒ごとにLEDランプが点滅していたらチェックOKです。

## Arduinoとブレッドボード
Arduinoとブレッドボードの連携方法の説明をします。
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

## Arduinoと光センサー
Arduinoと光センサーの接続方法、使用方法を説明します。

### 1.必要物品
※基本的なものは除きます。
![光センサー](../image/arduino/light1.jpg "光センサー")
光センサーモジュール。今回使用するものは端子が4つあります。

![光センサーの配線](../image/arduino/light2.jpg "光センサーの配線")
Arduinoと光センサーを繋ぐための配線です。  
3本あればOKです。

### 2.組み立て
![光センサー側配線](../image/arduino/light3.png "光センサー側配線")
今回AO、DO、VCCの3つの端子を使用します。

![アルディーノ側配線](../image/arduino/light4.png "アルディーノ側配線")
今回使用するのはinput側です。  
配線はAO→5V、DO→GND、VCC→A0に繋げばOKです。

### 3.コーディング
![光量判定コード](../image/arduino/light5.png "光量判定コード")
光量を測定するコードを記述します。

```
int val=0; // 入力される値を格納するための変数
void setUp() {
  Serial.begin(9800); // モニターに出力するための設定
}

void loop() {
  // ANALOG INの0番ピンからデータを取得 input時はsetupにピンの指定はいらない。
  val=analogRead(0);
  Serial.println(val); // 入力された値をモニターに出力(アナログピンの入力値は0～1023)
  delay(100); // 0.1秒待つ
}
```

### 4.結果確認
![確認用操作](../image/arduino/light6.png "確認用操作")
入力情報が取得できているか確認します。  
ツール→シリアルモニタを選択します。

![確認出力](../image/arduino/light7.png "確認出力")
光センサーを明るいところと暗いところに交互に置いてみましょう。  
明るさによって数値が変動しているとおもいます。
