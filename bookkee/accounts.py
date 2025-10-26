
from abc import ABC
import pandas as pd

sheet_names = [ 'book', 'rules', 'conf' ]

# TODO
columns = { 
    'book': [],
    'rules': [],
    'conf': []
}

class Account(ABC):

    def __init__(self, file, book = None, rules = None, conf = None):
        self.file = file
        self.book = pd.DataFrame(columns=columns['book']) if book is None else book
        # TODO: format rules?
        self.rules = pd.DataFrame(columns=columns['rules']) if rules is None else rules
        # TODO: default conf?
        self.conf = {} if conf is None else None
        return self
    

    @staticmethod
    def read_books(filename_or_object):
        filename = filename_or_object if isinstance(filename_or_object, str) else filename_or_object.name
        try:
            all_excel_sheets = pd.read_excel(filename, None)
        except:
            raise Exception(f'The file {filename} is not a valid Excel file.')
        valid_sheet_names = [ sheet_name for sheet_name in all_excel_sheets.keys() if sheet_name.endswith('.book') or sheet_name.endswith('.rules') or sheet_name.endswith('.conf') ]
        accounts_names = set([ sheet.split('.')[:-1] for sheet in valid_sheet_names ])
        accounts = {}
        for account in accounts_names:
            data = {}
            for sheet in sheet_names:
                if f'{account}.{sheet}' in  valid_sheet_names:
                    data[sheet] = all_excel_sheets[ f'{account}.{sheet}' ]
                else:
                    raise Exception(f'{account}.{sheet} not found among sheet names in {filename}')   
            accounts[account] = Account(file = filename,
                                        book = data['book'],
                                        rules = data['rules'],
                                        conf = data['conf']
                                        )
            # conf = parse_general_config(all_excel_sheets['general.conf'])
        return accounts

