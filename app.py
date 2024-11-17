import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = ""

# Function to generate a response using OpenAI's new API
def generate_response(prompt):
    try:
        # Use the correct method for the latest OpenAI API (ChatCompletion)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or use "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("Prompt Engineering with OpenAI")
st.sidebar.header("Instructions")
st.sidebar.text("""
- Enter a prompt in the input field below.
- Click 'Generate' to see how OpenAI responds.
- Modify the prompt to experiment with different prompts or techniques.
""")

# User input for prompt
user_prompt = st.text_input("Enter a prompt:", "Write a short story about a dragon.")

# Button to generate the response
if st.button("Generate"):
    with st.spinner("Generating response..."):
        # Generate the response using OpenAI API
        result = generate_response(user_prompt)
        st.write(result)

# Add a simple explanation about prompt engineering techniques
st.subheader("Prompt Engineering Techniques")
st.write("""
1. **Role-playing and Persona Assignment**: Specify a persona for the model to make the responses more focused. For example, "Act as a professional scientist."
   
2. **Chain-of-Thought Prompting**: Ask the model to think step by step to help with logical or reasoning tasks. For example, "Explain how to solve this math problem step by step."

3. **Few-shot and Zero-shot Prompting**: Provide examples (few-shot) or simply describe the task (zero-shot) for the model. E.g., "Translate this sentence into French."

4. **Iterative Refinement**: Use a feedback loop to refine the response. For example, ask the model to improve or rephrase its answer in different ways.
""")
