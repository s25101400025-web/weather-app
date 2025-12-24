import streamlit as st
import requests

# --- 設定 ---
# 💡 ご自身のAPIキーをここに貼り付けてください
API_KEY = "8e8e1efc195bb65308a107e888a1bb6c"

# --- ✨ デザイン設定（視認性抜群の水色デザイン） ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0ea5e9 0%, #38bdf8 100%);
    }
    .stMarkdown p, label {
        color: white !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
    }
    h1 {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        text-align: center;
    }
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

# 都市名を日本語で入力
city_input = st.text_input("都市名を入力（例：東京、大阪、札幌、ロサンゼルス）", "東京")

if st.button("天気をチェック！"):
    # 💡 確実な成功の鍵：日本語の入力をAPIが理解できる英語に内部変換
    # 代表的な都市の変換マップ
    jp_to_en = {
        "東京": "Tokyo", "大阪": "Osaka", "札幌": "Sapporo", "名古屋": "Nagoya",
        "福岡": "Fukuoka", "沖縄": "Okinawa", "那覇": "Naha", "横浜": "Yokohama",
        "ロサンゼルス": "Los Angeles", "デンバー": "Denver", "ロンドン": "London",
        "パリ": "Paris", "ニューヨーク": "New York"
    }
    
    # 変換マップにあれば英語に、なければそのまま送信
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
            humidity = data["main"]["humidity"]
            formal_name = data["name"]
            
            st.markdown(f"""
                <div class="weather-card">
                    <h2 style='margin: 0;'>📍 {city_input}</h2>
                    <p style='color: #64748b; margin-bottom: 10px;'>({formal_name})</p>
                    <h1 style='font-size: 64px; margin: 10px 0;'>{temp} ℃</h1>
                    <p style='font-size: 20px; font-weight: bold;'>{weather_desc} / 湿度: {humidity} %</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.snow()
            
            st.subheader("💡 コンシェルジュの助言")
            if temp < 10:
                st.info(f"現在の{city_input}はかなり寒いです。厚着をしてくださいね。")
            elif temp < 20:
                st.info(f"少し肌寒いかもしれません。上着を一枚持っていきましょう。")
            else:
                st.success(f"暖かいですね！とても過ごしやすい天気です。")
                
        else:
            st.error(f"「{city_input}」のデータが見つかりませんでした。英語（例: Tokyo）で入力して試してみてください。")
            
    except Exception as e:
        st.error(f"エラーが発生しました。接続を確認してください。")

st.markdown("---")
st.caption("Produced by My Weather App | 全世界対応・日本語入力強化版")
