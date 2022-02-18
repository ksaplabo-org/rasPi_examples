# RaspberryPi×Python

## 前準備
``` bash
$ mkdir kensyu_{研修年月日}
$ cd kensyu_{研修年月日}
$ git clone https://github.com/ksaplabo-org/rasPi_examples.git
```
## 午前
---------------------------------------
## task 01 Ltika
GPIO出力  
説明のみ。

## task 02 traffic_light
GPIO出力　複数  
中身ないので各自で作る。

## task 03 motion
GPIO入力  
説明のみ。

## task 04 speaker
GPIO出力　操作  
中身ないので各自で作る。  
圧電スピーカとは。どうやって音がなっているのか説明。  

## task 05 alert
人感センサと圧電スピーカを使ってアラートシステムの作成。  
中身ないので各自で作る。

## 午後
---------------------------------------
## task 06 dht11
``` bash
$ git clone https://github.com/szazo/DHT11_Python.git
```
サンプルの起動。  

## task 07 lcd_display

5V駆動  
SDA, SCL を RaspberryPi の SDA, SCL に接続  

アドレス確認。合ってなければ合わせる。認識できなければ正しく接続されていない。
``` bash
$ i2cdetect -y 1
```
実行
``` bash
$ python3 lcd_display.py
```

## task 08 mqtt
温度センサの情報をLCDディスプレイに表示しつつ、MQTTでIoT Coreに送信する。  
airconditionのreadmeに続く。
``` bash
git clone https://github.com/ksaplabo-org/aircondition.git
```
IoT Coreでデータ取得できたら終わり。