# speech and NLP

## 環境構築
+ Ubuntu
```shell
sh setup.sh
```

* build
```
docker-compose build
```
* 実行
```
docker-compose up
```

****

## 環境構築 (Docker使わずに)

* Ubuntu 18.04

```sh
$ sudo apt install cmake ffmpeg mecab libportaudio2 -y
```


* Arch


```
$ yay -S mecab
$ yay -S mecab-ipadic

or

$ git clone https://aur.archlinux.org/mecab.git
$ makepkg -sri
$ git clone https://github.com/neologd/mecab-ipadic-neologd.git
$ ./bin/install-mecab-ipadic-neologd
```

* ソースからコンパイルしてインストール
```
$ tar zxfv mecab-X.X.tar.gz
$ cd mecab-X.X
$ ./configure 
$ make
$ make check
$ su
$ make install

$ tar zxfv mecab-ipadic-2.7.0-XXXX.tar.gz
$ mecab-ipadic-2.7.0-XXXX
$ ./configure
$ make
$ su
$ make install
```

* pip
```sh
$ pip3 install --upgrade pip
$ pip3 install -r requirements.txt
```

## 実行
```sh
python main.py
```

# 辞書が見つからないとき
* エラー内容
```
------------------- ERROR DETAILS ------------------------
arguments: 
[ifs] no such file or directory: /home/haruki-goto/.local/lib/python3.10/site-packages/unidic/dicdir/mecabrc
----------------------------------------------------------
```

`src/tools/speech_to_text/MecabAnalyzer.py`を編集してください。

```python
import MeCab

def mecabAnalyzer(string):
    m = MeCab.Tagger(<ここを編集>)
    return m.parse(string).replace("EOS", "").split()
```

## リンク
* [ArchLinuxにMecabをインストール](https://www.komee.org/entry/2018/02/28/120128)
* [MeCab](https://taku910.github.io/mecab/)
* [VOSK](https://alphacephei.com/vosk/)
* [SoundDevice](https://pypi.org/project/sounddevice/)
