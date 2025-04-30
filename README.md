# 📡 YouTube Live Chat → Morse Signal Bot

YouTubeライブ配信のチャット欄に送られた `/morse` コマンド付きコメントを、  
**リアルタイムにモールス信号として音声再生する Python スクリプト**です。

600Hzのトーンとホワイトノイズを合成した、  
レトロ通信感あふれるモールス体験ができます！

---

## 🧩 Features / 特徴

- ✅ `/morse` コマンドで英語コメントをモールス変換
- ✅ リアルタイムで音を再生（YouTube Live対応）
- ✅ 600Hz固定トーン + ノイズ合成で雰囲気抜群
- ✅ コメントに日本語や記号が混ざっている場合はスキップ
- ✅ `Q` キーで安全にスクリプト停止（Ctrl+C不要）

---

## 📸 Demo

> YouTubeのライブチャット欄にこうコメントすると…

```
/morse hello world!
```

> 🎧 こんな感じのモールス信号がリアルタイム再生されます：

```
.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.-- 🔊
```

---

## 🔧 Requirements / 必要な環境

- Python 3.8 以降（推奨：Python 3.12）
- ffmpeg（音声処理に必要）
- インストール済パッケージ：

```bash
pip install pytchat simpleaudio pydub keyboard
```

---

## 📂 フォルダ構成（例）

```
YTComments2Morse/
├── yt_morse_live.py         ← メインスクリプト
├── ffmpeg/
│   └── ffmpeg.exe           ← Windows用ffmpeg実行ファイル
└── README.md                ← このドキュメント
```

---

## 🚀 Usage / 使い方

```bash
python yt_morse_live.py
```

1. 実行するとライブ配信のURLまたはIDの入力を求められます。
   ```
   🎥 配信のURLかVideo IDを入力してな：
   https://www.youtube.com/live/abcdefg1234
   ```

2. その配信のチャット欄に `/morse Hello World!` のようなコメントを送ると、
   モールス信号としてリアルタイムに音声再生されます。

3. `Q`キーを押すとスクリプトは安全に終了します。

---

## 🛡️ コメント仕様

| コメント内容         | 動作         |
|----------------------|--------------|
| `/morse Hello`       | ✅ 再生する   |
| `Hello`（/morseなし）| ❌ 無視する   |
| `/morse こんにちは` | ❌ 無視する   |
| `/morse Hello😊`     | ❌ 無視する   |

---

## 🎚️ モールス音仕様

| 項目         | 値        |
|--------------|-----------|
| 周波数       | 600Hz     |
| ドット長     | 80ms      |
| ダッシュ長   | 200ms     |
| シンボル間   | 60ms 無音 |
| 文字間       | 150ms 無音|
| 単語間       | 400ms 無音|
| ノイズ音量   | -35 dB    |
| トーン音量   | -10 dB    |

---

## 📥 備考

- ffmpegが見つからない場合、次のようにパスをスクリプト内で指定してください：

```python
AudioSegment.converter = "./ffmpeg/ffmpeg.exe"
```

- macOSやLinuxでは `/usr/local/bin/ffmpeg` などに置くとパスが通ります。

---

## 📜 License

MIT License（予定）

---

## 👤 Author

[Ruprous](https://github.com/Ruprous)
