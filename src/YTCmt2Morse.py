import re
import threading
import keyboard
import pytchat
import simpleaudio as sa
from pydub.generators import Sine, WhiteNoise
from pydub import AudioSegment
import os

# ffmpegのパス（必要に応じて相対パス指定）
AudioSegment.converter = os.path.join(os.path.dirname(__file__), "ffmpeg", "ffmpeg.exe")

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

def to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

def is_english_symbols_only(text):
    return re.fullmatch(r"[A-Za-z0-9\s\.\,\!\?\:\;\-\'\/\(\)\&\=\+\@\$\_]+", text) is not None

def extract_video_id_from_url(url_or_id: str) -> str:
    if re.fullmatch(r"[\w-]{11}", url_or_id):
        return url_or_id
    patterns = [
        r"(?:v=|\/)([\w-]{11})(?:[&?\/]|$)",
        r"youtube\.com/live/([\w-]{11})"
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    raise ValueError("⛔ 無効なYouTube URLまたはVideo IDやで！")

def build_morse_audio(morse_code: str) -> AudioSegment:
    dot_tone = Sine(600).to_audio_segment(duration=80).apply_gain(-30)
    dash_tone = Sine(600).to_audio_segment(duration=200).apply_gain(-30)
    dot_noise = WhiteNoise().to_audio_segment(duration=80).apply_gain(-55)
    dash_noise = WhiteNoise().to_audio_segment(duration=200).apply_gain(-55)
    gap = AudioSegment.silent(duration=40)
    char_gap = AudioSegment.silent(duration=80)
    word_gap = AudioSegment.silent(duration=260)

    result = AudioSegment.silent(duration=0)

    for symbol in morse_code:
        if symbol == '.':
            result += dot_tone.overlay(dot_noise) + gap
        elif symbol == '-':
            result += dash_tone.overlay(dash_noise) + gap
        elif symbol == ' ':
            result += char_gap
        elif symbol == '/':
            result += word_gap

    return result

def play_morse(morse_code: str):
    audio = build_morse_audio(morse_code)
    play_obj = sa.play_buffer(
        audio.raw_data,
        num_channels=1,
        bytes_per_sample=2,
        sample_rate=44100
    )
    play_obj.wait_done()

running = True
def watch_for_exit_key():
    global running
    keyboard.wait('q')
    running = False
    print("🛑 Qキーが押されたため、終了します。")

def monitor_chat(video_id):
    global running
    chat = pytchat.create(video_id=video_id)
    print("💬 コメント監視スタート！（Qキーで停止）")
    while chat.is_alive() and running:
        for c in chat.get().sync_items():
            try:
                msg = c.message
                if msg.lower().startswith("/morse "):
                    text = msg[7:]  # 「/morse 」の後ろだけ取り出し
                    if is_english_symbols_only(text):
                        morse = to_morse(text)
                        print(f"[{c.author.name}] {text} → {morse}")
                        play_morse(morse)
                    else:
                        print(f"→ {c.author.name} の /morse コメントに非対応文字があるためスキップ！")
                else:
                    print(f"→ {c.author.name} のコメントはスキップ（/morse 指定なし）")
            except Exception as e:
                print(f"⚠️ エラー：{e}")
        if not running:
            break

if __name__ == "__main__":
    user_input = input("Enter YouTube Live URL or Video ID: ")
    video_id = extract_video_id_from_url(user_input)
    threading.Thread(target=watch_for_exit_key, daemon=True).start()
    monitor_chat(video_id)
