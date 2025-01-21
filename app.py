
from flask import Flask, request, jsonify
from flask_cors import CORS
from help import extract_text_from_pdf, extract_text_from_image, generate_summary;


app= Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the API. Use the /uploads endpoint to upload files."})

@app.route("/uploads", methods=["POST"])
def upload_file():
    print("Line10")
    file = request.files["file"]
    summary_length = request.form.get("summary_length", "medium")
    print("Line13")

    if file.content_type == "application/pdf":
        text = extract_text_from_pdf(file)
    elif "image" in file.content_type:
        text = extract_text_from_image(file)
    else:
        return jsonify({"error": "Unsupported file type"}), 400

    summary = generate_summary(text, summary_length)
    return jsonify({"summary": summary})


if __name__== "__main__":    
     app.run(host="0.0.0.0", port=5000)

