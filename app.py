from flask import Flask, render_template_string

app = Flask(__name__)

layout = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            background: #f4f4f4;
        }
        nav {
            background: #222;
            padding: 15px;
        }
        nav a {
            color: white;
            margin-right: 20px;
            text-decoration: none;
            font-size: 18px;
        }
        .container {
            padding: 40px;
        }
        h1 {
            font-size: 42px;
            color: #222;
            margin-bottom: 20px;
        }
        p {
            font-size: 20px;
            line-height: 1.6;
        }
        .card {
            background: white;
            padding: 25px;
            margin-top: 20px;
            border-radius: 8px;
            max-width: 700px;
        }
    </style>
</head>
<body>

<nav>
    <a href="/">Home</a>
    <a href="/about">About Us</a>
    <a href="/membership">Membership</a>
</nav>

<div class="container">
    {{ content | safe }}
</div>

</body>
</html>
"""

@app.route("/")
def home():
    content = """
    <h1>Welcome to Our Gym</h1>
    <div class="card">
        <p><strong>Stay fit. Stay healthy. Stay strong.</strong></p>
        <p>✔ Modern gym equipment</p>
        <p>✔ Certified professional trainers</p>
        <p>✔ Friendly and motivating environment</p>
    </div>
    """
    return render_template_string(layout, title="Home", content=content)

@app.route("/about")
def about():
    content = """
    <h1>About Us</h1>
    <div class="card">
        <p>Our gym is dedicated to helping people achieve their fitness goals.</p>
        <p>We provide a clean, safe, and fully equipped environment.</p>
        <p>Our trainers focus on strength, endurance, and overall wellness.</p>
    </div>
    """
    return render_template_string(layout, title="About Us", content=content)

@app.route("/membership")
def membership():
    content = """
    <h1>Membership Plans</h1>
    <div class="card">
        <p><strong>Basic Plan:</strong> $20 / month</p>
        <p><strong>Standard Plan:</strong> $35 / month</p>
        <p><strong>Premium Plan:</strong> $50 / month</p>
    </div>
    """
    return render_template_string(layout, title="Membership", content=content)

if __name__ == "__main__":
    app.run(debug=True)
