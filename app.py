import streamlit as st
import requests

# --- 設定 ---
# 💡 ここにご自身のAPIキーを貼り付けてください
API_KEY = "8e8e1efc195bb65308a107e888a1bb6c"

# 日本語の都市名と、APIに送る英語名の対応表（辞書）
CITY_MAP = {
    "東京": "Tokyo",
    "大阪": "Osaka",
    "札幌": "Sapporo",
    "名古屋": "Nagoya",
    "福岡": "Fukuoka",
    "沖縄": "Okinawa",
    "ロンドン": "London",
    "ニューヨーク": "New York",
    "パリ": "Paris"
}

# --- ✨ 冬仕様のデザイン設定 ---
st.markdown("""
    <style>
    /* 1. 背景：冬の朝のような澄んだ青と白のグラデーション */
    .stApp {
        background: linear-gradient(135deg, #e0f2fe 0%, #ffffff 70%, #f1f5f9 100%);
    }
    
    /* 2. 文字の色：冬らしい深い紺色 */
    h1, h2, h3, p {
        color: #0f172a !important;
    }

    /* 3. 名言を表示するカード：氷のような透明感のある白 */
    .weather-card {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #e2e8f0;
        margin: 25px 0;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.05);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("❄️ 冬のお天気コンシェルジュ")
st.write("今の都市の天気を調べて、お出かけのアドバイスをします。")

# --- A案：セレクトボックスで都市を選択 ---
selected_city_jp = st.selectbox(
    "調べたい都市を選んでください",
    list(CITY_MAP.keys())
)

# 選択された日本語名に対応する英語名を取得
city_name_en = CITY_MAP[selected_city_jp]

if st.button("天気をチェック！"):
    # APIにリクエストを送る
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name_en}&appid={API_KEY}&units=metric&lang=ja"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            
            # 結果表示
            st.markdown(f"""
                <div class="weather-card">
                    <h2 style='color: #1e3a8a;'>📍 {selected_city_jp} ({city_name_en})</h2>
                    <h1 style='font-size: 60px; margin: 10px 0;'>{temp} ℃</h1>
                    <p style='font-size: 20px;'>天気: {weather} / 湿度: {humidity} %</p>
                </div>
            """, unsafe_allow_html=True)
            
            # --- B案：冬の演出（雪を降らせる） ---
            st.snow() 
            
            # アドバイス
            st.subheader("💡 コンシェルジュからの助言")
            if temp < 5:
                st.error("氷点下に近いです！凍結に注意して、最高レベルの防寒を。")
            elif temp < 15:
                st.info("冬の寒さです。コートやマフラーが必須ですね。")
            else:
                st.success("この時期にしては暖かいですが、油断は禁物です。")
                
            if "雨" in weather or "雪" in weather:
                st.warning("足元が滑りやすくなっているかもしれません。ご注意ください。")
                
        else:
            st.error("データの取得に失敗しました。")
            
    except Exception as e:
        st.error(f"接続エラー: {e}")

st.markdown("---")
st.caption("Data provided by OpenWeatherMap API | Winter Edition")
