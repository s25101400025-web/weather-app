import streamlit as st
import requests

# --- 設定 ---
# 💡 ご自身のAPIキーをここに貼り付けてください
API_KEY = "8e8e1efc195bb65308a107e888a1bb6c"

# --- ✨ デザイン設定 ---
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
    }

    .weather-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.1);
    }
    
    .weather-card h1, .weather-card h2, .weather-card p {
        color: #0c4a6e !important;
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
                    <h2 style='margin: 0; color: #0c4a6e;'>📍 {city_input}</h2>
                    <h1 style='font-size: 60px; margin: 10px 0; color: #0c4a6e;'>{temp} ℃</h1>
                    <p style='font-size: 20px; color: #0c4a6e;'>{weather_desc}</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.snow()
            
            st.markdown("<h3 style='color: white;'>💡 コンシェルジュの助言</h3>", unsafe_allow_html=True)
            
            if temp < 10:
                advice = f"かなり寒いです！厚手のコートを着て、しっかり防寒してください。"
                icon = "🥶"
            elif temp < 20:
                advice = f"少し肌寒いですね。ジャケットやカーディガンを持っていきましょう。"
                icon = "🧥"
            else:
                advice = f"暖かいですよ。軽装でお出かけを楽しんでください！"
                icon = "👕"
            
            # 💡 最終解決策：文字を「カードの一部」として表示し、
            # colorタグを何重にも重ねて、Streamlitの自動色反転を完全にブロックします。
            st.markdown(f"""
                <div style="background-color: white; padding: 20px; border-radius: 15px; border-left: 10px solid #0c4a6e; box-shadow: 0px 5px 15px rgba(0,0,0,0.2);">
                    <p style="margin: 0; padding: 0; line-height: 1.6;">
                        <span style="color: #000000 !important; font-size: 1.2rem; font-weight: 900;">
                            {icon} {advice}
                        </span>
                    </p>
                </div>
            """, unsafe_allow_html=True)
                
        else:
            st.error("都市が見つかりませんでした。")
            
    except:
        st.error("エラーが発生しました。")

st.markdown("---")
st.caption("Produced by My Weather App")
