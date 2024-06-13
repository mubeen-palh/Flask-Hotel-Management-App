from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('page1.html')

@app.route("/second")
def second_page():
    return render_template('page2.html')

@app.route('/third', methods=["POST", "GET"])
def third_page():
    # this if statement gets the username, password and email from the user
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Data validation
        errors = []
        if not username:
            errors.append("Username is required.")
        if len(username) < 4:
            errors.append("Username must be at least 4 characters long.")
        if not email or "@" not in email:
            errors.append("Invalid email address.")
        if not password or len(password) < 8:
            errors.append("Password must be at least 8 characters long.")

        if errors:
            return render_template('page3.html', errors=errors)
        else:
            return f"Account created successfully! (Username: {username}, Email: {email})"
        
    return render_template('page3.html')

@app.route('/fourth', methods=["POST", "GET"])
def fourth_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Data validation
        errors = []
        if not username:
            errors.append("Username is required.")
        if not password:
            errors.append("Password is required.")      

        if errors:
            return render_template('page4.html', errors=errors)
        else:
            return f"Login successfully! (Username: {username})"
        
    return render_template('page4.html')


@app.route("/fifth", methods=["POST", "GET"])
def fifth_page():
    code = request.form.get("code")
    errors = []
    # code validation
    if code == "1234": 
        errors.append("Code verified!")
    else:
        errors.append("Invalid verification code.")

    if errors:
        return render_template('page5.html', errors=errors)

    return render_template('page5.html')

@app.route('/sixth')
def sixth_page():
    return render_template('page6.html')

@app.route("/seventh",  methods=["POST", "GET"])
def hotel_details():
    hotel_name = "The Aston Villa Hotel"
    description = "This is a luxurious hotel located in a vibrant location. It offers ..."
    contact_info = "John Mail, m"  # Replace with complete contact info
    return render_template("page7.html", hotel_name=hotel_name, description=description, contact_info=contact_info)

@app.route("/eighth",  methods=["POST", "GET"])
def list_schedule():
    schedule_entries = []
    for i in range(1, 6):  # Generate 5 sample schedule entries
        schedule_entry = {
            "date": f"Date {i}",
            "location": f"Location {i}",
            "description": f"Description {i}",
        }
        schedule_entries.append(schedule_entry)
    return render_template("page8.html", schedule_entries=schedule_entries)

@app.route("/ninth",  methods=["POST", "GET"])
def booking_summary():
    # This dictionary stores Booking data
    booking_data = {
        "booking_date": "01-Jan-2024",
        "check_in": "24-Oct-2023",
        "check_out": "26-Oct-2023",
        "guests": 2,
        "rooms": [
            {"name": "Standard Room", "amount": 350}
        ],
        "amount": 350,
        "tax": 30,
        "total": 380
    }
    return render_template("page9.html", booking_data=booking_data)

@app.route("/tenth",  methods=["POST", "GET"])
def booking_next():
    booking_data2 = {
        "total_price": 750.00,
        "payment_method": "VISA",
        "card_holder": "Your Name",
    }
    return render_template("page10.html", booking_data =booking_data2)

@app.route("/eleventh",  methods=["POST", "GET"])
def finish_page():
    # this is the last page for displays congratulations 
    return render_template("page11.html")


if __name__ == "__main__":
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
