import streamlit as st
import requests

# --- 設定 ---
# 💡 ご自身のAPIキーをここに貼り付けてください
API_KEY = "8e8e1efc195bb65308a107e888a1bb6c"

# --- ✨ デザイン設定（視認性最強・水色デザイン） ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0ea5e9 0%, #38bdf8 100%);
    }
    
    /* 入力欄の上の文字（ラベル）を白く太くする */
    .stMarkdown p, label {
        color: white !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
    }

    h1 {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    /* 天気カード：真っ白にして中の文字を濃い紺にする */
    .weather-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
        text-align: center;
        margin: 20px 0;
    }
    
    .weather-card h1, .weather-card h2, .weather-card p {
        color: #0c4a6e !important; /* 濃い紺色 */
    }

    /* ボタン */
    div.stButton > button:first-child {
        background-color: #f8fafc !important;
        color: #0ea5e9 !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        border: none !important;
        height: 3em !important;
        width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("☀️ お天気コンシェルジュ")
st.write("日本の都市も、海外の都市も、日本語で入力してみてください！")

# --- 入力エリア ---
city_input = st.text_input("都市名を入力（例：大阪、那覇、札幌、デンバー）", "大阪")

if st.button("天気をチェック！"):
    # 💡 修正ポイント：日本語をより確実に送るためのURLエンコード対応
    # requestsが自動で処理してくれますが、パラメータをより明確に分けました
    params = {
        "q": city_input,
        "appid": API_KEY,
        "units": metric",
        "lang": "ja"
    }
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            weather_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            formal_name = data["name"]
            
            st.markdown(f"""
                <div class="weather-card">
                    <h2 style='margin: 0;'>📍 {city_input}</h2>
                    <p style='color: #64748b; margin-bottom: 10px;'>({formal_name})</p>
                    <h1 style='font-size: 60px; margin: 10px 0;'>{temp} ℃</h1>
                    <p style='font-size: 20px; font-weight: bold;'>{weather_desc} / 湿度: {humidity} %</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.snow()
            
            st.subheader("💡 アドバイス")
            if temp < 10:
                st.info("寒いですね！温かい格好でお出かけください。")
            elif temp < 20:
                st.info("過ごしやすいですが、羽織るものがあると安心です。")
            else:
                st.success("暖かいですね！お出かけ日和です。")
                
        else:
            # エラーの詳細を表示して原因を突き止めやすくする
            st.error(f"「{city_input}」が見つかりませんでした。理由: {data.get('message', '不明なエラー')}")
            
    except Exception as e:
        st.error(f"接続エラーが発生しました。")

st.markdown("---")
st.caption("Produced by My Weather App | Winter Edition")
