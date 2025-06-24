# 🤖 Gesture Math Solver with Voice Output

A real-time **gesture-controlled calculator** with **speech output**, built using Python, OpenCV, and MediaPipe.  
Use your hands to input numbers and operations, and the system speaks the result out loud. No mouse, no keyboard — just gestures!

---

## 💡 Features

- ✋ Real-time hand gesture recognition
- ➕ Gesture-controlled math expression building
- 🗣️ Voice feedback using `pyttsx3`
- 🧠 Modular architecture (separate files for recognition, logic, UI, and speech)
- 🎯 Lightweight, fast, and offline

---

## 🛠 Tech Stack

- Python 3.10+
- OpenCV
- MediaPipe
- NumPy
- pyttsx3 (text-to-speech)

---

## 📂 Project Structure

gesture_math_solver/
├── main.py # App entry point
├── recognizer.py # Hand detection & gesture mapping
├── evaluator.py # Expression evaluation logic
├── overlay.py # UI text overlays
├── speaker.py # Voice output system
├── requirements.txt
└── README.md

---

## 🎮 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/your-username/gesture-math-solver.git
cd gesture-math-solver

# 2. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python main.py
🧠 Example Gestures
Gesture	Action
✌️ + 🖐️	Add (+)
✌️ + 🤟	Subtract (-)
✌️ + ✋	Multiply (*)
✌️ + 👍	Divide (/)
👊 + 👊	Evaluate (=)
🖐️ + 🖐️	Clear screen
🏗 Future Ideas
Streamlit-based web version

Voice command input (e.g., “clear” or “say result”)

Gesture training mode

Accessibility features for visually impaired users

📜 License
MIT License



