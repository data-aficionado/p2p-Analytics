import pandas as pd
from gprofiler import GProfiler

def pathway_enrichment(input_file, output_file):
    # Load differentially expressed genes
    data = pd.read_csv(input_file)
    genes = data[data['p_adj'] < 0.05]['gene']
    
    # Perform pathway enrichment analysis
    gp = GProfiler(return_dataframe=True)
    results = gp.profile(organism='hsapiens', query=genes.tolist())
    
    # Save the results
    results.to_csv(output_file, index=False)

if __name__ == "__main__":
    pathway_enrichment("differential_expression_results.csv", "pathway_enrichment_results.csv")
