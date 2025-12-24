import streamlit as st
import requests

# --- 設定 ---
# 💡 ご自身のAPIキーをここに貼り付けてください
API_KEY = "8e8e1efc195bb65308a107e888a1bb6c"

# --- ✨ デザイン設定（視認性：最終解決版） ---
st.markdown("""
    <style>
    /* 全体の背景 */
    .stApp {
        background: linear-gradient(135deg, #0ea5e9 0%, #38bdf8 100%);
    }
    
    /* 入力欄の上の文字 */
    .stMarkdown p, label {
        color: white !important;
        font-weight: bold !important;
    }

    h1 {
        color: white !important;
        text-align: center;
    }

    /* 天気カード（メイン） */
    .weather-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin: 20px 0;
    }
    
    .weather-card h1, .weather-card h2, .weather-card p {
        color: #0c4a6e !important;
    }

    /* 💡 助言エリアのボックス：背景を真っ白に固定 */
    .advice-box {
        background-color: #ffffff !important;
        padding: 20px;
        border-radius: 15px;
        border-left: 8px solid #0c4a6e;
        margin-top: 10px;
    }
    
    /* 💡 ここが最重要：文字色を何があっても「真っ黒」にする設定 */
    .advice-text {
        color: #000000 !important; /* 真っ黒 */
        display: block !important;
        opacity: 1 !important;    /* 透明度なし */
        text-shadow: none !important; /* 変な影を消す */
        font-weight: bold !important;
        font-size: 1.2rem !important;
        margin: 0 !important;
    }
    
    /* ボタン */
    div.stButton > button:first-child {
        background-color: white !important;
        color: #0ea5e9 !important;
        font-weight: bold !important;
        width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("☀️ お天気コンシェルジュ")

city_input = st.text_input("都市名を入力してください", "東京")

if st.button("天気をチェック！"):
    # 日本語から英語への変換マップ
    jp_to_en = {
        "東京": "Tokyo", "大阪": "Osaka", "札幌": "Sapporo", "名古屋": "Nagoya",
        "福岡": "Fukuoka", "沖縄": "Okinawa", "那覇": "Naha", "横浜": "Yokohama",
        "ロサンゼルス": "Los Angeles", "デンバー": "Denver", "ロンドン": "London",
        "パリ": "Paris", "ニューヨーク": "New York"
    }
    search_city = jp_to_en.get(city_input, city_input)

    url = f"https://api.openweathermap.org/data/2.5/weather?q={search_city}&appid={API_KEY}&units=metric&lang=ja"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather_desc = data["weather"][0]["description"]
            temp = round(data["main"]["temp"], 1)
            
            # メインの天気カード
            st.markdown(f"""
                <div class="weather-card">
                    <h2 style='margin: 0;'>📍 {city_input}</h2>
                    <h1 style='font-size: 60px; margin: 10px 0;'>{temp} ℃</h1>
                    <p style='font-size: 20px;'>{weather_desc}</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.snow()
            
            # 助言タイトル（白）
            st.markdown("<h3 style='color: white;'>💡 コンシェルジュの助言</h3>", unsafe_allow_html=True)
            
            if temp < 10:
                advice = f"🥶 かなり寒いです！厚手のコートを着て、しっかり防寒してください。"
            elif temp < 20:
                advice = f"🧥 少し肌寒いですね。ジャケットやカーディガンを持っていきましょう。"
            else:
                advice = f"👕 暖かいですよ。軽装でお出かけを楽しんでください！"
            
            # 💡 助言を「真っ黒」で表示するボックス
            # タグの中に直接 style を書くことで、Streamlitの自動変換を上書きします
            st.markdown(f"""
                <div class="advice-box">
                    <span style="color: black !important; font-weight: bold; font-size: 1.1rem;">
                        {advice}
                    </span>
                </div>
            """, unsafe_allow_html=True)
                
        else:
            st.error("データが見つかりませんでした。")
            
    except:
        st.error("エラーが発生しました。")

st.markdown("---")
st.caption("Produced by My Weather App")
