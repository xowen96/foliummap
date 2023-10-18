# app.py

from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static', static_folder='static')
# 샘플 지하철역 데이터
subway_stations = [
    {"name": "역삼역", "latitude": 37.501417, "longitude": 127.038572},
    {"name": "강남역", "latitude": 37.497942, "longitude": 127.027621},
    {"name": "잠실역", "latitude": 37.513060, "longitude": 127.100542},
    # 나머지 지하철역 데이터를 추가
]

# 카테고리 및 필터 옵션 데이터
categories = {
    "지하철역": ["1호선","2호선","3호선","신분당선","5호선","GTX (예정)"],
    "고등학교": ["국립", "사립", "기숙사형 사립","특성화"],
    "관공서": ["Y", "N"],
    "병원": ["종합병원", "의원"],
    "조건 직접 입력": [" 7002번 버스노선 ", " 인근에 스타벅스가 위치해 있으면 좋겠어요 "],
    "자본금 직접 선택 ": [" ~ 1억 ", " ~ 2억 ", " ~ 3억 ", "~ 4억 ", " ~5억 ", " ~ 5억 이상 "]
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 사용자가 선택한 카테고리 및 필터 정보를 가져오는 코드
        selected_category = request.form.get("category")
        selected_filter = request.form.get("filter")

    return render_template("index.html", subway_stations=subway_stations, categories=categories)

if __name__ == "__main__":
    app.run(debug=True)
