import ipywidgets as widgets
from IPython.display import display, clear_output
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import ast

def remove_comments_and_spaces(code):
    # Parse the code to remove comments and spaces
    parsed_code = ast.parse(code)
    cleaned_code = ast.dump(parsed_code, annotate_fields=False)
    return cleaned_code

def calculate_num_lines(code):
    # Count the number of lines in the code
    return code.count('\n') + 1

def handle_upload_text1(change):
    uploaded_file = change['new']
    content = uploaded_file[0]['content']
    
    if isinstance(content, memoryview):
        content = content.tobytes().decode('utf-8')
    
    cleaned_code = remove_comments_and_spaces(content)
    
    global text1, num_lines1
    text1 = cleaned_code
    num_lines1 = calculate_num_lines(content)

def handle_upload_text2(change):
    uploaded_file = change['new']
    content = uploaded_file[0]['content']
    
    if isinstance(content, memoryview):
        content = content.tobytes().decode('utf-8')
    
    cleaned_code = remove_comments_and_spaces(content)
    
    global text2, num_lines2
    text2 = cleaned_code
    num_lines2 = calculate_num_lines(content)

def analyze_code(_):
    global text1, text2, num_lines1, num_lines2
    clear_output()
    
    # Calculate TF-IDF vectors for the texts
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    
    # Calculate the cosine similarity between the texts
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix) * 100
    
    similarity = cosine_sim[0][1] 
    
    # Determine if it's plagiarism or not based on the threshold
    PLAGIARISM_THRESHOLD = 0.25  # You can adjust this threshold as needed
    classification = "Plagiarism" if similarity >= PLAGIARISM_THRESHOLD else "Not Plagiarism"
    
    # Display the results
    print("Classification:", classification)
    print("Number of Lines in Code 1:", num_lines1)
    print("Number of Lines in Code 2:", num_lines2)
    print("TF-IDF Similarity:", similarity)
    
    # Create a bar chart to visualize the similarity
    labels = ['TF-IDF Similarity']
    values = [similarity]
    colors = ['blue' if classification == "Not Plagiarism" else 'red']
    
    plt.bar(labels, values, color=colors)
    plt.title('Plagiarism Detection')
    plt.ylim(0, 1)
    plt.show()

# Create file upload widgets for code
text_uploader1 = widgets.FileUpload()
text_uploader2 = widgets.FileUpload()
analyze_button = widgets.Button(description="Analyze Code")

# Register the file upload widgets' event handlers
text_uploader1.observe(handle_upload_text1, names='value')
text_uploader2.observe(handle_upload_text2, names='value')

# Register the button's click event handler
analyze_button.on_click(analyze_code)

# Display the file upload widgets and the analyze button
print("Please upload the first text file:")
display(text_uploader1)
print("Please upload the second text file:")
display(text_uploader2)
print("Click the 'Analyze Code' button to analyze the code:")
display(analyze_button)
