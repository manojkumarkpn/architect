"""
References:
- https://blog.stackademic.com/15-python-nano-scripts-that-automate-actual-business-problems-3-lines-or-less-5bbaa2c3716f
- 
"""

# Auto-Cleanup Email Attachments (Outlook Integration)
import win32com.client  
[att.SaveAsFile(f"C:/invoices/{att.FileName}") for att in win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI").Folders.Item("Inbox").Items if att.Attachments.Count]

# Download Daily Stock Prices (via Yahoo Finance)
import yfinance as yf  
yf.download("AAPL", period="1d").to_csv("aapl_today.csv")

# Slack Notification on File Drop
import os, time, requests  
while not os.path.exists("report.csv"): time.sleep(5)  
requests.post("https://slack.webhook.url", json={"text": "New report.csv uploaded!"})

# Auto-Back Up Google Sheets to Local CSV
import gspread; import pandas as pd  
df = pd.DataFrame(gspread.service_account().open("Sheet1").sheet1.get_all_records()); df.to_csv("backup.csv", index=False)