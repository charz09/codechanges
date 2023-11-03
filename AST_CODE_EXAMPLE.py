import ast
import ipywidgets as widgets
from IPython.display import display, clear_output
import matplotlib.pyplot as plt
import numpy as np
import math
from collections import Counter

# Set the threshold for plagiarism detection
PLAGIARISM_THRESHOLD = 0.25  # 25%

def preprocess_code(code):
    code = code.replace('\n', ' ')
    code = ' '.join(code.split())
    return code

def calculate_cosine_similarity(code1, code2):
    code1 = preprocess_code(code1)
    code2 = preprocess_code(code2)

    word_freq1 = Counter(code1.split())
    word_freq2 = Counter(code2.split())

    words = list(set(list(word_freq1.keys()) + list(word_freq2.keys())))

    dot_product = sum(word_freq1.get(word, 0) * word_freq2.get(word, 0) for word in words)

    magnitude1 = math.sqrt(sum(word_freq1.get(word, 0)**2 for word in words))
    magnitude2 = math.sqrt(sum(word_freq2.get(word, 0)**2 for word in words))

    # Check for division by zero
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0  # Return zero similarity if either magnitude is zero
    else:
        similarity = dot_product / (magnitude1 * magnitude2) * 100
        return similarity

def classify_plagiarism(similarity):
    if similarity >= PLAGIARISM_THRESHOLD:
        return "Plagiarism"
    else:
        return "Not Plagiarism"

def handle_upload_code1(change):
    uploaded_file = change['new']
    code = uploaded_file[0]['content']
    if isinstance(code, memoryview):
        code = bytes(code).decode('utf-8')
    global code1
    code1 = code

def handle_upload_code2(change):
    uploaded_file = change['new']
    code = uploaded_file[0]['content']
    if isinstance(code, memoryview):
        code = bytes(code).decode('utf-8')
    global code2
    code2 = code

def analyze_code(_):
    global code1, code2
    clear_output()
    similarity = calculate_cosine_similarity(code1, code2)
    
    # Display the result, classification, and the graph
    print("Cosine Similarity:", similarity)
    classification = classify_plagiarism(similarity)
    print("Classification:", classification)

    # Create a bar chart to visualize the similarity and other information
    labels = ['Cosine Similarity', 'Number of Lines in the Code']
    values = [similarity, max(code1.count('\n'), code2.count('\n'))]
    colors = ['blue', 'green']
    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots()
    ax.bar(x, values, width, label='Code Information', color=colors)
    ax.set_ylabel('Value')
    ax.set_title('Analysis of Code Files')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    fig.tight_layout()
    plt.show()

# Create file upload widgets for code
code_uploader1 = widgets.FileUpload()
code_uploader2 = widgets.FileUpload()
analyze_button = widgets.Button(description="Analyze Code")

# Register the file upload widgets' event handlers
code_uploader1.observe(handle_upload_code1, names='value')
code_uploader2.observe(handle_upload_code2, names='value')

# Register the button's click event handler
analyze_button.on_click(analyze_code)

# Display the file upload widgets and the analyze button
print("Please upload the first Python code file:")
display(code_uploader1)
print("Please upload the second Python code file:")
display(code_uploader2)
print("Click the 'Analyze Code' button to analyze the code:")
display(analyze_button)
