"""Compare sales and marketing KPIs without inventing attribution.
Usage: pip install pandas openpyxl
       python python/compare_performance.py
"""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"analysis";OUT.mkdir(exist_ok=True)
def load(path):
    df=pd.read_excel(ROOT/path)
    df.columns=[str(c).strip() for c in df.columns]
    print(path,"columns:",list(df.columns))
    return df
def find(df,*names):
    mapping={c.lower().replace("_"," ").strip():c for c in df.columns}
    return next((mapping[n.lower()] for n in names if n.lower() in mapping),None)
sales=load("data/sales_dataset.xlsx")
revenue=find(sales,"Sales","Revenue","Sales Amount")
profit=find(sales,"Profit")
region=find(sales,"Region")
if region and revenue:
    sales[revenue]=pd.to_numeric(sales[revenue],errors="coerce")
    measures={ "revenue":(revenue,"sum"),"records":(revenue,"size")}
    if profit:
        sales[profit]=pd.to_numeric(sales[profit],errors="coerce")
        measures["profit"]=(profit,"sum")
    grouped=sales.groupby(region,dropna=False).agg(**measures)
    if profit: grouped["profit_margin_pct"]=100*grouped.profit/grouped.revenue.where(grouped.revenue!=0)
    grouped.to_csv(OUT/"regional_sales.csv")
marketing=load("data/marketing_dataset.xlsx")
channel=find(marketing,"Channel","Marketing Channel","Campaign Channel")
spend=find(marketing,"Spend","Ad Spend","Cost","Marketing Spend")
clicks=find(marketing,"Clicks")
impressions=find(marketing,"Impressions")
conversions=find(marketing,"Conversions","Total Conversions")
if channel:
    fields={}
    for label,col in (("spend",spend),("clicks",clicks),("impressions",impressions),("conversions",conversions)):
        if col:
            marketing[col]=pd.to_numeric(marketing[col],errors="coerce")
            fields[label]=(col,"sum")
    if fields:
        m=marketing.groupby(channel,dropna=False).agg(**fields)
        if {"clicks","impressions"}<=set(m):m["ctr_pct"]=100*m.clicks/m.impressions.where(m.impressions!=0)
        if {"conversions","clicks"}<=set(m):m["conversion_per_click_pct"]=100*m.conversions/m.clicks.where(m.clicks!=0)
        if {"spend","conversions"}<=set(m):m["cost_per_conversion"]=m.spend/m.conversions.where(m.conversions!=0)
        m.to_csv(OUT/"channel_marketing.csv")
print("Done. Sales and campaign datasets were analyzed separately.")
print("No sales-to-campaign attribution or marketing ROI is inferred without a joining key.")
