from flask import Flask

app = Flask(__name__)

# Giao diện HTML vừa đủ đẹp, trình bày rõ ràng
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Server - Lab 06</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f0f2f5; display: flex; justify-content: center; padding-top: 50px; }
        .box { background: white; padding: 30px; border-radius: 10px; shadow: 0 4px 8px rgba(0,0,0,0.1); width: 500px; border-top: 6px solid #007bff; }
        h2 { color: #007bff; text-align: center; }
        .info { margin-bottom: 15px; font-size: 18px; border-bottom: 1px solid #eee; padding-bottom: 10px; }
        b { color: #333; }
        .status { color: green; font-weight: bold; text-align: center; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="box">
        <h2>KẾT QUẢ CÂU 6.6.1</h2>
        <div class="info"><b>Họ tên:</b> Huynh Ngoc Dat</div>
        <div class="info"><b>MSSV:</b> 0423</div>
        <div class="info"><b>Nội dung:</b> Triển khai Web Server cơ bản</div>
        <div class="status">● Server status: Online</div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return HTML_TEMPLATE

if __name__ == '__main__':
    # Chạy trên port 5000, host 0.0.0.0 để máy khác cũng truy cập được
    app.run(host='0.0.0.0', port=5000)