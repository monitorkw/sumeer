import json
import urllib.request
from datetime import datetime, timezone, timedelta


# 新発田市付近のWBGTデータ取得先
url = "https://www.wbgt.env.go.jp/forecast_data.php"


try:
    # ここで環境省データ取得
    # 実際のJSON形式に合わせて後ほど調整
    response = urllib.request.urlopen(url)
    data = response.read()

except Exception as e:
    print("取得エラー:", e)
    exit(1)


# 日本時間
jst = timezone(timedelta(hours=9))
now = datetime.now(jst)


# 仮データ保存
# 実データ取得部分は環境省データ形式確認後に調整
wbgt_data = {
    "wbgt": 0,
    "time": now.strftime("%H:%M")
}


with open("wbgt.json", "w", encoding="utf-8") as f:
    json.dump(wbgt_data, f, ensure_ascii=False, indent=2)


print("WBGT更新完了")
