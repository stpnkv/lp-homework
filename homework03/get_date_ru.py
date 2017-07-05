from datetime import date 

def get_date_ru(year, month):
    m = month.lower()
    num_month = {
        "январь": 1,
        "февраль": 2,
        "март": 3,
        "апрель": 4,
        "май": 5,
        "июнь": 6,
        "июль": 7,
        "август": 8,
        "сентябрь": 9,
        "октябрь": 10,
        "ноябрь": 11,
        "декабрь": 12
    }[m]
    num_year = int(year)
    dt = date(num_year, num_month, 1)
    return dt

if __name__ == "__main__":
    main()
