import streamlit as st
import requests

# --- 設定 ---
API_KEY = "8e8e1efc195bb65308a107e888a1bb6c"

# --- ✨ 強制ライトモード・デザイン設定 ---
st.markdown("""
    <style>
    /* 全体の背景 */
    .stApp {
        background: linear-gradient(135deg, #0ea5e9 0%, #38bdf8 100%);
    }
    
    /* 入力欄のラベル（白） */
    .stMarkdown p, label {
        color: white !important;
        font-weight: bold !important;
    }

    /* 💡 魔法の命令：このカードの中だけは「絶対にライトモード」として扱う */
    .force-light-card {
        background-color: #ffffff !important;
        color: #111111 !important; /* 真っ黒に近い紺 */
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.2);
        
        /* ブラウザの自動反転を禁止する命令 */
        color-scheme: light !important; 
    }

    /* カード内の全ての文字を強制的に黒くする */
    .force-light-card h1, 
    .force-light-card h2, 
    .force-light-card h3, 
    .force-light-card p,
    .force-light-card span {
        color: #111111 !important;
        -webkit-text-fill-color: #111111 !important; /* iPhoneなどの対策 */
    }

    /* ボタン */
    div.stButton > button:first-child {
        background-color: white !important;
        color: #0ea5e9 !important;
        font-weight: bold !important;
        width: 100% !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("☀️ お天気コンシェルジュ")

city_input = st.text_input("都市名を入力してください", "東京")

if st.button("天気をチェック！"):
    jp_to_en = {
        "東京": "Tokyo", "大阪": "Osaka", "札幌": "Sapporo", "名古屋": "Nagoya",
        "福岡": "Fukuoka", "沖縄": "Okinawa", "那覇": "Naha", "横浜": "Yokohama",
        "ロサンゼルス": "Los Angeles", "ニューヨーク": "New York"
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
                <div class="force-light-card">
                    <h2 style="margin:0;">📍 {city_input}</h2>
                    <h1 style="font-size: 70px; margin: 15px 0;">{temp} ℃</h1>
                    <p style="font-size: 22px;">{weather_desc}</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.snow()
            
            # 助言エリア
            st.markdown("<h3 style='color: white; text-align: center;'>💡 コンシェルジュの助言</h3>", unsafe_allow_html=True)
            
            if temp < 10:
                advice = "かなり寒いです！厚手のコートを着て、しっかり防寒してください。"
                icon = "🥶"
            elif temp < 20:
                advice = "少し肌寒いですね。ジャケットなど羽織るものを持っていきましょう。"
                icon = "🧥"
            else:
                advice = "過ごしやすい気温です。お出かけを楽しんでください！"
                icon = "👕"
            
            # 2️⃣ 助言カード（ここも強制ライトモード）
            st.markdown(f"""
                <div class="force-light-card" style="padding: 20px; border-left: 10px solid #0c4a6e; text-align: left;">
                    <p style="font-size: 1.2rem; font-weight: bold; margin: 0;">
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
