import ast
import difflib
from difflib import HtmlDiff
from hmac import compare_digest
import uuid
from flask import Flask, g, render_template, request, redirect, url_for, flash, send_file
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import sqlite3
import os
from difflib import ndiff
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from diff_match_patch import diff_match_patch
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')
import time



app = Flask(__name__)
app.config['SECRET_KEY'] = 'Ch@rles20234'
app.config['DATABASE'] = 'database.db'


# Database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = sqlite3.connect('database.db')
        db.row_factory = sqlite3.Row
        g._database = db
    return db

@app.teardown_appcontext
def close_db(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# Main page
@app.route('/')
def index():
    return render_template('index.html')

# Set the upload folder for uploaded files
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)



@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if f:
            filename = secure_filename(f.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            f.save(file_path)

            conn = get_db()
            cursor = conn.cursor()
            
            # Create the 'upload_files' table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS upload_files (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filename TEXT
                )
            ''')

            # Insert the uploaded filename into the table
            cursor.execute('INSERT INTO upload_files (filename) VALUES (?)', (filename,))
            conn.commit()
            conn.close()

            flash('File uploaded successfully', 'success')

        else:
            flash('No selected file', 'danger')

        return redirect(url_for('upload_file'))
    
    return render_template('upload.html')




# Projects page
@app.route('/projects')
def projects():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects')
    projects = cursor.fetchall()
    conn.close()

    return render_template('projects.html', projects=projects)

# Plagiarism checker page
@app.route('/plagiarism', methods=['GET', 'POST'])
def plagiarism():
    # Record the start time
    start_time = time.time()

    plagiarism_results = {}
    pdf_generated = False

    highlighted_content1 = ""
    highlighted_content2 = ""
    response_time_formatted = "" 
    

    if request.method == 'POST':
        # Handle plagiarism check
        file1 = request.files['file1']
        file2 = request.files['file2']
        threshold = 25 # Set the threshold as needed

        # Perform plagiarism checking and get results
        plagiarism_results = perform_plagiarism_check(file1, file2, threshold)

        # Calculate TF-IDF similarity
        tfidf_similarity = calculate_tfidf_similarity(file1.read().decode('utf-8'), file2.read().decode('utf-8'))
        


        # Read the content of the uploaded files
        content1 = file1.read().decode('utf-8')
        content2 = file2.read().decode('utf-8')


        # Generate highlighted content using difflib.ndiff
        highlighted_content1, highlighted_content2 = highlight_similarities(content1, content2)

        # Generate highlighted content using HtmlDiff
        d = HtmlDiff()
        highlighted_content1 = d.make_file(content1.splitlines(), content2.splitlines(), context=True, numlines=5)
        highlighted_content2 = d.make_file(content2.splitlines(), content1.splitlines(), context=True, numlines=5)



        # Handle PDF generation
        if 'generate_pdf' in request.form:
            pdf_filename = generate_pdf(content1, content2)
            pdf_generated = True

        # Calculate the response time
        end_time = time.time()
        response_time = end_time - start_time
        response_time_formatted = "{:.4f} seconds".format(response_time)

        # Add the response_time to the plagiarism_results dictionary
        plagiarism_results['response_time'] = response_time_formatted
        
        # Generate highlighted HTML representations
        highlighted_content1 = generate_highlighted_html(content1, content2)
        highlighted_content2 = generate_highlighted_html(content2, content1)

        return render_template('plagiarism.html', plagiarism_results=plagiarism_results, highlighted_content1=highlighted_content1, highlighted_content2=highlighted_content2, pdf_generated=pdf_generated, response_time=response_time_formatted, tfidf_similarity=tfidf_similarity)

    return render_template('plagiarism.html', plagiarism_results=plagiarism_results, highlighted_content1=highlighted_content1,highlighted_content2=highlighted_content2, pdf_generated=pdf_generated, response_time=response_time_formatted)



def calculate_tfidf_similarity(content1, content2):
    # Preprocess the content
    preprocessed_content1 = preprocess_text(content1)
    preprocessed_content2 = preprocess_text(content2)

    # Calculate TF-IDF values
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([preprocessed_content1, preprocessed_content2])
    tfidf_values1 = tfidf_matrix.toarray()[0]
    tfidf_values2 = tfidf_matrix.toarray()[1]

    # Calculate cosine similarity between TF-IDF vectors
    tfidf_similarity = cosine_similarity([tfidf_values1], [tfidf_values2])[0][0]

    return tfidf_similarity






# Function to highlight similarities between two strings
def highlight_similarities(content1, content2):
    dmp = diff_match_patch()
    diffs = dmp.diff_main(content1, content2)
    dmp.diff_cleanupSemantic(diffs)
    
    highlighted_content1 = []
    highlighted_content2 = []
    
    for diff in diffs:
        if diff[0] == 0:  # Equal parts
            highlighted_content1.append(diff[1])
            highlighted_content2.append(diff[1])
        elif diff[0] == -1:  # Deletions
            highlighted_content1.append('<span style="background-color: yellow;">' + diff[1] + '</span>')
        else:  # Insertions
            highlighted_content2.append('<span style="background-color: yellow;">' + diff[1] + '</span>')
    
    return ''.join(highlighted_content1), ''.join(highlighted_content2)




def generate_highlighted_html(content, other_content):
    dmp = diff_match_patch()
    diffs = dmp.diff_main(content, other_content)
    dmp.diff_cleanupSemantic(diffs)
    highlighted_diffs = []
    
    for op, text in diffs:
        if op == 0:  # Unchanged text
            highlighted_diffs.append(text)
        elif op == 1:  # Added text
            highlighted_diffs.append(f'<span style="background-color: yellow;">{text}</span>')
    
    highlighted_html = ''.join(highlighted_diffs)
    return highlighted_html







# Helper function to perform plagiarism check
def ast_similarity(code1, code2):
    tree1 = ast.parse(code1)
    tree2 = ast.parse(code2)
    
    # Compare ASTs and calculate similarity score
    similarity_score = ast_diff_similarity(tree1, tree2)
    
    return similarity_score

def ast_diff_similarity(node1, node2):
    if type(node1) == type(node2):
        if isinstance(node1, ast.AST):
            # Compare the type of AST node
            score = 100.0
            
            # Compare attributes based on the type of node
            if isinstance(node1, ast.Name):
                # Compare variable names
                if node1.id == node2.id:
                    score += 50.0
            elif isinstance(node1, ast.Call):
                # Compare function calls (name and arguments)
                if isinstance(node1.func, ast.Name) and isinstance(node2.func, ast.Name):
                    if node1.func.id == node2.func.id and len(node1.args) == len(node2.args):
                        score += 50.0
            # Add more comparisons for other types of nodes as needed
            
            # Recursively compare child nodes
            child_nodes1 = list(ast.iter_child_nodes(node1))
            child_nodes2 = list(ast.iter_child_nodes(node2))
            if child_nodes1 and child_nodes2:
                child_scores = [ast_diff_similarity(child1, child2) for child1, child2 in zip(child_nodes1, child_nodes2)]
                score += sum(child_scores) / len(child_nodes1)
            
            return score
        elif isinstance(node1, ast.expr):
            # Compare expressions (e.g., binary operations)
            if isinstance(node1, type(node2)):
                return 70.0
        elif isinstance(node1, ast.stmt):
            # Compare statements (e.g., assignments, loops)
            if isinstance(node1, type(node2)):
                return 80.0
        
    return 0.0

def preprocess_text(text):
    text = text.lower()
    words = word_tokenize(text)
    words = [word for word in words if word.isalnum()]
    words = [word for word in words if word not in stopwords.words('english')]


     # Ensure the preprocessed text is not empty
    if len(words) == 0:
        return "No meaningful content"  # Return some placeholder text
    
    return ' '.join(words)

def perform_plagiarism_check(file1, file2, threshold):
    # Read the content of the uploaded files
    content1 = file1.read().decode('utf-8')
    content2 = file2.read().decode('utf-8')


    # Preprocess the content
    preprocessed_content1 = preprocess_text(content1)
    preprocessed_content2 = preprocess_text(content2)

    # Calculate TF-IDF values
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([preprocessed_content1, preprocessed_content2])
    tfidf_values1 = tfidf_matrix.toarray()[0]
    tfidf_values2 = tfidf_matrix.toarray()[1]

    # Calculate cosine similarity between TF-IDF vectors
    tfidf_similarity = cosine_similarity([tfidf_values1], [tfidf_values2])[0][0] * 100
    tfidf_similarity = round(tfidf_similarity, 2)

    # Calculate AST-based similarity score
    similarity_score = difflib.SequenceMatcher(None, content1, content2).ratio() * 100
    similarity_score = round(similarity_score, 2)


    # Calculate cosine similarity score
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0] * 100
    cosine_sim = round(cosine_sim, 2)

    # # Determine comparison result based on the threshold
    if similarity_score >= threshold:
        result = "Plagiarized"
    else:
        result = "Not Plagiarized"

    # Determine comparison result based on the threshold
    if cosine_sim >= threshold:
        result = "Plagiarized"
    else:
        result = "Not Plagiarized"


    # Create a dictionary to hold the results
    highlighted_content1, highlighted_content2 = highlight_similarities(content1, content2)

    # Create a dictionary to hold the results
    plagiarism_results = {
        'similarity_score': similarity_score,
        'cosine_similarity': cosine_sim,
        'tfidf_similarity': tfidf_similarity,
        'matched_files': f"{file1.filename}, {file2.filename}",
        'comparison_result': result,
        'content1': content1,
        'content2': content2
    }

    return plagiarism_results





@app.route('/generate_pdf', methods=['POST'])
def generate_pdf(file1_content, file2_content):
    # Generate a unique filename for the PDF
    pdf_filename = f"plagiarism_result_{uuid.uuid4()}.pdf"

    # Initialize PDF document
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Convert file content to lines
    file1_lines = file1_content.splitlines()
    file2_lines = file2_content.splitlines()

    # Calculate differences using difflib.ndiff
    diff_lines = ndiff(file1_lines, file2_lines)

    # Set font size and line height for PDF
    font_size = 12
    line_height = 14

    # Set initial y-coordinate for rendering
    y = 750

    # Loop through the differences and render lines with highlights
    for line in diff_lines:
        if line.startswith('+ '):
            # Blue color for insertions
            c.setFillColorRGB(0, 0, 1)
            c.drawString(100, y, line[2:])
            c.setFillColorRGB(0, 0, 0)  # Reset color to black
        elif line.startswith('- '):
            # Red color for deletions
            c.setFillColorRGB(1, 0, 0)
            c.drawString(100, y, line[2:])
            c.setFillColorRGB(0, 0, 0)  # Reset color to black
        else:
            c.drawString(100, y, line[2:])
        y -= line_height

    # Save PDF document
    c.save()

    flash('PDF generated successfully!', 'success')

    return pdf_filename




@app.route('/download_pdf/<pdf_filename>')
def download_pdf(pdf_filename):
    return send_file(pdf_filename, as_attachment=True)



#Flask route to handle plagiarism check for a folder
@app.route('/plagiarism_folder', methods=['POST'])
def plagiarism_folder():
    folder1 = folder1 = request.files.getlist('folder1')   # Get the path of the first selected folder
    folder2 = request.files.getlist('folder2')  # Get the path of the second selected folder
    threshold = int(request.form['threshold'])

    # Get the file contents for each folder
    folder1_contents = read_files_in_folder(folder1)
    folder2_contents = read_files_in_folder(folder2)

    # Perform plagiarism checking and get results
    plagiarism_results = perform_plagiarism_check_folders(folder1, folder2, threshold)

    return render_template('plagiarism.html', plagiarism_results=plagiarism_results)

def perform_plagiarism_check_folders(folder1_contents, folder2_contents, threshold):
    # Your plagiarism checking logic for folders here
    # Compare the contents of files in the two folders and calculate the similarity score

    # Placeholder result for demonstration
    similarity_score = 25  # Replace this with your actual similarity calculation

    # Determine if the comparison result is "Plagiarized" or "Not Plagiarized" based on the threshold
    comparison_result = "Plagiarized" if similarity_score >= threshold else "Not Plagiarized"

    # Return the plagiarism results
    plagiarism_results = {
        'average_similarity_score': similarity_score,
        'matched_folders': "Folder 1, Folder 2",  # Replace with the actual folder names
        'comparison_result': comparison_result
    }

    return plagiarism_results



def read_files_in_folder(folder_path):
    file_contents = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                file_contents[filename] = content
    return file_contents


def read_folder(folder):
  files = []
  for filename in os.listdir(folder.filename):
    if filename.endswith(".txt"):
      file_path = os.path.join(folder.filename, filename)  
      files.append(read_file(file_path))  
  return files

def read_file(file_path):
  with open(file_path) as f:
    return f.read()






def perform_folder_plagiarism(folder1, folder2, threshold):
    # Read the content of files in folder1 and folder2
    files1 = read_files_in_folder(folder1)
    files2 = read_files_in_folder(folder2)

    # Calculate average AST-based similarity score
    similarity_scores = []
    for file1 in files1:
        for file2 in files2:
            similarity_score = difflib.SequenceMatcher(None, file1, file2).ratio() * 100
            similarity_scores.append(similarity_score)
    
    average_similarity_score = sum(similarity_scores) / len(similarity_scores)

    # Determine comparison result based on the threshold
    if average_similarity_score >= threshold:
        result = "Plagiarized"
    else:
        result = "Not Plagiarized"

    # Create a dictionary to hold the results
    plagiarism_results = {
        'average_similarity_score': average_similarity_score,
        'matched_folders': f"{folder1}, {folder2}",
        'comparison_result': result
    }

    return plagiarism_results

# Helper function to read the content of files in a folder
def read_files_in_folder(folder_contents):
    filenames = []
    for file in folder_contents:
        if file.filename:
            filenames.append(file.filename)
    return filenames


if __name__ == '__main__':
    app.run(debug=True)