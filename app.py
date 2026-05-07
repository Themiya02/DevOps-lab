from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DevOps Dashboard</title>
        <style>
            body {
                background-color: #0d1117; /* Dark Blue/Black */
                color: #c9d1d9;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 12px;
                padding: 40px;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                max-width: 500px;
                width: 100%;
            }
            h1 {
                color: #58a6ff;
                margin-bottom: 10px;
                font-size: 2.5rem;
            }
            .status {
                background-color: #238636;
                color: white;
                padding: 5px 15px;
                border-radius: 20px;
                font-size: 0.9rem;
                display: inline-block;
                margin-bottom: 20px;
            }
            .details {
                font-size: 1.1rem;
                margin: 10px 0;
                line-height: 1.6;
            }
            .tech-stack {
                margin-top: 25px;
                padding-top: 20px;
                border-top: 1px solid #30363d;
                font-size: 0.85rem;
                color: #8b949e;
            }
            b { color: #ffffff; }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="status">● SYSTEM ONLINE</div>
            <h1>DevOps Pipeline</h1>
            <div class="details">
                <p>Deployment Status: <b>Successful ✅</b></p>
                <p>Environment: <b>Docker Container</b></p>
                <p>Developed by: <b>Chirath Themiya</b></p>
            </div>
            <div class="tech-stack">
                Built with: Python | Flask | Docker | GitHub Actions | WSL 2
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
