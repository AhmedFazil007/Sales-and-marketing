# Sales and Marketing KPI Analysis

I added a reproducible Python analysis to compare **sales by region** and **marketing efficiency by channel** using the two Excel datasets.

Run:

```bash
pip install pandas openpyxl
python python/compare_performance.py
```

If the expected columns are available, the script exports `analysis/regional_sales.csv` and `analysis/channel_marketing.csv`. It prints the actual source column names so mismatches can be checked.

**Important distinction:** The two datasets are analyzed separately. A channel's cost per conversion is not the same as acquisition cost, and campaign ROI cannot be calculated without reliable revenue attribution. I have not claimed that a marketing campaign caused the sales observed in the separate sales dataset.

The script still needs to be executed against the workbooks and the exported results validated.
