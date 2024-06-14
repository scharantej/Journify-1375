
# main.py

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plan_trip', methods=['POST'])
def plan_trip():
    destination = request.form.get('destination')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')

    # Sample data for demonstration purposes
    itinerary = {
        "destinations": [destination],
        "travel_dates": [start_date, end_date],
        "activities": ["Activity A", "Activity B"],
        "accommodations": ["Hotel A", "Hotel B"]
    }

    return render_template('results.html', itinerary=itinerary)

if __name__ == '__main__':
    app.run(debug=True)
