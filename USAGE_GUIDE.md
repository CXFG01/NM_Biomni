# Biomni Usage Guide and Examples

## Quick Start

### 1. Installation

```bash
# Basic installation
pip install biomni --upgrade

# Or install from source
git clone https://github.com/snap-stanford/biomni.git
cd biomni
pip install -e .
```

### 2. Configure API Keys

Add to your `~/.bashrc` or `~/.zshrc`:

```bash
export ANTHROPIC_API_KEY="your_anthropic_api_key_here"
export OPENAI_API_KEY="your_openai_api_key_here"  # Optional
```

### 3. Basic Usage

```python
from biomni.agent import A1

# Initialize the agent
agent = A1(
    path='./data',                    # Data directory
    llm='claude-sonnet-4-20250514',   # LLM model
    use_tool_retriever=True,          # Enable tool retrieval
    timeout_seconds=600               # Task timeout
)

# Execute biomedical tasks
agent.go("Your biomedical research question here")
```

## Core Features

### 1. Natural Language Task Execution

Biomni can understand and execute complex biomedical tasks through natural language:

```python
# CRISPR Screen Design
agent.go("""
Plan a CRISPR screen to identify genes that regulate T cell exhaustion.
Generate 32 genes that maximize the perturbation effect.
Consider both positive and negative regulators.
""")

# Single-cell RNA-seq Analysis
agent.go("""
Perform scRNA-seq annotation on the dataset at /path/to/data.h5ad
and generate meaningful biological hypotheses about cell type differences.
""")

# Drug Discovery
agent.go("""
Predict ADMET properties for this compound: CC(C)CC1=CC=C(C=C1)C(C)C(=O)O
Include absorption, distribution, metabolism, excretion, and toxicity predictions.
""")

# Literature Analysis
agent.go("""
Find and analyze recent papers on CAR-T cell therapy resistance mechanisms.
Summarize key findings and identify potential therapeutic targets.
""")
```

### 2. Tool System

Biomni includes 200+ specialized tools across 18 biomedical domains:

```python
# Direct tool usage (advanced)
from biomni.tool.genomics import annotate_celltype_scRNA
from biomni.tool.pharmacology import predict_admet_properties
from biomni.tool.literature import search_pubmed

# Tools are automatically selected by the agent
# based on task requirements
```

### 3. Data Lake Access

Access to 74 biomedical datasets automatically:

```python
# Data is automatically downloaded and cached
# No manual data management required
agent.go("Analyze protein-protein interactions from the affinity capture dataset")
```

## Example Workflows

### 1. Genomics Analysis

```python
# Cell type annotation in single-cell data
agent.go("""
I have single-cell RNA-seq data from brain tissue.
Please:
1. Perform quality control and filtering
2. Normalize and scale the data
3. Perform clustering using Leiden algorithm
4. Annotate cell types using marker genes
5. Generate biological hypotheses about cell type functions
""")

# Variant analysis
agent.go("""
Analyze these genetic variants: rs1801133, rs1801131, rs2274976
Include:
- Functional annotations
- Disease associations
- Population frequencies
- Predicted effects on protein function
""")
```

### 2. Drug Discovery

```python
# ADMET prediction
agent.go("""
Predict ADMET properties for these drug candidates:
1. CC(C)CC1=CC=C(C=C1)C(C)C(=O)O
2. CC1=CC=C(C=C1)C(C)C(=O)O
3. CCC1=CC=C(C=C1)C(C)C(=O)O

Compare their drug-likeness and identify the best candidate.
""")

# Drug repurposing
agent.go("""
Find existing drugs that could be repurposed for treating Alzheimer's disease.
Focus on compounds with:
- Good brain penetration
- Favorable safety profiles
- Mechanisms targeting amyloid or tau pathways
""")
```

### 3. Cancer Biology

```python
# Mutation analysis
agent.go("""
Analyze TP53 mutations in cancer:
1. Identify most frequent mutations
2. Analyze functional consequences
3. Correlate with patient outcomes
4. Suggest therapeutic strategies
""")

# Pathway analysis
agent.go("""
Perform pathway enrichment analysis for these differentially expressed genes:
[Gene list here]
Focus on cancer-related pathways and identify potential therapeutic targets.
""")
```

### 4. Immunology

```python
# T cell analysis
agent.go("""
Analyze T cell exhaustion markers in this scRNA-seq dataset.
Identify:
- Exhausted T cell populations
- Key exhaustion markers
- Potential therapeutic targets
- Reversibility mechanisms
""")

# Immune profiling
agent.go("""
Profile the immune landscape of this tumor sample.
Include:
- Immune cell composition
- Activation states
- Immunosuppressive factors
- Therapeutic opportunities
""")
```

### 5. Systems Biology

```python
# Network analysis
agent.go("""
Build a protein-protein interaction network for Alzheimer's disease genes.
Identify:
- Hub proteins
- Functional modules
- Druggable targets
- Pathway crosstalk
""")

# Multi-omics integration
agent.go("""
Integrate transcriptomic and proteomic data from this cancer study.
Identify:
- Concordant changes
- Post-translational regulation
- Biomarker candidates
- Therapeutic targets
""")
```

## Advanced Usage

### 1. Custom Tool Development

```python
# Create a custom tool
def custom_analysis_tool(data_path: str, parameter: str) -> str:
    """
    Custom analysis tool description.
    
    Parameters:
    -----------
    data_path : str
        Path to the data file
    parameter : str
        Analysis parameter
        
    Returns:
    --------
    str
        Analysis results
    """
    # Your implementation here
    return "Analysis results"

# Register the tool (advanced usage)
# Tools are automatically discovered and registered
```

### 2. Batch Processing

```python
# Process multiple samples
samples = ["sample1.h5ad", "sample2.h5ad", "sample3.h5ad"]

for sample in samples:
    agent.go(f"""
    Analyze the single-cell data in {sample}:
    1. Perform quality control
    2. Annotate cell types
    3. Identify marker genes
    4. Generate summary report
    """)
```

### 3. Integration with Existing Pipelines

```python
# Use Biomni within existing analysis pipelines
def analyze_with_biomni(data_path, research_question):
    agent = A1(path='./data')
    
    # Formulate comprehensive analysis request
    analysis_request = f"""
    Analyze the data at {data_path} to answer: {research_question}
    
    Please provide:
    1. Data quality assessment
    2. Statistical analysis
    3. Biological interpretation
    4. Actionable recommendations
    """
    
    result = agent.go(analysis_request)
    return result

# Use in your workflow
result = analyze_with_biomni("my_data.csv", "What genes are associated with drug resistance?")
```

## Best Practices

### 1. Task Formulation

**Good**: Specific, structured requests
```python
agent.go("""
Perform differential expression analysis on RNA-seq data:
1. Compare treated vs control samples
2. Use DESeq2 normalization
3. Apply FDR correction (p < 0.05)
4. Perform pathway enrichment on significant genes
5. Generate visualization plots
""")
```

**Avoid**: Vague requests
```python
agent.go("Analyze my data")  # Too vague
```

### 2. Data Management

```python
# Organize data properly
data_structure = {
    "raw_data/": "Original datasets",
    "processed_data/": "Cleaned and processed data", 
    "results/": "Analysis outputs",
    "figures/": "Visualizations"
}

# Use absolute paths when possible
agent.go(f"Analyze the data at {os.path.abspath('data/sample.h5ad')}")
```

### 3. Error Handling

```python
try:
    result = agent.go("Complex analysis task")
    print("Analysis completed successfully")
except Exception as e:
    print(f"Analysis failed: {e}")
    # Retry with simplified request
    result = agent.go("Simplified analysis task")
```

### 4. Resource Management

```python
# For large datasets, consider timeout settings
agent = A1(
    path='./data',
    timeout_seconds=1800  # 30 minutes for large analyses
)

# Monitor resource usage
import psutil
print(f"Memory usage: {psutil.virtual_memory().percent}%")
```

## Troubleshooting

### Common Issues

1. **Module Not Found Errors**
   ```bash
   # Install missing dependencies
   pip install pandas numpy tqdm
   # Or use the full environment setup
   ```

2. **API Key Issues**
   ```bash
   # Verify API keys are set
   echo $ANTHROPIC_API_KEY
   # Re-source your shell configuration
   source ~/.bashrc
   ```

3. **Data Download Issues**
   ```python
   # Check internet connection and disk space
   # Data lake requires ~11GB of storage
   ```

4. **Timeout Errors**
   ```python
   # Increase timeout for complex analyses
   agent = A1(timeout_seconds=1800)
   ```

### Getting Help

1. **Check Documentation**: Review README.md and tutorials
2. **Community Support**: Join the Slack channel
3. **GitHub Issues**: Report bugs and request features
4. **Examples**: Check the tutorials/ directory

## Performance Tips

1. **Use Specific Requests**: More specific requests lead to better results
2. **Batch Similar Tasks**: Group related analyses together
3. **Cache Results**: Save intermediate results for reuse
4. **Monitor Resources**: Keep track of memory and compute usage
5. **Use Appropriate Models**: Choose the right LLM for your task complexity

## Contributing

See `CONTRIBUTION.md` for guidelines on:
- Adding new tools
- Contributing datasets
- Improving documentation
- Reporting bugs

## Next Steps

1. **Explore Tutorials**: Start with `tutorials/biomni_101.ipynb`
2. **Try Examples**: Experiment with different use cases
3. **Join Community**: Connect with other users and contributors
4. **Contribute**: Help improve Biomni for everyone

---

*This guide provides a comprehensive overview of Biomni's capabilities. For the most up-to-date information, please refer to the official documentation and community resources.*