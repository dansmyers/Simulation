# Monte Carlo Portfolio Simulation

<img src="https://compote.slate.com/images/926e5009-c10a-48fe-b90e-fa0760f82fcd.png?width=1200&rect=680x453&offset=0x30" width="400px" />

*number go up*

## Overview

**Portfolio simulation** is a practically significant application of the Monte Carlo technique.

The core question in financial planning is _Will I have enough?_ That is, will my portfolio of investments yield results that will allow me to retire/send my kids to college/etc. with a desired level of security?

One way to address this question is through Monte Carlo simulation. Given a starting allocation of stocks, bonds, and other investments, perform simulated experiments that predict how the portfolio's value will evolve over time. Typically, this is done in a way that allows the analyst to examine a variety of market trajectories to see how the portfolio performs under both good and adversarial circumstances.

In this project, you're going to use a Monte Carlo simulation to answer a simple financial question: What is the effect of beginning your investments at age 22 vs. age 32, over a lifetime leading up to retirement at age 65?

To simulate these returns, we'll use historical stock market return data from Yahoo Finance.

## Investing Background

(Obviously, I am not your financial advisor, but the following are basic details that are covered in most personal finance guides.)

### 401(k)

In the older days, many workers received pensions from their employers. Once a person retired, a pension plan would pay out a pre-set amount of money (a *defined benefit*) regularly for the rest of that person's life.

These days, traditional pensions have largely been phased out for most prviate-sector employees. Most Americans, other than the independently wealthy, rely on two sources of income to fund their living in retirement years:

- **Social Security**, the government program that provides monthly payments to the elderly, paid for by payroll taxes on current workers.

- **Returns from investments**, accumulated during working years. The most important vehicle for building wealth through investing is the 401(k) account, named for the section of the tax code that defines it.

The 401(k) allows workers to place a portion of their pre-tax income into a special account using automatic payroll deductions; every month a bit of your check is deducted and automatically invested into a fund that you've set up. Most employers will also **match** 401(k) contributions up to a certain amount: this can be a major source of free money for retirement.

401(k) plans are tax-advantaged, in that the money that goes into them reduces your taxable income and the money in the fund is not taxed until you withdraw it much later. In return there are restrictions: the amount you can put into a 401(k) annually is capped (currently about $23,000) and there are significant penalties if you withdraw funds before age 59.5.

### Roth IRA

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxnsBMgedbPWL1JbXcNtPfWd_HR35__QdZrQ&s" width="150px" />

Another type of retirement account that you'll frequently hear about is the **Roth IRA**, named after its creator, Van Halen lead singer and tax policy expert David Lee Roth ([not really](https://en.wikipedia.org/wiki/William_Roth)).

A Roth IRA has a different set of tax advantages: you deposit post-tax money into it, but withdrawals are tax free.

### Index funds

So, given that you're going to invest, how should you allocate your money?

- One option is to buy a basket of stocks that seem good. Right now, that would be, say, Nvidia, Apple, and Tesla, but those stocks might not be good forever. Picking good stocks requires knowledge and skill, and trying to trade too frequently can lead to high fees from brokers, so ideally you'd like to choose a good collection of stocks that are likely to go up for a long time.

- Rather than buying individual stocks, most retail investors put their money into **mutual funds**. The fund manages the buying and selling of stocks with the goal of securing the best returns and minimizing downside risk. Many funds are *actively managed* and charge fees to their investors that go toward compensating the fund supervisors.

Research has shown, however, that both of these approaches are undesirable for regular investors. Instead, the superior approach is to simply **own the entire stock market**. That is, instead of trying to pick which specific stocks will "win" over time, just invest in a broad index that holds a large collection of stocks that represent the general stock market.

It's been shown, empirically, that **index funds outperform almost all managed funds** over long periods of time. In a given year, some fund managers might "beat the market", but in the long run, a diversified approach tends to generate higher returns. Intuitively, investing in an index fund is like investing in the general strength of the U.S. economy.

The most important stock market index is the **S&P 500**, the collection of 500 of the largest companies traded on U.S. stock exchanges. The S&P 500 is often used as a measure of the overall strength of the stock market. Another index you may have heard of is the Dow Jones Industrial Average, which is prominently reported in the media, but the Dow is composed of only 30 companies.
 
Investing in index funds is often referred to as *passive investing* and index funds charge no or minimal fees, since they don't sell the idea of active management as a way to beat the market. This is a significant advantage: over time, paying active managment fees can noticeably eat into returns.

### Other details

- In practice, index funds still do transactions to periodically rebalance their holdings as the values of stocks in the market change. There are also techniques that allow a fund to mirror the performance of the complete index without actually needing to literally own shares of every stock.

- There are index funds other than the S&P 500, some of which are specialized in particular areas, like emerging markets, large cap stocks, etc. A more advanced strategy is to balance your allocations across a few different index funds for more diversification.

- There are *target date* funds aimed at people that want to retire in a particular year. These funds start with a higher-risk, growth-oriented allocation and then gradually shift to a lower-risk allocation as the target approaches.

- **Hedge funds** are a very different thing and use all kinds of complex financial techniques to generate high returns. They are generally only accessible to the extremely wealthy.

## Details

Write a program that simulates market returns for a person who begins investing in an index fund at age 22 and continues until age 65.

- The investor starts with an investment of $1000 and then invests another $1000 every month for 516 months

- For every month, simulate a percentage movement of the market up or down by sampling from the dataset of historical market returns, discussed below

- After 516 months, you'll end with an estimate of the value of the portfolio at the time of retirement

- Repeat for a total of 1000 simulations

- Calculate the average expected portfolio value from the 1000 simulated estimates, along with 90%, 95%, and 99% confidence intervals for the true mean return

Repeat the same simulation for a person starting at age 32, for a total of 396 months of returns.

Make a side-by-side box plot comparing the distributions of returns generated in both cases.


## Sampling Returns

The core of the simulation is modeling how much the market moves up or down each month.

To do this, we'll use historical data from Yahoo Finance.

- Pull monthly close prices for the S&P 500 using the Yahoo Finance API
- Calculate the month-to-month percentage changes
- On each step of your simulation, sample a value from this dataset (with replacement) and use it to adjust the value of the portfolio up or down

For example, if you sample a month where the market went up 1%, you would increase the value of the portfolio by 1%. If you sampled a value of -.5%, you would adjust the value of the portfolio down by .5%.

The script below uses the `yfinance` API to pull monthly return data for 1985 to the present. Use it as a starting point for the rest of your program.
```
"""
Monthly stock market returns using Yahoo Finance
"""
import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Time period
start_date = '1985-01-01'
end_date = '2025-01-31'

# Download S&P 500 data - '^GSPC' is the Yahoo Finance ticker for the S&P 500
ticker_data = yf.Ticker('^GSPC')
sp500_data = ticker_data.history(start='1970-01-01', auto_adjust=False, actions=False, interval='1mo')
print(sp500_data.head())

# Calculate percentage monthly returns
#
# 'Adj Close' is the close price at the end of each month accounting for stock splits
# and reinvesting dividends over time
sp500_data['Monthly_Return'] = sp500_data['Adj Close'].pct_change()

# Remove the first row which will have NaN for return
sp500_returns = sp500_data['Monthly_Return'].dropna()

# Display a few monthly returns
print(sp500_returns.head())
```

## Submission

Submit the following:

- Your script that performs both simulations and the analysis
- Your side-by-side box plot showing the distributions of sampled outcomes for the two ages
- A short text document giving the means, 90% CIs, and 95% CIs for the two ages


