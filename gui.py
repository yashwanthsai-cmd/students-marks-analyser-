import tkinter as tk
from tkinter import filedialog, messagebox
import studentmarksanalyser as analyzer


def load_and_analyze():
    filepath = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV Files", "*.csv")]
    )
    
    if not filepath:
        return
    
    try:
        result = analyzer.run_analysis(filepath)
        messagebox.showinfo("Analysis Complete", result)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def create_gui():
    window = tk.Tk()
    window.title("Student Marks Analyzer")
    window.geometry("400x200")

    label = tk.Label(window, text="Student Marks Analyzer", font=("Arial", 16))
    label.pack(pady=20)

    load_button = tk.Button(window, text="Load CSV File & Analyze", command=load_and_analyze, width=25, height=2)
    load_button.pack()

    window.mainloop()


if __name__ == "__main__":
    create_gui()
