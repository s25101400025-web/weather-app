import streamlit as st
import requests

# --- 設定 ---
# 💡 ここにご自身のAPIキーを貼り付けてください
API_KEY = "8e8e1efc195bb65308a107e888a1bb6c"

# デザイン設定（目に優しいパステルブルー）
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f0fdf4 0%, #ffffff 100%);
    }
    h1 { color: #166534 !important; }
    .weather-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border: 1px solid #bbf7d0;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("☀️ お天気コンシェルジュ")
st.write("今の都市の天気を調べて、お出かけのアドバイスをします。")

# 1. ユーザー入力
city_name = st.text_input("調べたい都市名を英語で入力してください（例: Tokyo, Osaka, London）", "Tokyo")

if st.button("天気をチェック！"):
    # 2. APIにリクエストを送る
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=ja"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            # データの抽出
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            
            # 3. 結果の表示
            st.markdown(f"""
                <div class="weather-card">
                    <h2 style='color: #15803d;'>📍 {city_name} の今の天気</h2>
                    <h1 style='font-size: 50px; margin: 10px 0;'>{temp} ℃</h1>
                    <p style='font-size: 20px;'>☁️ 状況: {weather} / 💧 湿度: {humidity} %</p>
                </div>
            """, unsafe_allow_html=True)
            
            # 天気に合わせた一言アドバイス
            st.subheader("💡 コンシェルジュからの助言")
            if temp < 10:
                st.info("かなり冷え込んでいます。厚手のコートとマフラーを忘れずに！")
            elif temp < 20:
                st.info("少し肌寒いですね。ジャケットやカーディガンがあると安心です。")
            else:
                st.info("過ごしやすい気温です。軽装でお出かけを楽しんでください！")
                
            if "雨" in weather or "雪" in weather:
                st.warning("外は天気が崩れているようです。傘を持って出かけましょう。")
                
            st.balloons()
            
        else:
            st.error(f"都市名が見つかりませんでした。綴りを確認してください。")
            
    except Exception as e:
        st.error(f"接続にエラーが発生しました。時間を置いて試してください。")

st.markdown("---")
st.caption("Produced by My Weather App | Data provided by OpenWeatherMap")
