# GPT4All Batch Processing Script

This project processes job data using the **GPT4All** library with a local **GGUF model** (TinyLlama or Mistral-7B). 
The script processes job titles and descriptions to predict job families, standard job titles, and key technical skills.
The predictions are saved in a CSV file.

## 🚀 **Overview**

### **What are we using?**
- **Python 3.8+**
- **GPT4All**: A local language model to process job descriptions and titles.
- **TinyLlama or Mistral-7B Model**: We use either a small or larger local model for predictions.
- **pandas**: To handle data processing and storage.
- **tqdm**: For progress bar visualization during the processing.
- **logging**: For error logging.

### **What does the script do?**
The script reads a CSV file containing job titles and descriptions, then predicts:
1. **Job Family**: The broad category of the job.
2. **Standard Job Title**: The standardized job title for that role.
3. **Skills**: A list of key technical skills required for the role.

These predictions are saved to a new CSV file, which you can use for further analysis.

---

## 📦 **Installation**
```bash
pip install -r requirements.txt

```

### 1. **System Requirements**
- **RAM**: Minimum 8GB (Recommended 16GB or more for larger models like Mistral-7B)
- **Disk Space**: At least 5GB free space for model storage

### 2. **Software Requirements**
- **Python 3.8 or higher**
- **Dependencies**: Listed in `requirements.txt`
  - **pandas** for data manipulation
  - **tqdm** for progress bars
  - **gpt4all** for interacting with local LLM models

### 3. **Install Dependencies**

1. **Clone the Repository**
   Clone the repository to your local machine using Git:
   ```bash
   git clone https://github.com/your-repo-url.git

    ```
2.**Navigate to Project Directory**
   Go to the project directory:
   ```bash
   cd your-repo
   ```
3.**Create and Activate Virtual Environment**
   For Windows:
   ```bash
   python -m venv venv
.\venv\Scripts\activate
   ```
For Linux/macOS::
   ```bash
 python3 -m venv venv
source venv/bin/activate
   ```
4.**Install Dependencies**
   Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```


### **Model Setup**
1. **Download the Model**
- **Mistral-7B GGUF Model (Recommended for systems with >16GB RAM):
```bash
https://huggingface.co/Meta-Llama/Mistral-7B-GGUF
```
2. ** Place the Model**
- After downloading, place the .gguf model file in the models_gpt4all folder:
```bash
E:/project/models_gpt4all/mistral-7b-openorca.Q4_0.gguf  # or TinyLlama-1.1b-chat-v1.0.Q4_0.gguf
```
3. ** Prepare Your Dataset**
- 1.Your Jobs CSV: Prepare your input dataset (your_jobs.csv). It should have columns like:
- id, title, description, job_family, seniority, etc.
- 2.Place the CSV in the data/ folder:
```bash
  E:/project/data/your_jobs.csv
```



  
