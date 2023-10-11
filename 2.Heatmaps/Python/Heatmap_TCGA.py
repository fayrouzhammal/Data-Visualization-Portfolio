import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse
import numpy as np

def generate_heatmap(input_file, output_file):
    # Load the dataset
    data = pd.read_csv(input_file, sep='\t', comment='#')
    # Filter out unnecessary rows
    data = data[data['gene_name'].notna()]
    
    # Set gene_name as index
    data.set_index('gene_name', inplace=True)
    
    #Create column with log of fpkm
    data['log_fpkm_unstranded'] = np.log2(data['fpkm_unstranded'] + 1)
    data['log_fpkm_uq_unstranded'] = np.log2(data['fpkm_uq_unstranded'] + 1)
    data['log_tpm_unstranded'] = np.log2(data['tpm_unstranded'] + 1)
    

    # Select columns for heatmap
    heatmap_data = data[['log_fpkm_unstranded','log_fpkm_uq_unstranded','log_tpm_unstranded']]
    
    # Plotting the heatmap
    plt.figure(figsize=(10, 10))
    sns.heatmap(heatmap_data, cmap='coolwarm')
    plt.title("Gene Expression Heatmap")
    
    # Save the plot
    plt.savefig(output_file)
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Generate heatmap from TCGA data.')
    parser.add_argument('-i', '--input', required=True, help='Path to the input TCGA file.')
    parser.add_argument('-o', '--output', required=True, help='Path where you want to save the heatmap.')

    args = parser.parse_args()

    generate_heatmap(args.input, args.output)

if __name__ == "__main__":
    main()
