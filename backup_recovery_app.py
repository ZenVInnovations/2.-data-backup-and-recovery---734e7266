import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import zipfile
from datetime import datetime

# Log file path
log_file = "backup_log.txt"

# Log function
def log_action(action, src, dest):
    with open(log_file, "a") as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] {action} from {src} to {dest}\n")

# Backup function
def backup_data():
    path = filedialog.askopenfilename(title="Select File") or filedialog.askdirectory(title="Or Select Folder")
    if not path:
        return
    dest_dir = filedialog.askdirectory(title="Select Backup Destination")
    if not dest_dir:
        return

    try:
        base_name = os.path.basename(path.rstrip(os.sep))
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        zip_filename = f"{base_name}_backup_{timestamp}.zip"
        zip_path = os.path.join(dest_dir, zip_filename)

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            if os.path.isdir(path):
                for root, _, files in os.walk(path):
                    for file in files:
                        full_path = os.path.join(root, file)
                        rel_path = os.path.relpath(full_path, os.path.dirname(path))
                        zipf.write(full_path, arcname=rel_path)
            else:
                zipf.write(path, arcname=base_name)

        log_action("Backup", path, zip_path)
        messagebox.showinfo("Backup Successful", f"Backup created:\n{zip_path}")
    except Exception as e:
        messagebox.showerror("Backup Error", str(e))

# Recover function
def recover_data():
    zip_file = filedialog.askopenfilename(title="Select ZIP Backup File", filetypes=[("ZIP files", "*.zip")])
    if not zip_file:
        return
    dest = filedialog.askdirectory(title="Select Destination Folder")
    if not dest:
        return

    try:
        with zipfile.ZipFile(zip_file, 'r') as zipf:
            zipf.extractall(dest)
            files = zipf.namelist()

        log_action("Recovery", zip_file, dest)
        messagebox.showinfo("Recovery Successful", f"Recovered {len(files)} files to:\n{dest}")
    except Exception as e:
        messagebox.showerror("Recovery Error", str(e))

# View log function
def show_log():
    if os.path.exists(log_file):
        log_window = tk.Toplevel(root)
        log_window.title("Backup & Recovery Log")
        log_window.geometry("600x400")

        log_text = scrolledtext.ScrolledText(log_window, wrap=tk.WORD, font=("Courier", 10))
        with open(log_file, "r") as f:
            log_text.insert(tk.END, f.read())
        log_text.pack(fill=tk.BOTH, expand=True)
    else:
        messagebox.showinfo("Log Missing", "No backup log found yet.")

# GUI Setup
root = tk.Tk()
root.title("Advanced Data Backup & Recovery Tool")
root.geometry("500x350")
root.configure(bg="#eef2f3")

# GUI widgets
tk.Label(root, text="🗂️ Data Backup & Recovery Tool", font=("Arial", 16, "bold"), bg="#eef2f3").pack(pady=20)
tk.Button(root, text="📦 Backup File or Folder", command=backup_data, width=30, bg="#add8e6", font=("Arial", 11)).pack(pady=10)
tk.Button(root, text="♻️ Recover from ZIP", command=recover_data, width=30, bg="#90ee90", font=("Arial", 11)).pack(pady=10)
tk.Button(root, text="📜 View Log", command=show_log, width=30, bg="#d3d3d3", font=("Arial", 11)).pack(pady=10)

root.mainloop()
