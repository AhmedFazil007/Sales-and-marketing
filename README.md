# Sales & Marketing Analytics

**Excel · Power BI · Sales performance · Campaign measurement**

I put two related questions together in this project: **Where are sales coming from, and how can marketing performance be evaluated beyond clicks and impressions?**

The repository contains two dashboards and their Excel datasets—one for sales performance and one for marketing campaigns. I wanted to show how commercial reporting and marketing measurement can support each other, while keeping their KPIs distinct.

## Sales dashboard

![Sales analysis](assets/Sales%20analysis.png)

The sales dataset contains roughly **9,000 records**. In the analysis, total sales were over **$2 million**, the **West region** had the largest contribution, and **Technology** stood out among the categories.

**What I'd investigate next:** Compare sales with profit, discounts and product mix before deciding which regions or categories deserve more investment.

## Marketing dashboard

![Marketing campaign analysis](assets/Marketing.png)

The campaign dataset contains roughly **5,000 records**. I used metrics such as **click-through rate (CTR), conversion rate and cost per acquisition (CPA)** to compare campaign efficiency.

**What I'd investigate next:** Look at channels with stronger conversion efficiency and test whether changing budget allocation improves actual conversions—not just traffic.

## Why these two analyses belong together

A campaign can bring plenty of visitors without producing valuable sales. Likewise, a high-revenue category isn't always the most profitable. Looking at sales and marketing side by side makes it easier to ask whether activity is translating into results.

In a real business setting, I'd want to connect campaign spend to attributable orders and contribution margin before recommending a budget change.

## Reproduce the KPI comparisons

I added a [Python KPI script](python/compare_performance.py) and [analysis notes](docs/KPI_ANALYSIS.md). The script keeps sales and marketing results separate because the datasets do not establish campaign-to-order attribution. The code still needs to be run and its outputs checked.

## Explore the files

| Area | Dataset | Dashboard |
|---|---|---|
| Sales | [sales_dataset.xlsx](data/sales_dataset.xlsx) | [Sales Performance.pbix](powerbi/Sales%20Performance.pbix) |
| Marketing | [marketing_dataset.xlsx](data/marketing_dataset.xlsx) | [Marketing Campaign.pbix](powerbi/Marketing%20Campaign.pbix) |

## A note on impact

This is an analytics portfolio exercise. The dashboards highlight patterns and possible decisions; they don't show that a company implemented the recommendations or achieved a verified increase in sales or marketing ROI.

---

[Ahmed Fazil](https://github.com/AhmedFazil007)
