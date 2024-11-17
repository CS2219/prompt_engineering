# prompt_engineering
**Interactive Prompt Testing: Enter custom prompts and see real-time responses from OpenAI's GPT models.**
Prompt Engineering Techniques: Learn and apply techniques like:
Role-playing and Persona Assignment
Chain-of-Thought Prompting
Few-shot and Zero-shot Learning
Iterative Refinement
Streamlit-Based UI: A simple, user-friendly interface to interact with the API.
Educational Content: Includes explanations and examples of effective prompt engineering.

**Installation**
Follow these steps to get the app up and running:

**1. Clone the Repository**
```python
git clone https://github.com/your-username/prompt-engineering.git
cd prompt-engineering

```
**2. Install Dependencies**
Make sure you have Python 3.7 or later. Install the required libraries:
```python
pip install -r requirements.txt

```
**3. Set Up OpenAI API Key**
Create a .env file in the root directory and add your OpenAI API key:
```python
OPENAI_API_KEY=your-openai-api-key-here
```
Alternatively, you can set the environment variable directly in your terminal:
```python
export OPENAI_API_KEY=your-openai-api-key-here
```
**4. Run the App**
Run the Streamlit app locally:
```python
streamlit run app.py
```
The app will open in your default browser at http://localhost:8501.

**Usage**
Enter a prompt in the text input field (e.g., "Write a story about a mischievous dragon.").
Click the "Generate" button to get a response from the OpenAI API.
Experiment with different prompt engineering techniques explained in the app.

**Resources**
Here are some useful resources to learn more about OpenAI’s API and prompt engineering:

📖 OpenAI API Documentation
💡 OpenAI Cookbook
📚 Introduction to Prompt Engineering
🎥 YouTube: Practical Prompt Engineering Techniques
🛠 Streamlit Documentation