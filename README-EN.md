# 📡 YouTube Live Chat → Morse Signal Bot

This is a Python script that monitors YouTube Live chat messages in real-time.  
If a message starts with `/morse`, the script converts the message into Morse code and plays it back as audio.

It uses a 600Hz tone combined with low-level white noise for a nostalgic, analog-like Morse transmission feel.

---

## 🧩 Features

- ✅ Converts messages starting with `/morse` into Morse code audio
- ✅ Real-time playback synced with YouTube Live chat
- ✅ Clear tone + white noise overlay for realistic effect
- ✅ Skips non-English (e.g., Japanese) or emoji-filled messages
- ✅ Exit safely by pressing the `Q` key (no need for Ctrl+C)

---

## 📸 Demo

> Example comment in YouTube Live chat:

```
/morse hello world!
```

> 🎧 Will be played as:

```
.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.-- 🔊
```

---

## 🔧 Requirements

- Python 3.8 or later (Recommended: Python 3.12)
- ffmpeg (required for audio processing)

### 📦 Dependencies

- `pytchat`
- `simpleaudio`
- `pydub`
- `keyboard`

### 🛠 Install with pip

```bash
pip install pytchat simpleaudio pydub keyboard
```

---

## 📂 Project Structure

```
YTComments2Morse/
├── src/
│   ├── YTCmt2Morse.py         ← Main script
│   └── ffmpeg.exe             ← Included ffmpeg binary (Windows)
├── LICENSE
└── README_en.md
```

---

## 🚀 Usage

```bash
python src/YTCmt2Morse.py
```

1. You will be prompted to enter a live stream URL or video ID:
   ```
   Enter YouTube Live URL or Video ID:
   https://www.youtube.com/live/abcdefg1234
   ```

2. Then post a comment in the live chat like `/morse Hello World!`  
   The message will be converted into Morse code and played as sound.

3. Press `Q` to safely stop the script at any time.

---

## 🛡️ Chat Filtering

| Message Example           | Action        |
|---------------------------|---------------|
| `/morse Hello`            | ✅ Played     |
| `Hello` (without `/morse`) | ❌ Ignored    |
| `/morse こんにちは`       | ❌ Ignored    |
| `/morse Hello😊`          | ❌ Ignored    |

---

## 🎚️ Morse Tone Settings

| Parameter      | Value        |
|----------------|--------------|
| Tone Frequency | 600 Hz       |
| Dot Duration   | 80 ms        |
| Dash Duration  | 200 ms       |
| Symbol Gap     | 40 ms (silence) |
| Letter Gap     | 80 ms (silence) |
| Word Gap       | 260 ms (silence) |
| Noise Volume   | -55 dB       |
| Tone Volume    | -30 dB       |

---

## 📥 About ffmpeg

This project includes a bundled `ffmpeg.exe`, built under the LGPL v2.1+ license.  
This binary is redistributable and does **not** include GPL or nonfree components.

Source and license details:  
https://ffmpeg.org

---

## 📜 License

- Source code: MIT License  
- Included ffmpeg.exe: LGPL v2.1+ (redistributable)

FFmpeg licensing details:  
https://ffmpeg.org/legal.html

---

## 👤 Author

[Ruprous](https://github.com/Ruprous)
