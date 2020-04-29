import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

pd.options.display.float_format = '{:.3f}'.format


# monthly charges set to groups by range
def group_monthly_charges(df):
    df['monthly_charges_group'] = np.where( (df['monthly_charges'] <= 20.00), 'one_to_twenty',
                                        np.where( (df['monthly_charges'] <= 30.00), 'twenty_one_to_thirty',
                                            np.where( (df['monthly_charges'] <= 40.00), 'thirty_one_to_forty',
                                                np.where( (df['monthly_charges'] <= 50.00), 'forty_one_to_fifty',
                                                     np.where( (df['monthly_charges'] <= 60.00), 'fifty_one_to_sixty',
                                                         np.where( (df['monthly_charges'] <= 70.00), 'sixty_one_to_seventy',
                                                            np.where( (df['monthly_charges'] <= 80.00), 'seventy_one_to_eighty',
                                                                np.where( (df['monthly_charges'] <= 90.00), 'eighty_one_to_ninety',
                                                                    np.where( (df['monthly_charges'] <= 100.00), 'ninety_one_to_one_hundred',
                                                                        np.where( (df['monthly_charges'] <= 110.00), 'one_hundred_to_one_hundred_ten',
                                                                            np.where( (df['monthly_charges'] <= 120.00), 'one_hundred_eleven_to_hundred_twenty',
                                                                                np.where( (df['monthly_charges'] > 120.00), 'more_then_one_hundred_twenty', 'zero'))))))))))))
    return df

# just adding a line

# tenure divided into groups by six month increaments
def group_tenure(df):
    df['tenure_group'] = np.where( (df['tenure_years'] <= .5), 'half_a_year',
                               np.where( (df['tenure_years'] <= 1), 'one_year',
                                   np.where( (df['tenure_years'] <= 1.5), 'one_&_a_half_years',
                                       np.where( (df['tenure_years'] <= 2), 'two_years',
                                           np.where( (df['tenure_years'] <= 2.5), 'two_&_a_half_years',
                                                np.where( (df['tenure_years'] <= 3), 'three_years',
                                                   np.where( (df['tenure_years'] <= 3.5), 'three_&_a_half_years',
                                                       np.where( (df['tenure_years'] <= 4), 'four_years',
                                                           np.where( (df['tenure_years'] <= 4.5), 'four_&_a_half_years',
                                                               np.where( (df['tenure_years'] <= 5), 'five_years',
                                                                    np.where( (df['tenure_years'] <= 5.5), 'five_&_a_half_years',
                                                                       np.where( (df['tenure_years'] > 5.5), 'six_or_more_years', 'zero_years'))))))))))))
    
    return df


def start_explore():
    df = pd.read_csv('train.csv')
    df = group_monthly_charges(df)
    df = group_tenure(df)
    return df


def plot_data(df, list):
    for x in list:
        plt.figure(figsize=(14,10))
        sns.countplot(x, data=df, hue='churn')
        plt.show()
        print()
        
def get_dsl_fiber_sig(alpha, dsp_p, dstp_p, dsm_p, fstp_p, fsmp_p):
    return ([
        print('The folowing combinations were found to be significant:\n'),
        print(f'Aplha: {alpha}\n'),
        print('- DSL,onliine security, & phone  p-value: {:.4f}\n'.format(dsp_p)),
        print('- DSL, tech support, & phone       p-value: {:.4f}\n'.format(dtsp_p)),
        print('- DSL, streaming tv, & phone       p-value: {:.4f}\n'.format(dstp_p)),
        print('- DSL, streaming movies            p-value: {:.4f}\n'.format(dsm_p)),
        print('- fiber,sreaming tv, & phone       p-value: {:.4f}\n'.format(fstp_p)),
        print('- fiber,streaming movie, & phone   p-value: {:.4f}\n'.format(fsmp_p))
    ]) 
