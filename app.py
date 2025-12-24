import streamlit as st
import requests

# --- 設定 ---
API_KEY = "8e8e1efc195bb65308a107e888a1bb6c"

# --- ✨ デザイン設定（冬仕様） ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #e0f2fe 0%, #ffffff 100%);
    }
    .weather-card {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("❄️ 全世界お天気コンシェルジュ")
st.write("日本の都市も、海外の都市も、**日本語で入力**してみてください！")

# --- A案：自由入力（日本語OK） ---
city_input = st.text_input("都市名を入力（例：沖縄、ロサンゼルス、デンバー）", "東京")

if st.button("天気をチェック！"):
    # 💡【ここがポイント】日本語の都市名をAPIが理解できる形式に整える
    # units=metric（摂氏）、lang=ja（説明を日本語に）
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={API_KEY}&units=metric&lang=ja"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            # 取得したデータ
            weather_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            # APIが返してきた正式な都市名（英語）
            formal_name = data["name"]
            
            # 結果表示
            st.markdown(f"""
                <div class="weather-card">
                    <h2 style='color: #1e3a8a;'>📍 {city_input} ({formal_name})</h2>
                    <h1 style='font-size: 60px; margin: 10px 0;'>{temp} ℃</h1>
                    <p style='font-size: 20px;'>状況: {weather_desc} / 湿度: {humidity} %</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.snow() # 冬の演出
            
            # アドバイス
            st.subheader("💡 コンシェルジュからの助言")
            if temp < 5:
                st.error(f"現在の{city_input}は凍える寒さです！しっかり防寒してください。")
            elif temp < 15:
                st.info(f"冬らしい気温です。暖かい服装でお出かけください。")
            else:
                st.success(f"比較的過ごしやすいですね。")
                
        else:
            st.error(f"「{city_input}」という都市が見つかりませんでした。漢字やカタカナが正しいか確認してください。")
            
    except Exception as e:
        st.error(f"接続に失敗しました。")

st.markdown("---")
st.caption("Data provided by OpenWeatherMap API | 全世界日本語検索対応版")
