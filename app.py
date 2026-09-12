import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Duration Converter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            width: 650px;
        }
        .header-box {
            background-color: #f1f3f5;
            padding: 12px 15px;
            border-radius: 6px;
            margin-bottom: 20px;
            font-weight: bold;
            color: #333;
            border: 1px solid #ddd;
        }
        .converter-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
        }
        .card {
            background-color: #f8f9fa;
            border: 1px solid #ced4da;
            border-radius: 8px;
            padding: 12px 15px;
        }
        .card input {
            width: 100%;
            font-size: 22px;
            border: none;
            background: transparent;
            outline: none;
            font-weight: bold;
            color: #212529;
        }
        .card label {
            font-size: 13px;
            color: #495057;
            display: block;
            margin-top: 5px;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header-box">
        Duration Converter
    </div>
    
    <div class="converter-grid">
        <div class="card">
            <input type="number" id="days" value="356" oninput="convertFrom('days')">
            <label>Days</label>
        </div>

        <div class="card">
            <input type="number" id="hours" value="8544" oninput="convertFrom('hours')">
            <label>Hours</label>
        </div>

        <div class="card">
            <input type="number" id="minutes" value="512640" oninput="convertFrom('minutes')">
            <label>Minutes</label>
        </div>

        <div class="card">
            <input type="number" id="seconds" value="30758400" oninput="convertFrom('seconds')">
            <label>Seconds</label>
        </div>
    </div>
</div>

<script>
    function convertFrom(source) {
        let daysInput = document.getElementById('days');
        let hoursInput = document.getElementById('hours');
        let minutesInput = document.getElementById('minutes');
        let secondsInput = document.getElementById('seconds');

        let totalSeconds = 0;

        if (source === 'days' && daysInput.value !== '') {
            totalSeconds = parseFloat(daysInput.value) * 86400;
        } else if (source === 'hours' && hoursInput.value !== '') {
            totalSeconds = parseFloat(hoursInput.value) * 3600;
        } else if (source === 'minutes' && minutesInput.value !== '') {
            totalSeconds = parseFloat(minutesInput.value) * 60;
        } else if (source === 'seconds' && secondsInput.value !== '') {
            totalSeconds = parseFloat(secondsInput.value);
        }

        if (isNaN(totalSeconds)) return;

        if (source !== 'days') daysInput.value = (totalSeconds / 86400).toFixed(2);
        if (source !== 'hours') hoursInput.value = (totalSeconds / 3600).toFixed(2);
        if (source !== 'minutes') minutesInput.value = (totalSeconds / 60).toFixed(2);
        if (source !== 'seconds') secondsInput.value = totalSeconds.toFixed(2);
    }
</script>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)