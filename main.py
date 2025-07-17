from flask import Flask, request, jsonify, Response, render_template_string
import json
import time
import threading
import requests
import random
import re
from uuid import uuid4

app = Flask(__name__)
app.secret_key = str(uuid4())

# HTML Template with modern design
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Fb Comment Master Pro</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        :root {
            --primary-color: #4a90e2;
            --background-color: #1a1a1a;
            --card-bg: #2d2d2d;
        }
        
        body {
            background: var(--background-color);
            color: #fff;
            font-family: 'Arial', sans-serif;
        }
        
        .container {
            max-width: 1200px;
            padding: 2rem;
        }
        
        .task-box {
            background: var(--card-bg);
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }
        
        .task-box:hover {
            transform: translateY(-3px);
        }
        
        .form-control {
            background: #333;
            border: 1px solid #444;
            color: #fff;
            padding: 1rem;
            margin-bottom: 1.5rem;
        }
        
        .form-control:focus {
            background: #444;
            border-color: var(--primary-color);
            box-shadow: none;
        }
        
        .live-logs {
            height: 400px;
            background: #000;
            border-radius: 8px;
            padding: 1rem;
            font-family: 'Courier New', monospace;
            color: #00ff00;
            overflow-y: auto;
        }
        
        .btn-custom {
            background: var(--primary-color);
            border: none;
            padding: 1rem 2rem;
            font-size: 1.1rem;
            transition: all 0.3s;
        }
        
        .btn-custom:hover {
            background: #357abd;
            transform: scale(1.02);
        }
        
        h2 {
            color: var(--primary-color);
            text-align: center;
            margin-bottom: 2rem;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>⚡ Facebook Comment System Pro</h2>
        
        <form id="mainForm" enctype="multipart/form-data">
            <div class="row g-4">
                <div class="col-md-6">
                    <textarea class="form-control" name="cookies" rows="7" 
                        placeholder="Paste JSON Cookies Here..." required></textarea>
                    <input type="text" class="form-control" name="post_id" 
                        placeholder="Facebook Post ID" required>
                </div>
                
                <div class="col-md-6">
                    <div class="row g-3">
                        <div class="col-md-6">
                            <input type="text" class="form-control" name="prefix" 
                                placeholder="Name Prefix" required>
                        </div>
                        <div class="col-md-6">
                            <input type="text" class="form-control" name="suffix" 
                                placeholder="Name Suffix" required>
                        </div>
                    </div>
                    
                    <input type="file" class="form-control" name="comments_file" required>
                    
                    <div class="input-group">
                        <span class="input-group-text">Delay (Seconds)</span>
                        <input type="number" class="form-control" name="delay" 
                            value="15" min="5" required>
                    </div>
                </div>
            </div>
            
            <button type="submit" class="btn btn-custom w-100 mt-4">
                🚀 Start Commenting Process
            </button>
        </form>

        <div class="mt-5">
            <h4 class="mb-3">📊 Active Tasks</h4>
            <div id="tasksContainer"></div>
        </div>

        <div class="mt-5">
            <h4 class="mb-3">📜 Live Activity Logs</h4>
            <div class="live-logs" id="liveLogs"></div>
        </div>
    </div>

    <script>
        // ... (Keep the same JavaScript code as original) ...
    </script>
</body>
</html>
'''

# Global tasks tracker (same as original)
active_tasks = {}
task_logs = {}
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1"
]

def facebook_comment_task(task_id, data):
    # ... (Keep same task function but remove whatsapp notification calls) ...
    # Remove these lines:
    # send_whatsapp_notification(...)
    
# ... (Keep all route handlers the same as original but remove Twilio references) ...

if __name__ == '__main__':
    app.run(debug=True, port=4000)
