# Anamoly-detection-project-

flowchart TD

A[Raw Synthetic Data<br>visitor_events, marketing_source,<br>applications, accounts, transactions] 
    --> B[Data Cleaning Layer<br>- Standardization<br>- Missing Value Handling<br>- Deduplication]

B --> C[Technical Data Quality (TDQ)<br>- Schema Validation<br>- Null Checks<br>- Freshness Checks<br>- Volume Drift Detection]

C --> D[Business Data Quality (BDQ)<br>- Visitor → Application Mapping<br>- Application → Account Mapping<br>- Range Validations<br>- Marketing Attribution<br>- Cross-Table Consistency]

D --> E[ML Anomaly Detection<br>- Time-Series Anomalies<br>- Row-Level Outliers]

E --> F[Reports & Dashboards<br>TDQ/BDQ Reports<br>Anomaly Visualizations<br>Interactive Notebooks]
