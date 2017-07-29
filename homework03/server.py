# Добавьте на сайт страницу /names, на которой в табличном виде выведите данные о именах новорожденных, 
# получаемые при помощи функции из предыдущей задачи.

from flask import Flask, request, render_template
from req_data_mos_ru import get_data
from datetime import date, datetime, timedelta
import settings
from get_date_ru import get_date_ru

app = Flask(__name__)

def get_name_stats():
    api_url = "http://api.data.mos.ru/v1/datasets/2009/rows?api_key={}".format(settings.DATA_MOS_RU_API_KEY)
    data = get_data(api_url)
    
    date_from = get_filter()
    year = timedelta(days=365)
    date_to = date_from + year

    names_list = []
    for data_record in data:
        record_date = datetime.strptime(str(data_record["Cells"]["Year"]), "%Y")
        if date_from <= record_date < date_to:
            names_item = {}
            names_item["Date"] = get_date_ru(data_record["Cells"]["Year"], data_record["Cells"]["Month"])
            names_item["Name"] = data_record["Cells"]["Name"]
            names_item["NumberOfPersons"] = data_record["Cells"]["NumberOfPersons"]
            names_list.append(names_item)

    names_list = sorted(names_list, key=lambda k: k['Name']) 
    names_list = sorted(names_list, key=lambda k: k['Date'], reverse=True) 

    return names_list

def get_filter():
    today = datetime.now()
    default_year = datetime(today.year, 1, 1)

    try:
        year_filter = datetime.strptime(request.args.get("year"), "%Y")
    except ValueError: 
        year_filter = default_year
    except TypeError:
        year_filter = default_year

    return year_filter

# возвращает список лет, по которым есть данные об именах
def get_unique_years():
    api_url = "http://api.data.mos.ru/v1/datasets/2009/rows?api_key={}".format(settings.DATA_MOS_RU_API_KEY)
    data = get_data(api_url)
    dates_list = set()

    for data_record in data:
        dates_list.add(str(data_record["Cells"]["Year"]))

    return sorted(dates_list)


@app.route("/")
def index():
    return render_template("index.html", 
        page_name = "My page",
        page_title= "Most popular girl names in {}".format(datetime.strftime(get_filter(), "%Y")),
        table_data = get_name_stats(),
        available_years = "You can also check out years: {}".format(", ".join(get_unique_years()))
    )


if __name__ == "__main__":
    app.run(debug=True)
