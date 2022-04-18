import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn.linear_model import LogisticRegression
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.weightstats import ttest_ind
import seaborn as sns
from sklearn.svm import SVC
import pandas as pd
import ssl
import certifi
from  urllib.request import urlopen
import plotly.figure_factory as ff
import json

df = pd.read_csv('combined_ri_data.csv')

#PRE-PROCESS/FILTER DATA
#limit to one to four family dwellings
df = df[df['property_type_name']== 'One-to-four family dwelling (other than manufactured housing)']
#limit to co_applicant_race == 'No co_applicant' 
df = df[df['co_applicant_ethnicity_name'] == 'No co-applicant']
df['is_denial'] = (df['action_taken_name'] == 'Application denied by financial institution')

#TO-DO
#examine pct of entries with no information or not applicable for race, sex, 
print(' ')
removals = df[df['applicant_race_name_1'] != 'Information not provided by applicant in mail, Internet, or telephone application']
removals = removals[removals['applicant_race_name_1'] != 'Not applicable']
print('percentage of entries without race- ', 1- len(removals)/len(df))

print(' ')
removals = df[df['applicant_sex_name'] != 'Information not provided by applicant in mail, Internet, or telephone application']
removals = removals[removals['applicant_sex_name'] != 'Not applicable']
print('percentage of entries without sex- ', 1- len(removals)/len(df))

#percent with no income across sex
print(' ')
removals = df[df['applicant_sex_name'] == 'Male']
num_blank = len(removals[removals['applicant_income_000s'].isna() == True])
print('males with blank income:', num_blank/len(removals))
print(' ')
removals = df[df['applicant_sex_name'] == 'Female']
num_blank = len(removals[removals['applicant_income_000s'].isna() == True])
print('females with blank income:', num_blank/len(removals))


#hypothesis questions- 
'''
Examining bias in the data
1. applicant_race_name and percentage of denials (action_taken)
	limit to applicant_race != 'Information not provided' or 'Not applicable'
	consider only the first race listed by applicants
'''
sub_df = df[df['applicant_race_name_1'] != 'Information not provided by applicant in mail, Internet, or telephone application']
sub_df = sub_df[sub_df['applicant_race_name_1'] != 'Not applicable']
print(' ')
print('denial pcts')
races = list(set(sub_df['applicant_race_name_1']))
pcts = []
ns = []
for race in races:
	race_df = sub_df[sub_df['applicant_race_name_1'] == race]
	pct = race_df['is_denial'].sum()/len(race_df)
	pcts.append(pct)
	ns.append(len(race_df))
	print(race, pct, len(race_df))
print(' ')

#minority vs white denial percentage
minorities = sub_df[sub_df['applicant_race_name_1'] != 'White']
min_count = minorities['is_denial'].sum()
min_nobs = len(minorities)
white = sub_df[sub_df['applicant_race_name_1'] == 'White']
wh_count = white['is_denial'].sum()
wh_nobs = len(white)
counts = np.array([min_count, wh_count])
nobs = np.array([min_nobs, wh_nobs])
print('minority denials, white denials:', counts/nobs)
stat, pval = proportions_ztest(counts, nobs)
print('p value 2 sample independent proportions z test')
print('{0:0.3f}'.format(pval))

'''
2. applicant income vs. applicant race
	limit to applicant_race != 'Information not provided'
	DO NOT limit to filled in income
'''
#sub_df = sub_df[sub_df['applicant_income_000s'].isna() != True]
sub_df['applicant_income_000s'] = sub_df['applicant_income_000s'].fillna(0)
races = list(set(sub_df['applicant_race_name_1']))
avgs = []
ns = []
print(' ')
print('avg incomes')
for race in races:
	race_df = sub_df[sub_df['applicant_race_name_1'] == race]
	avg = race_df['applicant_income_000s'].sum()/len(race_df)
	avgs.append(avg)
	ns.append(len(race_df))
	print(race, avg, len(race_df))
print(' ')

#minority vs white income
minorities = sub_df[sub_df['applicant_race_name_1'] != 'White']
min_income = minorities['applicant_income_000s'].values
white = sub_df[sub_df['applicant_race_name_1'] == 'White']
white_income = white['applicant_income_000s'].values

tstat, pval, degrees = ttest_ind(min_income, white_income, alternative='smaller', usevar='pooled')
print('two sample t-test white vs. minority - tstat, pval, dof:', tstat, pval, degrees)

'''
3. applicant_sex_name and percentage of denials (action_taken)
	applicant_sex != 'Information not provided'
'''
sub_df = df[df['applicant_sex_name'] != 'Information not provided by applicant in mail, Internet, or telephone application']
sub_df = sub_df[sub_df['applicant_sex_name'] != 'Not applicable']
print(' ')
print('denial pcts')
races = list(set(sub_df['applicant_sex_name']))
pcts = []
ns = []
for race in races:
	race_df = sub_df[sub_df['applicant_sex_name'] == race]
	pct = race_df['is_denial'].sum()/len(race_df)
	pcts.append(pct)
	ns.append(len(race_df))
	print(race, pct)
print(' ')


#male vs female denial pct
male = sub_df[sub_df['applicant_sex_name'] == 'Male']
m_count = male['is_denial'].sum()
m_nobs = len(male)
female = sub_df[sub_df['applicant_sex_name'] != 'Male']
f_count = female['is_denial'].sum()
f_nobs = len(female)
counts = np.array([m_count, f_count])
nobs = np.array([m_nobs, f_nobs])
stat, pval = proportions_ztest(counts, nobs)
print('p value 2 sample independent proportions z test')
print('{0:0.3f}'.format(pval))

'''
4. applicant income vs. applicant sex
	limit to applicant_sex != 'Information not provided'
	limit to filled in income
'''
#sub_df = sub_df[sub_df['applicant_income_000s'].isna() != True]
sub_df['applicant_income_000s'] = sub_df['applicant_income_000s'].fillna(0)
races = list(set(sub_df['applicant_sex_name']))
avgs = []
ns = []
print(' ')
print('avg incomes')
for race in races:
	race_df = sub_df[sub_df['applicant_sex_name'] == race]
	avg = race_df['applicant_income_000s'].sum()/len(race_df)
	avgs.append(avg)
	ns.append(len(race_df))
	print(race, avg)
print(' ')

#male vs female income
male = sub_df[sub_df['applicant_sex_name'] == 'Male']
m_income = male['applicant_income_000s'].values
female = sub_df[sub_df['applicant_sex_name'] != 'Male']
f_income = female['applicant_income_000s'].values

tstat, pval, degrees = ttest_ind(m_income, f_income, alternative='larger', usevar='pooled')
print('tstat, pval, dof:', tstat, pval, degrees)
print(' ')


'''
Examining non-biased reasons for disparities
5. income/loan_amount vs denial coefficient
	treat blank income as no income
'''

df['applicant_income_000s'] = df['applicant_income_000s'].fillna(value = 0) 
income =  np.array(df['applicant_income_000s'].values)
income = np.reshape(income, (-1,1))
print(income)
denials = df['is_denial']
denials = np.array(denials.values)
income = np.concatenate((income, np.ones((len(income),1))), axis = 1)
logit_model=sm.Logit(denials, income)
result=logit_model.fit()
print(result.summary())

#outcome- race correlated with denial, income correlated with denial, gender not correlated with denial
#income not correlated with denial through gender, probably only race

'''
6: distribution of denials across sex and races
HEATMAP
'''

sub_df = df[df['applicant_race_name_1'] != 'Information not provided by applicant in mail, Internet, or telephone application']
sub_df = sub_df[sub_df['applicant_race_name_1'] != 'Not applicable']
sub_df = sub_df[sub_df['applicant_sex_name'] != 'Information not provided by applicant in mail, Internet, or telephone application']
sub_df = sub_df[sub_df['applicant_sex_name'] != 'Not applicable']
ctab = pd.crosstab(sub_df['applicant_race_name_1'], sub_df['applicant_sex_name'], values=sub_df['is_denial'], aggfunc=np.mean)
#PLOT HEATMAP 
print(ctab)

ax = sns.heatmap(data = ctab, annot = True, cmap = 'Blues', fmt = '.2%')
ax.set_title('Percentage denial by race and sex')
plt.show()



'''
7- Visualization of denials across different counties
'''

request = 'https://raw.githubusercontent.com/plotly/datasets/master/laucnty16.csv'
geo_data = urlopen(request, context=ssl.create_default_context(cafile=certifi.where()))

df_loan = pd.read_csv('combined_ri_data.csv')
df_geo = pd.read_csv(geo_data)
df_geo['County FIPS Code'] = df_geo['County FIPS Code'].apply(lambda x: str(x).zfill(3))
split_df_geo = df_geo['County Name/State Abbreviation'].str.split(',', expand=True)
split_df_geo.rename(columns={0: "County Name", 1: "State"}, inplace=True)
df_geo = pd.concat([split_df_geo, df_geo[['County FIPS Code']]], axis=1)
df_geo = df_geo.apply(lambda x: x.str.strip())
df_geo = df_geo[df_geo["State"] == "RI"]
df_geo = df_geo[["County Name", "County FIPS Code"]]
df_merged = pd.merge(df_loan, df_geo, how="left", left_on="county_name", right_on="County Name")

request = 'https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json'
geo_data = urlopen(request, context=ssl.create_default_context(cafile=certifi.where()))
counties = json.load(geo_data)


df_merged = df_merged[df_merged['property_type_name']== 'One-to-four family dwelling (other than manufactured housing)']
#limit to co_applicant_race == 'No co_applicant' 
df_merged = df_merged[df_merged['co_applicant_ethnicity_name'] == 'No co-applicant']
df_merged['is_denial'] = (df_merged['action_taken_name'] == 'Application denied by financial institution')

df_merged['is_denial'] = (df_merged['action_taken_name'] == 'Application denied by financial institution')
df_merged = df_merged[df_merged['County FIPS Code'].notnull()]
values = df_merged['is_denial'].tolist()
fips = df_merged['County FIPS Code'].tolist()

df = df_merged[['is_denial', 'County FIPS Code']]
df = df.groupby(['County FIPS Code']).mean()

values = df['is_denial']
fips = df.index.values
fips = ['44' + str(x) for x in fips]

fig = ff.create_choropleth(fips=fips,\
                        values=values,\
                        scope=['Rhode Island'],\
                        title='Denial Rates by County',\
                        legend_title='Percentage of Mortgage Applications Which Are Denied',\
                        show_hover = True
                        )
fig.show()



