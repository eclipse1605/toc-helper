from flask import Flask, render_template, send_from_directory, jsonify, request
import time
import os

app = Flask(__name__)

@app.route("/")
def home():
    """Render the main application page"""
    return render_template("index.html", time=int(time.time()))

@app.route("/save", methods=["POST"])
def save_diagram():
    """Save diagram data (for future restoration)"""
    # This could be expanded to actually save diagrams to a database or files
    # For now, just return success response
    return jsonify({"success": True, "message": "Diagram saved successfully"})

@app.route("/examples/<example_name>")
def load_example(example_name):
    """Load example diagrams"""
    examples = {
        "simple": {"nodes": [{"x": 200, "y": 200, "text": "q0", "isAcceptState": False},
                          {"x": 400, "y": 200, "text": "q1", "isAcceptState": True}],
                 "links": [{"type": "link", "nodeA": 0, "nodeB": 1, "text": "1"}]},
        "dfa": {"nodes": [{"x": 200, "y": 200, "text": "q0", "isAcceptState": False},
                        {"x": 400, "y": 200, "text": "q1", "isAcceptState": True},
                        {"x": 300, "y": 350, "text": "q2", "isAcceptState": False}],
               "links": [{"type": "link", "nodeA": 0, "nodeB": 1, "text": "1"},
                         {"type": "link", "nodeA": 0, "nodeB": 2, "text": "0"},
                         {"type": "link", "nodeA": 1, "nodeB": 1, "text": "1"},
                         {"type": "link", "nodeA": 1, "nodeB": 2, "text": "0"},
                         {"type": "link", "nodeA": 2, "nodeB": 0, "text": "0,1"}]}
    }
    
    if example_name in examples:
        return jsonify(examples[example_name])
    return jsonify({"error": "Example not found"}), 404

@app.route("/themes/<theme_name>")
def get_theme(theme_name):
    """Get color theme for the application"""
    themes = {
        "dark": {"background": "#121212", "canvas": "#1e1e1e", "text": "#ffffff", "accent": "#3498db"},
        "light": {"background": "#f5f5f5", "canvas": "#ffffff", "text": "#333333", "accent": "#2980b9"},
        "nord": {"background": "#2e3440", "canvas": "#3b4252", "text": "#eceff4", "accent": "#88c0d0"},
        "monokai": {"background": "#272822", "canvas": "#2d2e27", "text": "#f8f8f2", "accent": "#a6e22e"}
    }
    
    if theme_name in themes:
        return jsonify(themes[theme_name])
    return jsonify(themes["dark"])  # Return default theme if not found

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
