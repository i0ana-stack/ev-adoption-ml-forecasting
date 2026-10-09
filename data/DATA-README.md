\# Dataset



The dataset used in this project is provided through the \*\*Washington State Open Data Portal\*\*.



\## Source



The data is accessed directly through the public API:



`https://data.wa.gov/resource/f6w7-q2d2.csv`



The notebook loads the dataset dynamically from this endpoint, so the project does not store a local copy of the raw dataset.



\## Dataset Description



The dataset contains records of electric vehicles registered in Washington State and includes variables such as:



\- Model year

\- Manufacturer

\- Electric vehicle type

\- Clean Alternative Fuel Vehicle (CAFV) eligibility

\- Electric range

\- County



\## Reproducibility



Because the dataset is retrieved directly from the public API, the available records may change over time. As a result, model results and forecasts may differ slightly when the notebook is rerun at a later date.



The preprocessing and analysis steps used in the project are documented in the main notebook.

