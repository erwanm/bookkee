import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# A rule is a dict with keys:
# - N: int, interval of time expressed in time_unit
# - time_unit: 'days', 'weeks', 'months', 'years'
# - from_date: date, start of the rule being applied
# - time_span: 'forever', 'only once', 'until ...'
# - to_date: date, defined only if time_span is 'until ...'
# - window: int, number of days allowed between expected date and real date
# - must_happens: bool, whether the rule can or must be applied
# - disabled: bool, whether the rule is currently disabled
# - text_contains: str, text filter being applied
# - amount_range: bool, whether the amount is a range or a single value
# - amount: pair (float, float), the amount to match (absolute value)
# - sign: 'any', 'credit', 'debit'
#

def newrule_form(edit_existing_rule = None, from_transaction = None):
    newrule = {}
    # if using form, no dynamic behaviour possible within the form, since
    # variables are not assigned
    # with st.form("newrule_form"):
    row1 = st.columns([1,3,3])
    with row1[0]:
        st.write('Every')
    with row1[1]:
        newrule['N'] = st.number_input("every",
                key = 'newrule_N',
                value = 1,
                min_value = 1,
                format = "%d",
            label_visibility="collapsed")
    with row1[2]:
        newrule['time_unit'] = st.selectbox('unit',
            ['days', 'weeks', 'months', 'years'], 
            index=2, 
            key='newrule_timeunit', 
            label_visibility="collapsed")

    row2 = st.columns([1,1,1])
    with row2[0]:
        newrule['from_date'] = st.date_input(label = 'From',
            key='newrule_startdate', 
            format="DD/MM/YYYY")
            #label_visibility="collapsed")
        newrule['disabled'] = st.checkbox('Disabled')
    with row2[1]:
        newrule['time_span'] = st.radio('Apply',
            options = [ 'forever', 'only once', 'until ...' ],
            key = 'newrule_timespan',
            label_visibility="collapsed")
#            on_change = newrule_timespan_change)
        newrule['to_date'] = st.date_input(label = 'Until',
            key='newrule_enddate', 
            format="DD/MM/YYYY",
            label_visibility="collapsed",
            disabled = newrule['time_span'] != 'until ...')
    with row2[2]:
        newrule['window'] = st.number_input("Within n days",
            key = 'newrule_window',
            value = 5,
            min_value = 1,
            max_value = 30,
            format = "%d")
        must_happen = st.radio('Must happen?',
            options = [ 'optional', 'must happen'],
            key = 'newrule_must',
            label_visibility="collapsed")
        newrule['must_happen'] = (must_happen == 'must happen')

    row3 = st.columns([1,4])
    with row3[0]:
        st.write('Text contains:')
    with row3[1]:
        newrule['text_contains'] = st.text_input('Text contains:',
            key='newrule_text',
            label_visibility="collapsed")

    row3 = st.columns([2,3])
    with row3[0]:
        newrule['amount_range'] = st.checkbox('Amount range')
    with row3[1]:
        newrule['sign'] = st.radio('sign',
            options = [ 'any', 'credit', 'debit' ],
            key = 'newrule_sign',
            horizontal = True,
            label_visibility="collapsed")

    row4 = st.columns([1,1])
    with row4[0]:
        if newrule['amount_range']:
            min_amount = st.number_input('Min amount',
                min_value = 0,
                key = 'newrule_minamount')
        else:
            min_amount = st.number_input('Amount',
                min_value = 0,
                key = 'newrule_amount')
            max_amount = min_amount
    with row4[1]:
        max_amount = st.number_input('Max amount',
            key = 'newrule_maxamount',
            min_value = 0,
            disabled = not newrule['amount_range'])

    newrule['amount'] = (min_amount, max_amount)
    return newrule

#        st.form_submit_button('Create rule')

#col1, col2 = st.columns([2,3])
with col1:
    newrule_form()

