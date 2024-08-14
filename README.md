
# Customer Analytics Data Pipeline

This project is an automated data pipeline for customer analytics using open-source tools. The pipeline performs data ingestion, preprocessing, feature engineering, model training, and workflow automation.

## Project Structure

- **data_ingestion/**: Contains scripts for data ingestion using Apache NiFi.
- **data_processing/**: Contains scripts for data cleaning and feature engineering.
- **model_training/**: Contains scripts for model training and evaluation using TensorFlow.
- **workflow_automation/**: Contains scripts for setting up Airflow DAGs.
- **data_visualization/**: Contains scripts for setting up Metabase and Redash.
- **utils/**: Contains utility scripts for logging and data loading.
- **tests/**: Contains unit tests for the modules.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd customer_analytics_pipeline
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the project using Docker:
   ```bash
   docker build -t customer_analytics .
   docker run -p 8080:8080 customer_analytics
   ```

## Usage

- **Data Ingestion**: Use `ingestion.py` to start data ingestion.
- **Data Processing**: Use `preprocessing.py` and `feature_engineering.py` to clean and prepare data.
- **Model Training**: Use `churn_prediction.py` to train and evaluate the model.
- **Workflow Automation**: Set up the Airflow DAG using `airflow_setup.py`.

## Testing

Run unit tests:
```bash
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT License.
