from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
   return """
<!DOCTYPE html>
<html>
<head>
    <title>Production App</title>
    <style>
        body {
            background:#0f172a;
            color:white;
            text-align:center;
            padding-top:100px;
            font-family:Arial;
        }
        .card {
            background:#1e293b;
            width:500px;
            margin:auto;
            padding:40px;
            border-radius:10px;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>ECS Fargate Deployment Successful</h1>
        <p>Application accessible via ALB</p>
        <p>EventBridge scheduler active</p>
    </div>
</body>
</html>
"""

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)