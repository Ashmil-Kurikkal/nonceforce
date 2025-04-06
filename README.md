# 🛠️ DSA Nonce Brute-Forcer (CPU Multiprocessing)


## 🚀 Overview  
This script is designed to brute-force the **nonce (k) value** used in a **DSA (Digital Signature Algorithm)** signing process, leveraging **multiprocessing** for faster computation.  The script expects a known p, q, g and a known (r,s) value.

It targets **weak nonce generation vulnerabilities** and attempts to recover the **private key** using a brute-force approach on the **k** value.

---

## 🔍 Features  
- **Parallel brute-forcing** using Python's multiprocessing module.  
- **Optimized CPU usage** to speed up calculations.  
- **Supports large keyspaces** without requiring GPU acceleration.   
- **Interactive CLI & Web App Interface** for testing different DSA parameters.
---

## 🛠️ Requirements  
- Python 3.x  
- **Multiprocessing module** (built into Python)  
- `pyfiglet`
- `colorama`

---

## 📦 Installation

**Choose your flavour :**

Download both anyways

- **Web Interface (main branch)**
   ```bash
   git clone https://github.com/Ashmil-Kurikkal/nonceforce
   cd nonceforce/webapp
   pip install -r requirements.txt 
   ```

- **Prefer sticking to the CLI, hacker? Command Line Interface (cli branch)**
   ```bash
   git clone https://github.com/Ashmil-Kurikkal/nonceforce
   cd nonceforce/cli
   pip install -r requirements.txt
   ```

## 🔹Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/Ashmil-Kurikkal/nonceforce

2. Open the cloned repository  
   ```sh
   cd nonceforce

3. Run server.py
      1. if you downloaded the webapp
         ```sh
         #for web app
         python3 server.py
         #The server will be running on http://127.0.0.1:5000 (Local Host port 5000), on your browser search for
         http://127.0.0.1:5000
         ```

      2. else run nonceforce.py directly
         ```sh
         #for standalone CLI script
         python3 nonceforce.py
         ```

4. Provide the required parameters.

5. Wait until you get the result!

## 🔹 Performance Considerations
High CPU Usage: The script utilizes all available CPU cores, leading to 100% utilization.

Thermal Throttling: Extended usage may cause overheating on inadequately cooled systems.

Optimizing Performance:

Adjust the worker process count to balance speed and CPU load.

## 🔹 Disclaimer
This tool is developed strictly for educational and ethical hacking purposes. It is primarily relevant in CTF (Capture The Flag) environments or controlled scenarios and may not be applicable in real-world applications.

The script was originally created for a CTF challenge where the DSA implementation lacked sufficient randomness in nonce generation. In that scenario, all necessary parameters were exposed via admin logs—a condition unlikely in real-life systems.

This is intended as a proof of concept to demonstrate how weak or predictable nonce values can critically compromise the security of DSA. Do not use this tool against any unauthorized or real-world digital signature systems.