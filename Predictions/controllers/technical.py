

def predict(company):
    #Enter the prediction here, you will be getting the company code as input Eg: TCS,INFY,HEROMOTOCO
    '''
    :param company: company code
    :return: list
    Output is a list with dictionaries
    Eg:
    [
    {'day':"Tomorrow", 'value':"58.55"},
    {'day':"5 days later", 'value':"58.55"},
    {'day':"10 days later", 'value':"58.55"},
    {'day':"15 days later", 'value':"58.55"},
    .
    .
    .
    .
    ]

    '''
    predictions =  [
    {'day':"Tomorrow", 'value':"58.55"},
    {'day':"5 days later", 'value':"58.55"},
    {'day':"10 days later", 'value':"58.55"},
    {'day':"15 days later", 'value':"58.55"},
    ]
    return predictions

def stock_prices(company):

    #return the list of stock prices and dates(in a dict), list of dicts

    return 0