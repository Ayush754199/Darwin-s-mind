import customtkinter as ctk
from tkinter import filedialog
import PyPDF2
import threading
import time
import os
from dotenv import load_dotenv
from transformers import pipeline
import google.generativeai as genai

# Load .env
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini Flash setup
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
    gemini_chat = gemini_model.start_chat()
else:
    gemini_chat = None

# App appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Darvin's Mind - PDF Q&A")
app.geometry("750x600")

# Load QA pipeline
pdf_text = ""
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

# Upload PDF
def load_pdf():
    global pdf_text
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        status_label.configure(text="Extracting PDF text...", text_color="orange")
        app.update()
        pdf_text = extract_text_from_pdf(file_path)
        status_label.configure(text="✅ PDF loaded successfully!", text_color="lightgreen")

# Typing animation
def type_text(text):
    output_box.delete("0.0", "end")
    for char in text:
        output_box.insert("end", char)
        output_box.see("end")
        app.update()
        time.sleep(0.02)

# Answer logic (threaded)
def answer_question_thread():
    question = question_entry.get().strip()

    if not question:
        type_text("❌ Please enter a question.")
        return

    try:
        if pdf_text:
            result = qa_pipeline(question=question, context=pdf_text[:4000])
            answer = result["answer"]
            type_text(f"✅ Answer:\n{answer}")
        else:
            if not gemini_chat:
                type_text("⚠ Gemini API Key not configured properly.")
                return
            response = gemini_chat.send_message(question)
            type_text(f"💡 Darvin:\n{response.text}")
    except Exception as e:
        type_text(f"⚠ Error: {str(e)}")

# Thread wrapper
def answer_question():
    threading.Thread(target=answer_question_thread).start()

# UI layout
title_label = ctk.CTkLabel(app, text="🧠 Darvin's Mind", font=ctk.CTkFont(size=24, weight="bold"))
title_label.pack(pady=20)

upload_button = ctk.CTkButton(app, text="📄 Upload PDF", command=load_pdf)
upload_button.pack(pady=10)

status_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=14))
status_label.pack(pady=5)

question_entry = ctk.CTkEntry(app, width=500, placeholder_text="💬 Ask a question about the PDF...")
question_entry.pack(pady=20)

submit_button = ctk.CTkButton(app, text="🔍 Get Answer", command=answer_question)
submit_button.pack(pady=10)

output_box = ctk.CTkTextbox(app, width=650, height=250, fg_color="#1e1e1e", text_color="white", font=("Consolas", 13), wrap="word")
output_box.pack(pady=20)

app.mainloop()
