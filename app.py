import streamlit as st
import requests

# --- 設定 ---
# 💡 ご自身のAPIキーをここに貼り付けてください
API_KEY = "8e8e1efc195bb65308a107e888a1bb6c"

# --- ✨ デザイン設定（実績のあるスタイルのみを使用） ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0ea5e9 0%, #38bdf8 100%);
    }
    
    .stMarkdown p, label {
        color: white !important;
        font-weight: bold !important;
    }

    h1 {
        color: white !important;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }

    /* 🏆 実績あり：上の気温表示と同じ、確実に文字が見えるスタイル */
    .result-card {
        background-color: white !important;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        margin: 15px 0;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.1);
    }
    
    /* 🏆 実績あり：この色指定なら必ず見えます */
    .dark-text {
        color: #0c4a6e !important;
        font-weight: bold !important;
        margin: 0 !important;
    }

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
    # 日本語変換マップ
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
            
            # 1️⃣ メインの気温カード
            st.markdown(f"""
                <div class="result-card">
                    <h2 class="dark-text">📍 {city_input}</h2>
                    <h1 style='font-size: 60px; margin: 10px 0; color: #0c4a6e;'>{temp} ℃</h1>
                    <p class="dark-text" style="font-size: 20px;">{weather_desc}</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.snow()
            
            # 助言タイトル
            st.markdown("<h3 style='color: white; text-align: center;'>💡 コンシェルジュの助言</h3>", unsafe_allow_html=True)
            
            if temp < 10:
                advice = "かなり寒いです！厚手のコートを着て、しっかり防寒してください。"
                icon = "🥶"
            elif temp < 20:
                advice = "少し肌寒いですね。ジャケットなど羽織るものを持っていきましょう。"
                icon = "🧥"
            else:
                advice = "暖かいですよ。軽装でお出かけを楽しんでください！"
                icon = "👕"
            
            # 2️⃣ 助言カード（上のカードと同じ仕組みをそのまま使います）
            st.markdown(f"""
                <div class="result-card">
                    <p class="dark-text" style="font-size: 1.2rem;">
                        {icon} {advice}
                    </p>
                </div>
            """, unsafe_allow_html=True)
                
        else:
            st.error("都市が見つかりませんでした。")
            
    except:
        st.error("通信エラーが発生しました。")

st.markdown("---")
st.caption("Produced by My Weather App")
