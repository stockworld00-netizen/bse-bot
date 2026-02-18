import requests

def get_latest_announcements():
    url = "https://api.bseindia.com/BseIndiaAPI/api/AnnSubCategoryGetData/w"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.bseindia.com/"
    }
    params = {
        "pageno": 1,
        "strCat": -1,
        "strSearch": "P",
        "strType": "C",
        "subcategory": -1
    }
    response = requests.get(url, headers=headers, timeout=10)
    data = response.json()
    return data.get("Table", [])[:20]  # only latest 20 announcements
