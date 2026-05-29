# PROBLEM STATEMENT (Car Sales - Data Analysis)

## DASHBOARD 1: OVERVIEW

### KPI’s Requirement

#### 1. Sales Overview
- Year-to-Date (YTD) Total Sales
- Month-to-Date (MTD) Total Sales
- Year-over-Year (YOY) Growth in Total Sales
- Difference between YTD Sales and Previous Year-to-Date (PTYD) Sales

#### 2. Average Price Analysis
- YTD Average Price
- MTD Average Price
- YOY Growth in Average Price
- Difference between YTD Average Price and PTYD Average Price

#### 3. Cars Sold Metrics
- YTD Cars Sold
- MTD Cars Sold
- YOY Growth in Cars Sold
- Difference between YTD Cars Sold and PTYD Cars Sold


Calculations:

> CALENDER(MIN(data[date]), MAX(data[date]))
> YEAR('table'[date])
> FORMAT('table'[date], "MMMM")
> WEEKNUM('table'[date])

> YTD TOTAL SALES = TOTALYTD(SUM(data['price']), 'table'[date])
> PYTD Total Sales = CALCULATE(SUM(data['price']), SAMEPERIODLASTYEAR('table'[date]))
> IF( > 0, '', '')

> YOY SALES GROWTH = profit / pytd