import pandas as pd
import numpy as np

# If they pay $10.00 or less, they get ten_or_less
# If they pay $20.00 or less, they get twenty
# If they pay $30.00 or less, they get thirty
# If they pay $40.00 or less, they get forty
# If they pay $50.00 or less, they get fifty
# If they pay $60.00 or less, they get sixty
# If they pay $70.00 or less, they get seventy
# If they pay $80.00 or less, they get eighty
# If they pay $90.00 or less, they get ninety
# If they pay $90.00 or more, they get more_then_nintey
# else, they get zero, error check
# def group_monthly_charges(df):
#     df['monthly_charges_group'] = np.where( (df['monthly_charges'] <= 10.00), 'ten_or_less',
#                                        np.where( (df['monthly_charges'] <= 20.00), 'twenty',
#                                            np.where( (df['monthly_charges'] <= 30.00), 'thirty',
#                                                np.where( (df['monthly_charges'] <= 40.00), 'forty',
#                                                    np.where( (df['monthly_charges'] <= 50.00), 'fifty',
#                                                         np.where( (df['monthly_charges'] <= 60.00), 'sixty',
#                                                            np.where( (df['monthly_charges'] <= 70.00), 'seventy',
#                                                                np.where( (df['monthly_charges'] <= 80.00), 'eighty',
#                                                                    np.where( (df['monthly_charges'] <= 90.00), 'ninety',
#                                                                        np.where( (df['monthly_charges'] > 90.00), 'more_then_nintey', 'zero'))))))))))
#     return df




# If they have 1 or less , they get one_year
# If they have 2 or less , they get two_years
# If they have 3 or less , they get three_years
# If they have 4 or less , they get four_years
# If they have 5 or less , they get five_years
# If they have 6 or less , they get six_years
# else, they get zero_years, error check
def group_tenure(df):
    df['tenure_group'] = np.where( (df['tenure_months'] <= 1), 'one_year',
                               np.where( (df['tenure_months'] <= 2), 'two_years',
                                   np.where( (df['tenure_months'] <= 3), 'three_years',
                                       np.where( (df['tenure_months'] <= 4), 'four_years',
                                           np.where( (df['tenure_months'] <= 5), 'five_years',
                                               np.where( (df['tenure_months'] > 5), 'six_years', 'zero_years'))))))
    return df


def group_monthly_charges(df):
    df['monthly_charges_group'] = np.where( (df['monthly_charges'] <= 20.00), 'zero to twenty',
                                        np.where( (df['monthly_charges'] <= 40.00), 'twenty_one to forty',
                                                np.where( (df['monthly_charges'] <= 60.00), 'forty_one to sixty',
                                                        np.where( (df['monthly_charges'] <= 80.00), 'sixty_one to eighty',
                                                                    np.where( (df['monthly_charges'] > 80.00), 'more_then_eighty', 'zero')))))
    return df