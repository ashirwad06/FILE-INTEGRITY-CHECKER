import hashlib
import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

HASH_FILE = "hashes.json"
LOG_FILE = "log.txt"

# === Hashing Function ===
def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

# === Generate and Save Hashes ===
def generate_hashes(directory):
    hashes = {}
    for root, _, files in os.walk(directory):
        for fname in files:
            fpath = os.path.join(root, fname)
            file_hash = calculate_hash(fpath)
            if file_hash:
                hashes[fpath] = file_hash
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)
    messagebox.showinfo("Success", f"Hashes stored in {HASH_FILE}")

# === Check Integrity and Log ===
def check_integrity():
    if not os.path.exists(HASH_FILE):
        messagebox.showerror("Error", f"No hash file found. Please generate hashes first.")
        return

    with open(HASH_FILE, "r") as f:
        old_hashes = json.load(f)

    log_entries = [f"\n=== File Check on {datetime.now()} ===\n"]
    for path, old_hash in old_hashes.items():
        current_hash = calculate_hash(path)
        if not current_hash:
            result = f"[!] File missing: {path}"
        elif current_hash != old_hash:
            result = f"[!] File changed: {path}"
        else:
            result = f"[OK] File intact: {path}"
        log_entries.append(result)

    # Save to log file
    with open(LOG_FILE, "a") as log:
        log.write("\n".join(log_entries) + "\n")

    messagebox.showinfo("Check Complete", f"Integrity check complete. Log saved in {LOG_FILE}")

# === GUI Setup ===
def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

def run_generate():
    path = folder_path.get()
    if os.path.isdir(path):
        generate_hashes(path)
    else:
        messagebox.showerror("Error", "Invalid directory selected.")

# GUI layout
root = tk.Tk()
root.title("File Integrity Checker")
root.geometry("400x250")
root.resizable(False, False)

folder_path = tk.StringVar()

tk.Label(root, text="Select Directory:", font=("Arial", 12)).pack(pady=10)
tk.Entry(root, textvariable=folder_path, width=40).pack()
tk.Button(root, text="Browse", command=browse_folder).pack(pady=5)
tk.Button(root, text="Generate Hashes", command=run_generate, bg="lightblue").pack(pady=10)
tk.Button(root, text="Check File Integrity", command=check_integrity, bg="lightgreen").pack(pady=5)

root.mainloop()
