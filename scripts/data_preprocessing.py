import pandas as pd

def preprocess_data(input_file, output_file):
    # Load the data
    data = pd.read_csv(input_file)
    
    # Perform quality control and normalization
    # (Assume some preprocessing steps here)
    
    # Save the preprocessed data
    data.to_csv(output_file, index=False)

if __name__ == "__main__":
    preprocess_data("raw_data.csv", "preprocessed_data.csv")
