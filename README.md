🧠 Darvin's Mind - PDF Q&A Assistant
Darvin's Mind is a sleek desktop application built using CustomTkinter that lets you upload a PDF and ask questions about its contents. It uses Hugging Face's transformer models for local question-answering and can fall back to Google's Gemini API for more open-ended queries.

🚀 Features
📄 PDF Upload – Easily upload and parse any PDF document.

🤖 Local Q&A – Uses distilbert-base-uncased-distilled-squad to answer questions from the document.

🌐 Gemini AI Integration – When no PDF is loaded, fallback to conversational AI via Google's Gemini (if API key is configured).

🎨 Modern UI – Built with CustomTkinter for a clean, dark-themed interface.

💬 Typing Animation – Animated output gives a more interactive feel.

📦 Dependencies
Install the required packages with:

bash
Copy
Edit
pip install -r requirements.txt
Required libraries:

customtkinter

PyPDF2

transformers

google-generativeai

python-dotenv

tkinter (usually comes with Python)

🔐 Environment Variables
Create a .env file in the root directory with your API keys:

ini
Copy
Edit
HUGGINGFACE_API_KEY=your_huggingface_key_here
DEEPSEEK_MODEL=your_deepseek_model_if_needed
GEMINI_API_KEY=your_google_gemini_api_key
If you don’t want to use Gemini, you can leave GEMINI_API_KEY empty.

💻 How to Use
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/darvins-mind.git
cd darvins-mind
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
python main.py
Upload a PDF and start asking questions, or chat with Gemini without a document.

📸 Screenshots
Add screenshots here for better visual reference. You can use:

scss
Copy
Edit
![Screenshot](assets/screenshot.png)
🧠 Models Used
DistilBERT QA: distilbert-base-uncased-distilled-squad

Gemini: Google's conversational LLM API via google-generativeai

🛠 To-Do / Improvements
 Add support for multi-document handling

 Summarization feature

 Model selection from GUI

 Export Q&A history to text/markdown

📃 License
MIT License. Feel free to fork and adapt for your use.

👤 Author
Darvin's Mind was built by Ayush Kumar Mishra – inspired by the desire to make document reading smarter and interactive.

