import random

CATEGORY_MAP = [
    {"main": "Financials", "keywords": ["Quarterly Results","Annual Results","Financial Results","Earnings","Audited","Unaudited"], "emojis": ["📊","💹","📈"]},
    {"main": "Dividend", "keywords": ["Interim Dividend","Final Dividend","Dividend"], "emojis": ["💰","💸"]},
    {"main": "Buyback", "keywords": ["Share Buyback","Buyback","Offer Price"], "emojis": ["🔄","💵"]},
    {"main": "Bonus / Split", "keywords": ["Bonus Issue","Stock Split","Split"], "emojis": ["⚙️","🔧"]},
    {"main": "IPO / Offer", "keywords": ["IPO","FPO","Issue Price","Offer Size"], "emojis":["🆕","💵"]},
    {"main": "Fund Raising", "keywords": ["QIP","Qualified Institutional Placement","Allotment","Debenture","NCD","Bond","Debt Issue","Warrants"], "emojis": ["💳","💵"]},
    {"main": "M&A / Strategic Deal", "keywords": ["Merger","Acquisition","Takeover","Strategic Partnership","Joint Venture","Amalgamation"], "emojis":["🤝","🏢"]},
    {"main": "Order Win", "keywords": ["Order Win","Contract Win","New Order"], "emojis": ["🏗","📦"]},
    {"main": "Expansion / Capex", "keywords": ["Expansion","Capex","New Plant","Project Launch"], "emojis": ["🏢","🛠"]},
    {"main": "Rating / Credit Action", "keywords": ["Credit Rating","Rating Agency","Upgrade","Downgrade","Moody's","CRISIL","ICRA"], "emojis":["📈","📉"]},
    {"main": "Insolvency", "keywords": ["Insolvency","Bankruptcy","NCLT"], "emojis": ["⚖️","🏛"]},
    {"main": "Litigation", "keywords": ["Litigation","Court Case","Legal Notice"], "emojis":["⚖️","📜"]},
    {"main": "Tax Notice", "keywords": ["Tax Notice","Income Tax","GST"], "emojis":["📄","💰"]},
    {"main": "Shareholding", "keywords": ["Shareholding Pattern","Top Shareholders","Bulk Deal","Promoter Holding","Insider Trading","Pledge"], "emojis":["📊","📋","📈"]},
    {"main": "Governance", "keywords": ["Appointment","Resignation","Independent Director","Board Meeting","Related Party Transaction","RPT"], "emojis":["👥","🔗"]},
    {"main": "Exchange Action", "keywords": ["Listing","New Listing","Suspension","Trading Halt","Delisting","Exit Offer"], "emojis":["🆕","⛔","❌"]},
    {"main": "Regulatory / Compliance", "keywords": ["SEBI","FEMA","Regulation 30","LODR","Listing Compliance","Disclosure","Intimation"], "emojis":["📄","⚖️"]},
    {"main": "Guidance", "keywords": ["Guidance","Forecast","Outlook","Projection"], "emojis": ["🔮","📉"]},
    {"main": "Record Date", "keywords": ["Record Date","Ex-Date"], "emojis":["📅","💰"]},
    {"main": "Other", "keywords": [], "emojis":["📢"]}
]

def categorize_announcement(text):
    text_lower = text.lower()
    for category in CATEGORY_MAP:
        for keyword in category["keywords"]:
            if keyword.lower() in text_lower:
                emoji = random.choice(category["emojis"])
                return category["main"], emoji
    return "Other", "📢"
