import streamlit as st
import requests

# --- 設定 ---
# 💡 ご自身のAPIキーをここに貼り付けてください
API_KEY = "8e8e1efc195bb65308a107e888a1bb6c"

# --- ✨ デザイン設定（視認性最強・エラーなし版） ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0ea5e9 0%, #38bdf8 100%);
    }
    
    /* 入力エリアのラベルを白く太く */
    .stMarkdown p, label {
        color: white !important;
        font-weight: bold !important;
    }

    h1 {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        text-align: center;
    }

    /* 天気カード（メイン） */
    .weather-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
        text-align: center;
        margin: 20px 0;
    }
    
    .weather-card h1, .weather-card h2, .weather-card p {
        color: #0c4a6e !important;
    }

    /* 💡 助言エリア：不透明な白背景に濃い紺色の文字 */
    .advice-box {
        background-color: #ffffff !important;
        padding: 20px;
        border-radius: 15px;
        border-left: 8px solid #0c4a6e;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.1);
        margin-top: 10px;
    }
    
    .advice-text {
        color: #0c4a6e !important;
        font-size: 1.1rem !important;
        font-weight: bold !important;
        margin: 0 !important;
        line-height: 1.5 !important;
    }
    
    /* ボタン */
    div.stButton > button:first-child {
        background-color: white !important;
        color: #0ea5e9 !important;
        font-weight: bold !important;
        width: 100% !important;
        border: none !important;
        height: 3em !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("☀️ お天気コンシェルジュ")
st.write("日本の都市も、海外の都市も、日本語で入力してみてください！")

city_input = st.text_input("都市名を入力（例：東京、大阪、札幌、ロサンゼルス）", "東京")

if st.button("天気をチェック！"):
    # 内部変換用のマップ
    jp_to_en = {
        "東京": "Tokyo", "大阪": "Osaka", "札幌": "Sapporo", "名古屋": "Nagoya",
        "福岡": "Fukuoka", "沖縄": "Okinawa", "那覇": "Naha", "横浜": "Yokohama",
        "ロサンゼルス": "Los Angeles", "デンバー": "Denver", "ロンドン": "London",
        "パリ": "Paris", "ニューヨーク": "New York"
    }
    
    search_city = jp_to_en.get(city_input, city_input)

    params = {
        "q": search_city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "ja"
    }
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            weather_desc = data["weather"][0]["description"]
            temp = round(data["main"]["temp"], 1)
            formal_name = data["name"]
            
            # メインの天気カード
            st.markdown(f"""
                <div class="weather-card">
                    <h2 style='margin: 0;'>📍 {city_input}</h2>
                    <p style='color: #64748b; margin-bottom: 10px;'>({formal_name})</p>
                    <h1 style='font-size: 64px; margin: 10px 0;'>{temp} ℃</h1>
                    <p style='font-size: 20px; font-weight: bold;'>{weather_desc}</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.snow()
            
            # 💡 助言エリア（ここをクォーテーション・ミスなく修正しました）
            st.markdown("<h3 style='color: white;'>💡 コンシェルジュの助言</h3>", unsafe_allow_html=True)
            
            if temp < 10:
                advice = f"🥶 現在の{city_input}はかなり寒いです！しっかり防寒してください。"
            elif temp < 20:
                advice = f"🧥 少し肌寒いかもしれません。羽織るものがあると安心です。"
            else:
                advice = f"👕 過ごしやすい気温です！軽装でお出かけを楽しんでください。"
            
            st.markdown(f"""
                <div class="advice-box">
                    <p class="advice-text">{advice}</p>
                </div>
            """, unsafe_allow_html=True)
                
        else:
            st.error(f"「{city_input}」のデータが見つかりませんでした。")
            
    except Exception as e:
        st.error(f"エラーが発生しました。")

st.markdown("---")
st.caption("Produced by My Weather App | 全世界対応・日本語
