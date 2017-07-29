import requests
import settings

def get_data(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        print("ERROR: return code {}".format(r.status_code))

if __name__ == "__main__":
    api_url = "http://api.data.mos.ru/v1/datasets/2009/rows?api_key={}".format(settings.DATA_MOS_RU_API_KEY)
    data = get_data(api_url)

    print(data[1])
