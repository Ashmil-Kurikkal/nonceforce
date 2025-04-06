from flask import Flask, render_template, request, jsonify
from core import parallel_brute_force

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def clean_int(value):
    if isinstance(value, (tuple, list)):
        value = value[0]
    return int(str(value).strip().replace(" ", ""))

def clean_hex(value):
    if isinstance(value, (tuple, list)):
        value = value[0]
    return int(str(value).strip().replace(" ", ""), 16)

@app.route("/bruteforce", methods=["POST"])
def bruteforce():
    data = request.json
    try:
        p = clean_int(data["p"])
        q = clean_int(data["q"])
        g = clean_int(data["g"])
        r = clean_int(data["r"])
        s = clean_int(data["s"])
        hashed_message = clean_hex((data["hashed_message"], 16))
        k_min = clean_int(data["k_min"])
        k_max = clean_int(data["k_max"])

        result = parallel_brute_force(k_min, k_max, p, q, g, r, s, hashed_message)

        if result:
            return jsonify({"status": "success", "k": result[0], "priv_key": str(result[1])})
        else:
            return jsonify({"status": "error", "message": "No valid k found."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
