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
            background: #0f172a;
            color: white;
            text-align: center;
            padding-top: 100px;
            font-family: Arial, sans-serif;
        }

        .card {
            background: #1e293b;
            width: 500px;
            margin: auto;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0px 0px 20px rgba(255,255,255,0.1);
        }

        h1 {
            color: #38bdf8;
        }

        p {
            font-size: 18px;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>ECS Fargate Deployment Successful</h1>
        <p>Application accessible via ALB</p>
        <p>Jenkins CI/CD Pipeline Working</p>
        <p>ECR Image Deployment Successful</p>
        <p>AWS Region: ap-south-2</p>
    </div>
</body>
</html>
"""

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
