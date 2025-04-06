import tkinter as tk
from tkinter import filedialog, messagebox
from model import GeneticTraitPredictorModel


class GeneticTraitPredictorApp:
    def __init__(self):
        self.model = GeneticTraitPredictorModel()
        self.root = tk.Tk()
        self.root.title("Genetic Trait Predictor")
        self.root.geometry("600x400")

        self.label = tk.Label(self.root, text="Upload Family CSV File", font=("Arial", 14))
        self.label.pack(pady=10)

        self.upload_button = tk.Button(self.root, text="Upload CSV", command=self.upload_file)
        self.upload_button.pack(pady=10)

        self.result_text = tk.Text(self.root, width=70, height=20)
        self.result_text.pack(pady=10)

        self.save_button = tk.Button(self.root, text="Save Report", command=self.save_report)
        self.save_button.pack(pady=10)

        self.root.mainloop()

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            result = self.model.predict(file_path)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)

    def save_report(self):
        report = self.result_text.get(1.0, tk.END)
        if not report.strip():
            messagebox.showwarning("Warning", "No report to save!")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text file", "*.txt"), ("PDF file", "*.pdf")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(report)
            messagebox.showinfo("Success", "Report saved successfully!")
