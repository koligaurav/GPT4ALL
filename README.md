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
