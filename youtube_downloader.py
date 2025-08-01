import tkinter as tk
from tkinter import messagebox
import subprocess

def download_video():
    url = entry.get()
    if not url:
        messagebox.showwarning("คำเตือน", "กรุณาใส่ลิงก์วิดีโอ YouTube")
        return
    try:
        subprocess.run(['yt-dlp', url], check=True)
        messagebox.showinfo("สำเร็จ", "ดาวน์โหลดวิดีโอสำเร็จแล้ว")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("ข้อผิดพลาด", f"เกิดข้อผิดพลาดในการดาวน์โหลด\n{e}")

app = tk.Tk()
app.title("YouTube Video Downloader")
app.geometry("400x200")
app.config(bg="#f0f0f0")

tk.Label(app, text="ลิงก์วิดีโอ YouTube", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=10)
entry = tk.Entry(app, width=45, font=("Helvetica", 12))
entry.pack()

tk.Button(app, text="ดาวน์โหลดวิดีโอ", command=download_video,
          bg="#007bff", fg="white", font=("Helvetica", 12)).pack(pady=20)

app.mainloop()
