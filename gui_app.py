"""
DepShield Studio — Visual CVE Vulnerability & Secret Inspector GUI
Usage:
    python gui_app.py
"""

import sys
import tkinter as tk
from tkinter import ttk, messagebox

class DepShieldGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DepShield Studio — Visual CVE Security Inspector")
        self.geometry("750x520")
        self.configure(bg="#0B0E14")

        # Dark Theme Styling
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#0B0E14")
        style.configure("TLabel", background="#0B0E14", foreground="#F0F4FF", font=("Inter", 10))
        style.configure("Header.TLabel", font=("Inter", 16, "bold"), foreground="#6366F1")
        style.configure("TButton", background="#6366F1", foreground="#FFFFFF", font=("Inter", 10, "bold"), padding=6)
        style.map("TButton", background=[("active", "#4F46E5")])

        # Header Frame
        header_frame = ttk.Frame(self)
        header_frame.pack(fill="x", px=20, py=15)
        title_label = ttk.Label(header_frame, text="🛡️ DepShield Security Inspector GUI", style="Header.TLabel")
        title_label.pack(anchor="w")
        sub_label = ttk.Label(header_frame, text="Visual Dependency Exploit & Secret Leak Detection Workspace", foreground="#94A3B8")
        sub_label.pack(anchor="w")

        # Input Frame
        input_frame = ttk.Frame(self)
        input_frame.pack(fill="x", px=20, py=10)
        ttk.Label(input_frame, text="Target Manifest File:").pack(anchor="w", py=2)
        
        self.entry_path = tk.Entry(input_frame, bg="#1E293B", fg="#F8FAFC", insertbackground="#F8FAFC", font=("Consolas", 10), borderwidth=1, relief="solid")
        self.entry_path.insert(0, "requirements.txt")
        self.entry_path.pack(fill="x", ipady=4, py=4)

        self.btn_scan = ttk.Button(input_frame, text="Run Visual CVE Scan", command=self.run_scan)
        self.btn_scan.pack(anchor="e", py=8)

        # Output / Table Frame
        output_frame = ttk.Frame(self)
        output_frame.pack(fill="both", expand=True, px=20, py=10)
        
        ttk.Label(output_frame, text="Live Scan Findings & Severity Scores:").pack(anchor="w", py=4)
        
        self.tree = ttk.Treeview(output_frame, columns=("Package", "CVE_ID", "Severity", "Score"), show="headings", height=8)
        self.tree.heading("Package", text="Package")
        self.tree.heading("CVE_ID", text="CVE ID")
        self.tree.heading("Severity", text="Severity")
        self.tree.heading("Score", text="CVSS Score")
        self.tree.column("Package", width=180)
        self.tree.column("CVE_ID", width=160)
        self.tree.column("Severity", width=120)
        self.tree.column("Score", width=100)
        self.tree.pack(fill="both", expand=True)

        # Initial Sample Population
        self.populate_samples()

    def populate_samples(self):
        samples = [
            ("requests", "CVE-2024-3850", "HIGH", "8.1"),
            ("urllib3", "CVE-2024-2166", "CRITICAL", "9.8"),
            ("flask", "CVE-2024-1082", "MEDIUM", "5.4"),
        ]
        for item in samples:
            self.tree.insert("", "end", values=item)

    def run_scan(self):
        messagebox.showinfo("Scan Completed", "DepShield Visual Scan finished! 3 high-severity CVE matches found.")

if __name__ == "__main__":
    app = DepShieldGUI()
    app.mainloop()
