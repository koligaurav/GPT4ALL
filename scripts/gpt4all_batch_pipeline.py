import pandas as pd
from gpt4all import GPT4All
from tqdm import tqdm
import os
import time
import logging

# --- CONFIGURATION ---
MODEL_PATH = 'E:/project/models_gpt4all/mistral-7b-openorca.Q4_0.gguf'
INPUT_FILE = 'E:/project/data/your_jobs.csv'
OUTPUT_FILE = 'E:/project/data/final_gpt4all_output.csv'
ERROR_LOG_FILE = 'E:/project/data/error_log.txt'
SAMPLE_SIZE = None  # Set to 10 for quick test runs, or None for full dataset
DELAY_BETWEEN_CALLS = 0  # Seconds between requests; set to 0 for max speed

# --- SETUP LOGGING ---
logging.basicConfig(filename=ERROR_LOG_FILE, level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def gpt4all_process(gpt, title, description):
    prompt = f"""
    Job Title: {title}
    Job Description: {description}

    Predict:
    1. The most likely job family (broad role category).
    2. The most accurate standard job title.
    3. A comma-separated list of key technical skills.

    Respond in this format:
    Job Family: [job family]
    Standard Job Title: [standard job title]
    Skills: [comma-separated skills list]
    """
    response = gpt.generate(prompt, max_tokens=300)
    return response.strip()

def main():
    # --- PREPARE OUTPUT FOLDER ---
    output_dir = os.path.dirname(OUTPUT_FILE)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"✅ Created output directory: {output_dir}")

    # --- LOAD DATASET ---
    df = pd.read_csv(INPUT_FILE, low_memory=False)
    print(f"✅ Loaded {len(df)} records from {INPUT_FILE}")

    if SAMPLE_SIZE:
        df = df.head(SAMPLE_SIZE)
        print(f"⚠ Running in SAMPLE MODE on first {SAMPLE_SIZE} records.")

    # --- INITIALIZE GPT4All (LOCAL GGUF MODEL) ---
    gpt = GPT4All(MODEL_PATH)

    results = []
    error_count = 0

    with gpt:
        for idx, row in tqdm(df.iterrows(), total=len(df), desc="Processing jobs"):
            try:
                result = gpt4all_process(gpt, row['title'], row['description'])
                results.append(result)
                if DELAY_BETWEEN_CALLS > 0:
                    time.sleep(DELAY_BETWEEN_CALLS)
            except Exception as e:
                error_msg = f"❌ Error on row {idx}: {e}"
                print(error_msg)
                logging.error(error_msg)
                results.append("ERROR")
                error_count += 1

    # --- ATTACH RESULTS + SAVE ---
    df['gpt4all_output'] = results
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Saved enriched output to {OUTPUT_FILE}")
    print(f"⚠ Completed with {error_count} errors out of {len(df)} records.")
    if error_count > 0:
        print(f"⚠ Check error details in log file: {ERROR_LOG_FILE}")

if __name__ == "__main__":
    main()
