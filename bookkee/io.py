
import pandas as pd


def read_books(uploaded_file):
    filename = uploaded_file if isinstance(uploaded_file, str) else uploaded_file.name
    try:
        all_excel_sheets = pd.read_excel(uploaded_file, None)
    except:
        raise Exception(f'The file {filename} is not a valid Excel file.')
    valid_sheet_names = [ sheet_name for sheet_name in all_excel_sheets.keys() if sheet_name.endswith('.book') or sheet_name.endswith('.rules') or sheet_name.endswith('.conf') ]:
    accounts_names = set([ sheet.split('.')[:-1] for sheet in valid_sheet_names ])
    data = {}
    for sheet in [ 'book', 'rules', 'bank', 'conf' ]:
        data[sheet] = {}
        for account in accounts_names:
            if f'{account}.{sheet}' in  valid_sheet_names:
                data[sheet][account] = all_excel_sheets[ f'{account}.{sheet}' ]
            else:
                raise Exception(f'{account}.{sheet} not found among sheet names in {filename}')   

    # conf = parse_general_config(all_excel_sheets['general.conf'])
    return data


