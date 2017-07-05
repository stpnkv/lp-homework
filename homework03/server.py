# Добавьте на сайт страницу /names, на которой в табличном виде выведите данные о именах новорожденных, 
# получаемые при помощи функции из предыдущей задачи.

from flask import Flask, request
from req_data_mos_ru import get_data
from datetime import date, datetime
import settings
from get_date_ru import get_date_ru

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/names")
def get_names():
    api_url = "http://api.data.mos.ru/v1/datasets/2009/rows?api_key={}".format(settings.DATA_MOS_RU_API_KEY)
    data = get_data(api_url)

    try:
        year_filter = int(request.args.get("year"))
    except ValueError: 
        year_filter = ""
    except TypeError:
        year_filter = ""

    content = ""
    for element in data:
        if year_filter == "":
            content += "<tr>"
            content += "<td>{}</td>".format(get_date_ru(element["Cells"]["Year"], element["Cells"]["Month"]).strftime('%Y.%m'))
            content += "<td>{}</td>".format(element["Cells"]["Name"])
            content += "<td>{}</td>".format(element["Cells"]["NumberOfPersons"])
            content += "</tr>"
            caption = "<h1>Showing all available data</h1>"
        else:
            if element["Cells"]["Year"] == year_filter:
                content += "<tr>"
                content += "<td>{}</td>".format(get_date_ru(element["Cells"]["Year"], element["Cells"]["Month"]).strftime('%Y.%m'))
                content += "<td>{}</td>".format(element["Cells"]["Name"])
                content += "<td>{}</td>".format(element["Cells"]["NumberOfPersons"])
                content += "</tr>"
                caption = "<h1>Showing data for year {}</h1>".format(year_filter)
    
    if content == "":
        caption = "<h1>Sorry, no data found for year {}</h1>".format(year_filter)

    with open('template.html', 'r', encoding='utf-8') as f:
        template = ""
        for line in f:
            if line.replace(' ','').replace('\n','').replace('\r','') == "<!--caption-->":
                template += caption
            if line.replace(' ','').replace('\n','').replace('\r','') == "<!--contents-->":
                template += content
            else:
                template += line
    return template

if __name__ == "__main__":
    app.run(debug=True)
