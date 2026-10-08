"""
Resume Analyzer - Main Application
Topic #37: Resume Analyzer
Concepts: Strings, Regex, File Handling

Run:
    python main.py
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from resume_parser import extract_text_from_file
from analyzer import analyze_resume


class ResumeAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume Analyzer")
        self.root.geometry("900x650")
        self.root.minsize(800, 600)

        self.file_path = None

        title = tk.Label(
            root,
            text="Resume Analyzer",
            font=("Segoe UI", 24, "bold")
        )
        title.pack(pady=(20, 5))

        subtitle = tk.Label(
            root,
            text="Analyze resume information using Python, Strings, Regex and File Handling",
            font=("Segoe UI", 10)
        )
        subtitle.pack(pady=(0, 15))

        controls = tk.Frame(root)
        controls.pack(pady=10)

        tk.Button(
            controls,
            text="Upload Resume",
            command=self.upload_resume,
            width=18,
            height=2
        ).grid(row=0, column=0, padx=8)

        tk.Button(
            controls,
            text="Analyze Resume",
            command=self.run_analysis,
            width=18,
            height=2
        ).grid(row=0, column=1, padx=8)

        tk.Button(
            controls,
            text="Clear",
            command=self.clear,
            width=18,
            height=2
        ).grid(row=0, column=2, padx=8)

        self.file_label = tk.Label(
            root,
            text="No resume selected",
            font=("Segoe UI", 10)
        )
        self.file_label.pack(pady=5)

        self.output = tk.Text(
            root,
            wrap="word",
            font=("Consolas", 11),
            padx=15,
            pady=15
        )
        self.output.pack(fill="both", expand=True, padx=25, pady=15)

    def upload_resume(self):
        path = filedialog.askopenfilename(
            title="Select Resume",
            filetypes=[
                ("Resume files", "*.pdf *.txt"),
                ("PDF files", "*.pdf"),
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )

        if path:
            self.file_path = path
            self.file_label.config(text=f"Selected: {path}")
            self.output.delete("1.0", tk.END)
            self.output.insert(
                tk.END,
                "Resume selected successfully.\n\n"
                "Click 'Analyze Resume' to begin."
            )

    def run_analysis(self):
        if not self.file_path:
            messagebox.showwarning(
                "No Resume",
                "Please upload a PDF or TXT resume first."
            )
            return

        try:
            text = extract_text_from_file(self.file_path)

            if not text.strip():
                raise ValueError("No readable text was found in the resume.")

            result = analyze_resume(text)

            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, result)

        except Exception as exc:
            messagebox.showerror("Analysis Error", str(exc))

    def clear(self):
        self.file_path = None
        self.file_label.config(text="No resume selected")
        self.output.delete("1.0", tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeAnalyzerApp(root)
    root.mainloop()
