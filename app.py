from flask import Flask, render_template, send_from_directory

app = Flask(
    __name__,
    template_folder="pages",
    static_folder="style",
    static_url_path="/style",
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scripts/<path:filename>")
def scripts(filename):
    return send_from_directory("scripts", filename)

@app.route("/table")
def table():
    flights = {
        "flight_1": {"departure_time": "06:15", "arrival_time": "08:40", "from_code": "MSK", "to_code": "VLG", "flight_number": "SU 120", "price": "от 4 900 руб."},
        "flight_2": {"departure_time": "07:30", "arrival_time": "09:55", "from_code": "LED", "to_code": "KZN", "flight_number": "DP 214", "price": "от 5 200 руб."},
        "flight_3": {"departure_time": "08:10", "arrival_time": "10:35", "from_code": "AER", "to_code": "MSK", "flight_number": "FV 305", "price": "от 6 100 руб."},
        "flight_4": {"departure_time": "09:05", "arrival_time": "11:20", "from_code": "VLG", "to_code": "MSK", "flight_number": "SU 188", "price": "от 4 450 руб."},
        "flight_5": {"departure_time": "10:00", "arrival_time": "12:15", "from_code": "MSK", "to_code": "AER", "flight_number": "DP 134", "price": "от 6 850 руб."},
        "flight_6": {"departure_time": "11:45", "arrival_time": "14:05", "from_code": "KZN", "to_code": "LED", "flight_number": "SU 442", "price": "от 3 100 руб."},
        "flight_7": {"departure_time": "12:20", "arrival_time": "14:55", "from_code": "MSK", "to_code": "ROV", "flight_number": "FV 501", "price": "от 5 750 руб."},
        "flight_8": {"departure_time": "13:10", "arrival_time": "15:45", "from_code": "ROV", "to_code": "MSK", "flight_number": "SU 211", "price": "от 4 980 руб."},
        "flight_9": {"departure_time": "14:40", "arrival_time": "17:20", "from_code": "LED", "to_code": "MOW", "flight_number": "DP 518", "price": "от 3 650 руб."},
        "flight_10": {"departure_time": "15:05", "arrival_time": "17:40", "from_code": "MOW", "to_code": "LED", "flight_number": "SU 110", "price": "от 2 980 руб."},
        "flight_11": {"departure_time": "16:00", "arrival_time": "18:25", "from_code": "MSK", "to_code": "KZN", "flight_number": "FV 410", "price": "от 3 880 руб."},
        "flight_12": {"departure_time": "16:35", "arrival_time": "19:10", "from_code": "KZN", "to_code": "MSK", "flight_number": "SU 905", "price": "от 3 420 руб."},
        "flight_13": {"departure_time": "17:20", "arrival_time": "19:45", "from_code": "VLG", "to_code": "LED", "flight_number": "DP 402", "price": "от 4 120 руб."},
        "flight_14": {"departure_time": "18:15", "arrival_time": "20:40", "from_code": "LED", "to_code": "VLG", "flight_number": "SU 277", "price": "от 4 980 руб."},
        "flight_15": {"departure_time": "19:10", "arrival_time": "21:35", "from_code": "MSK", "to_code": "KRR", "flight_number": "FV 612", "price": "от 5 500 руб."},
        "flight_16": {"departure_time": "20:00", "arrival_time": "22:25", "from_code": "KRR", "to_code": "MSK", "flight_number": "SU 335", "price": "от 5 250 руб."},
        "flight_17": {"departure_time": "06:50", "arrival_time": "09:05", "from_code": "MSK", "to_code": "UFA", "flight_number": "DP 703", "price": "от 4 660 руб."},
        "flight_18": {"departure_time": "07:45", "arrival_time": "09:55", "from_code": "UFA", "to_code": "MSK", "flight_number": "SU 704", "price": "от 4 820 руб."},
        "flight_19": {"departure_time": "08:30", "arrival_time": "10:50", "from_code": "MSK", "to_code": "SVX", "flight_number": "FV 520", "price": "от 5 900 руб."},
        "flight_20": {"departure_time": "09:20", "arrival_time": "11:45", "from_code": "SVX", "to_code": "MSK", "flight_number": "SU 980", "price": "от 6 100 руб."},
        "flight_21": {"departure_time": "10:15", "arrival_time": "12:35", "from_code": "MSK", "to_code": "TJM", "flight_number": "DP 630", "price": "от 7 280 руб."},
        "flight_22": {"departure_time": "11:10", "arrival_time": "13:30", "from_code": "TJM", "to_code": "MSK", "flight_number": "SU 881", "price": "от 7 050 руб."},
        "flight_23": {"departure_time": "12:05", "arrival_time": "14:25", "from_code": "MSK", "to_code": "OMS", "flight_number": "FV 271", "price": "от 8 150 руб."},
        "flight_24": {"departure_time": "13:00", "arrival_time": "15:20", "from_code": "OMS", "to_code": "MSK", "flight_number": "SU 290", "price": "от 8 420 руб."},
        "flight_25": {"departure_time": "14:05", "arrival_time": "16:30", "from_code": "MSK", "to_code": "KUF", "flight_number": "DP 832", "price": "от 4 350 руб."},
        "flight_26": {"departure_time": "15:15", "arrival_time": "17:40", "from_code": "KUF", "to_code": "MSK", "flight_number": "SU 833", "price": "от 4 520 руб."},
        "flight_27": {"departure_time": "16:25", "arrival_time": "18:50", "from_code": "MSK", "to_code": "DME", "flight_number": "FV 660", "price": "от 2 350 руб."},
        "flight_28": {"departure_time": "17:35", "arrival_time": "19:55", "from_code": "DME", "to_code": "MSK", "flight_number": "SU 661", "price": "от 2 450 руб."},
        "flight_29": {"departure_time": "18:40", "arrival_time": "21:05", "from_code": "MSK", "to_code": "PEK", "flight_number": "DP 119", "price": "от 14 200 руб."},
        "flight_30": {"departure_time": "19:50", "arrival_time": "22:20", "from_code": "PEK", "to_code": "MSK", "flight_number": "SU 120", "price": "от 14 900 руб."},
    }

    return render_template("table.html", flights=flights.values())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)