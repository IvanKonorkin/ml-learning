import json

import pandas as pd


def main():
    with open('data/stats.json') as file:
        json_stats = file.read()
    stats = json.loads(json_stats)

    assets_data = []
    categories_data = []
    accounts_data = []
    for asset in stats['assets'].values():
        for month_id, month in asset['months'].items():
            month_data = month.copy()
            asset_info = {
                'asset_id': asset['asset_id'],
                'units': asset['units'],
                'month_id': month_id,
            }
            for category_id, category in month_data['categories'].items():
                categories_data.append({
                    **asset_info,
                    'category_id': category_id,
                    'actual': category['actual'],
                    'budget': category['budget'],
                })
            for account_id, account in month_data['accounts'].items():
                accounts_data.append({
                    **asset_info,
                    'account_id': account_id,
                    'actual': account['actual'],
                    'budget': account['budget'],
                })
            del month_data['categories']
            del month_data['accounts']
            assets_data.append({
                **asset_info,
                **month_data,
            })
    df = pd.DataFrame.from_records(assets_data)
    categories_df = pd.DataFrame.from_records(categories_data)
    accounts_df = pd.DataFrame.from_records(accounts_data)

    df = df[
        (df['expenses'] != 0)
        & (df['revenue'] != 0)
        & (df['budget_expenses'] != 0)
        & (df['budget_revenue'] != 0)
    ]

    # df[['budget_expenses', 'expenses']] = df[['budget_expenses', 'expenses']].abs()

    # df['expenses_varianse'] = (df['expenses'] - df['budget_expenses']).abs()
    # df['expenses_varianse_persantage'] = [
    #     0 if budget == 0 
    #     else varianse / budget 
    #     for budget, varianse in zip(df['budget_expenses'], df['expenses_varianse'])
    # ]

    # df = df[
    #     (df['expenses_varianse'] > 5000)
    #     & (df['expenses_varianse_persantage'] > 0.1)
    # ]

    # df.sort_values(by=['expenses_varianse'], ascending=False)

    print(df)
    print(categories_df)
    print(accounts_df)


if __name__ == '__main__':
    main()