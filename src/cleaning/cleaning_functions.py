import pandas as pd

def clean_visitor_events(df):
    df = df.copy()
    df = df.drop_duplicates()
    df = df[df["event_timestamp"].notna()]

    df["event_timestamp"] = pd.to_datetime(df["event_timestamp"], errors="coerce")

    return df


def clean_applications(df):
    df = df.copy()
    df = df.drop_duplicates()

    if "credit_score" in df.columns:
        df.loc[df["credit_score"] < 300, "credit_score"] = 300
        df.loc[df["credit_score"] > 850, "credit_score"] = 850

    df["application_date"] = pd.to_datetime(df["application_date"], errors="coerce")

    return df


def clean_accounts(df):
    df = df.copy()
    df = df.drop_duplicates()

    df["initial_deposit"] = df["initial_deposit"].abs()

    df["account_open_date"] = pd.to_datetime(df["account_open_date"], errors="coerce")

    return df

def clean_transactions(df):
    df = df.copy()
    df = df.drop_duplicates()
    df = df[df["transaction_timestamp"].notna()]

    df["amount"] = df["amount"].abs()

    df["transaction_timestamp"] = pd.to_datetime(df["transaction_timestamp"], errors="coerce")

    return df
