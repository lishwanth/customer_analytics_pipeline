
# Customer Analytics Data Pipeline

## Overview

This project is an automated data pipeline for customer analytics using open-source tools. The pipeline handles data ingestion, preprocessing, feature engineering, model training, and workflow automation, all while leveraging object-oriented programming (OOP) principles.

## Tools Used

- **Apache NiFi**: For creating and managing data ingestion pipelines.
- **Apache Airflow**: For workflow automation and orchestration.
- **TensorFlow**: For building and training machine learning models, particularly for churn prediction.
- **Metabase/Redash**: As alternatives to Power BI for data visualization.
- **Python**: The primary programming language used, with libraries like Pandas, Scikit-learn, and TensorFlow.

## Project Structure

```
customer_analytics_pipeline/
│
├── data_ingestion/
│   ├── ni-fi_templates/
│   │   └── nifi_template.xml            # NiFi template for data ingestion
│   ├── ingestion.py                     # Script to handle data ingestion using NiFi API
│   └── config.py                        # Configuration file for data ingestion
│
├── data_processing/
│   ├── preprocessing.py                 # Script for data cleaning
│   ├── feature_engineering.py           # Script for feature engineering
│   ├── config.py                        # Configuration file for data processing
│
├── model_training/
│   ├── churn_prediction.py              # Main script to train and evaluate churn prediction model
│   ├── evaluation.py                    # Script to evaluate the model's performance
│   ├── config.py                        # Configuration file for model training
│   └── model.py                         # Script defining the model architecture
│
├── workflow_automation/
│   ├── airflow_dags/                    # Directory to store Airflow DAGs
│   ├── airflow_setup.py                 # Script to set up Airflow DAGs
│   └── config.py                        # Configuration file for workflow automation
│
├── data_visualization/
│   ├── metabase_setup.py                # Script to set up Metabase for data visualization
│   └── redash_setup.py                  # Script to set up Redash for data visualization
│
├── utils/
│   ├── logger.py                        # Logger utility for consistent logging across modules
│   ├── data_loader.py                   # Utility to load data for processing and model training
│   └── config.py                        # General configuration file
│
├── tests/
│   ├── test_ingestion.py                # Unit tests for data ingestion module
│   ├── test_processing.py               # Unit tests for data processing module
│   ├── test_model_training.py           # Unit tests for model training module
│   └── test_workflow.py                 # Unit tests for workflow automation
│
├── Dockerfile                           # Docker setup for containerizing the application
├── requirements.txt                     # List of required Python packages
└── README.md                            # Project documentation
```

## Setup

### Prerequisites

- Docker
- Python 3.7+
- Apache NiFi
- Apache Airflow
- Metabase/Redash (Optional)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd customer_analytics_pipeline
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the project using Docker**:
   ```bash
   docker build -t customer_analytics .
   docker run -p 8080:8080 customer_analytics
   ```

## Usage

### Data Ingestion

- Use the NiFi template in `data_ingestion/ni-fi_templates/nifi_template.xml` to set up data ingestion from a local file system or any other source.

### Data Processing

- Preprocess and engineer features by running the scripts in the `data_processing` module.

### Model Training

- Train and evaluate the churn prediction model using the scripts in the `model_training` module.

### Workflow Automation

- Set up the Airflow DAG using `workflow_automation/airflow_setup.py` to automate the entire pipeline.

### Data Visualization

- Use `data_visualization/metabase_setup.py` or `data_visualization/redash_setup.py` to visualize the processed data and model results.

## Testing

Run unit tests for each module:
```bash
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT License.
