import streamlit as st
import requests

# --- 設定 ---
# 💡 ここにご自身のAPIキーを貼り付けてください
API_KEY = "8e8e1efc195bb65308a107e888a1bb6c"

# --- ✨ デザイン設定（視認性重視の水色デザイン） ---
st.markdown("""
    <style>
    /* 1. 全体の背景：ハッキリとした水色のグラデーション */
    .stApp {
        background: linear-gradient(135deg, #7dd3fc 0%, #38bdf8 100%);
    }
    
    /* 2. 入力ラベルなどの文字色を白にして見やすくする */
    .stMarkdown p, label {
        color: white !important;
        font-weight: bold !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }

    /* 3. メインのタイトル */
    h1 {
        color: white !important;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    /* 4. 天気結果のカード：真っ白にして文字を黒（濃い紺）にする */
    .weather-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
        text-align: center;
        margin-top: 20px;
    }
    
    .weather-card h2, .weather-card h1, .weather-card p {
        color: #0c4a6e !important; /* 濃い紺色 */
        text-shadow: none !important;
    }

    /* 5. ボタンのデザイン */
    div.stButton > button:first-child {
        background-color: #0ea5e9 !important;
        color: white !important;
        border: 2px solid white !important;
        border-radius: 10px !important;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("❄️ 全世界お天気コンシェルジュ")
st.write("日本の都市も、海外の都市も、日本語で入力してみてください！")

# --- 入力エリア ---
city_input = st.text_input("都市名を入力（例：那覇、札幌、デンバー）", "東京")

if st.button("天気をチェック！"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={API_KEY}&units=metric&lang=ja"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            formal_name = data["name"]
            
            # 結果表示（白いカードで視認性抜群）
            st.markdown(f"""
                <div class="weather-card">
                    <h2 style='margin-bottom: 0;'>📍 {city_input}</h2>
                    <p style='font-size: 0.9em; color: #64748b;'>({formal_name})</p>
                    <h1 style='font-size: 64px; margin: 10px 0;'>{temp} ℃</h1>
                    <p style='font-size: 20px; font-weight: bold;'>{weather_desc} / 湿度: {humidity} %</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.snow() # 冬の演出
            
            # アドバイスエリア（カードの外）
            st.subheader("💡 コンシェルジュからの助言")
            if temp < 5:
                st.error(f"現在の{city_input}は凍える寒さです！最高レベルの防寒を。")
            elif temp < 15:
                st.info(f"冬らしい気温です。暖かい服装でお出かけください。")
            else:
                st.success(f"比較的過ごしやすいですね。お出かけ日和です。")
                
        else:
            st.error(f"「{city_input}」が見つかりませんでした。")
            
    except Exception as e:
        st.error(f"エラーが発生しました。")

st.markdown("---")
st.caption("Produced by My Weather App | Winter Edition")
