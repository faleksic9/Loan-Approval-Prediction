# Data Spec
This is where you will be describing your data spec comprehensively. Please refer to the handout for a couple of examples of good data specs.

You will also need to provide a sample of your data in this directory. Please delete the example `sample.db` and replace it with your own data sample. ***Your sample does not necessarily have to be in the `.db` format; feel free to use `.json`, `.csv`, or any other data format that you are most comfortable with***.

Our dataset contains 224,325 records and 78 attributes. 
1: Agency_code
  Type of data that will be used for the representation.
    Integer which corresponds to a classification. These may need to be turned into dummy variables in the analysis step. 
  Default value
    The default value is unknown because all entries have a value.
  Range of value.
    1-9 integers- each integer indicates an agency that is providing the data
  Simplified analysis of the distribution of values
  [Screen-Shot-2022-03-03-at-8-31-04-PM.png](https://postimg.cc/p5xwBd6s)
    Agencies 7,9 seem to be the most common, while 1,2 make up a smaller proportion of the data. 
  Is this an identifier?
    No
  Are these values unique?
    No
  Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how?
    SInce this value is not unique, it cannot be used to detect duplicate records
  Is this a required value?
    This value is required, and there are no datapoints without it.
  Do you plan to use this attribute/feature in the analysis? If so, how?
    This value may hold significance for analysis due to the fact that it indicates which agency the loan was provided by. It would be used through dummy variables     if used. 
  Does this feature include potentially sensitive information? If so, how do you suggest handling such issues?
    This feature does not contain sensitive information. 



2:  Loan_purpose
  Type of data that will be used for the representation.
    Integer which corresponds to a classification. These may need to be turned into dummy variables in the analysis step. 
  Default value
    The default value is unknown because all entries have a value.
  Range of value. 
    1-3 corresponds to loan_purpose_name (1 = Home Purchase, 2 = Home Improvement, 3 = Refinancing)
  Simplified analysis of the distribution of values
  [Screen-Shot-2022-03-03-at-8-38-00-PM.png](https://postimg.cc/Thp7Zgrn)
    Mostly home purchase or refinancing loans
  Is this an identifier?- No.
  Are these values unique?- No.
  Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how?
  No, because multiple records could all have the same loan_purpose.
  Is this a required value?
  I am not sure if it is required in data collection but all records contain this variable.
  Do you plan to use this attribute/feature in the analysis? If so, how?
  Maybe. If we are only looking at loans with one purpose, this feature will not be important, however if we are analyzing loans across different purposes, this feature will be important for analysis. 
  Does this feature include potentially sensitive information? If so, how do you suggest handling such issues?
  This feature does not contain sensitive information. 
  
3: loan_type_name
    Data Type—string 
    Default Value—empty string
    Range of Values—four possible loan types are represented: 
      conventional
      va-guaranteed
      fha-insured
      fsa/rhs-guaranteed
    Distribution of Values:
      conventional—162,416 records associated with this loan type label
      fha-insured—49,334 records associated with this loan type label
      va-guaranteed—11,100 records associated with this loan type label
      fsa/rhs-guaranteed—1,475 records associated with this loan type label
    This is not an identifier nor are the values unique
    This value will not be used to identify duplicate records
    This is a required value since these are loan applications and each application is classified on its type
    We will want to use this feature to see if there are differences in approval rates or other actions taken depending on the loan type itself
    This field by itself does not contain sensitive information
    
4: applicant_ethnicity_name
    Data Type—string 
    Default Value—empty string
    Range of Values—four possible ethnicity values are represented: 
      not hispanic or latino
      information not provided by applicant in mail, internet, or telephone application,
      not applicable
      hispanic or latino
    Distribution of Values:
      not hispanic or latino–167,735 records associated with this ethnicity label
      not applicable–23,569 records associated with this ethnicity label                                                                        
      information not provided by applicant in mail, Internet, or telephone application–18,351 records associated with this ethnicity label
      hispanic or latino–14,670 records associated with this ethnicity label
      This is not an identifier nor are the values unique
      This value will not be used to identify duplicate records
      This loan applicants themselves did not have to provide this information but each data point in our dataset does have an ethnicity name associated
      We will want to use this feature to see if ethnicity impacts loan application approval
      This field contains somewhat sensitive information since it concerns the identity of an individual. However, since all this data has been anonymized by the government we have no way of mapping particular individuals to their private information


5: property_type
Data Type—integer
Default Value— Not sure as all entries have this value
Range of Values— each corresponds to a property_type_name
  1: One-to-four family dwelling (other than manufactured housing)
  2: Manufactured Housing
  3: Multifamily dwelling
Distribution of Values:
[Screen-Shot-2022-03-03-at-8-41-21-PM.png](https://postimg.cc/jCwc8KbX)
  Almost all loans are for one-four family dwellings
This is not an identifier nor are the values unique
This value is also not be used to identify duplicate records
This is a required value. 
We will most likely look at approval rates for one-to-four family dwellings and will need to use this variable to filter our data, not as a variable in our analysis. 
This field by itself does not contain sensitive information. 

6: loan_amount_000s
    Data Type—integer
    Default Value— Not sure as all entries have this value
    Range of Values— 1- 90080
    Distribution of Values:
      [Screen-Shot-2022-03-03-at-8-43-01-PM.png](https://postimg.cc/30mg38rQ)
      Skewed distribution with a long right tail
    This is not an identifier nor are the values unique
    This value could be used in combination with other values such as the county, race, action_taken, and respondent_id to identify specific loans. 
    This is a required value. 
    This variable is most likely very important in determining the likelihood of loan approvals and will definitely be important to our analysis. 
    This field contains sensitive information which could reveal the financial standing of borrowers. However, this dataset does not indicate the personal identity     of any people, so this field is not completely sensitive material. 
    
7. hud_median_family_income
    Data Type—float64 
    Default Value—0
    Range of Values—71,100-74,500: 
    Distribution of Values:
      Mean:  73, 019.22
      Min: 71,100.00
      25% Quartile: 72,200.00
      50% Quartile: 73,100.00
      75% Quartile:  74,400.00
       Max: 74, 500.00
    This is not an identifier nor are the values unique
    This value will not be used to identify duplicate records
    This is not a required field
    We will want to use this feature to see if income impacts loan application approval



8. action_taken_name
    Data Type—string 
    Default Value—empty string
    Range of Values—seven possible values are represented: 
      application denied by financial institution
      application withdrawn by applicant
      loan originated
      preapproval request approved but not accepted
      loan purchased by the institution
      file closed for incompleteness
      application approved but not accepted
      preapproval request denied by financial institution
    Distribution of Values:
      loan originated–123,016 records associated with this action label
      application denied by financial institution–33,587 records associated with this action label
      loan purchased by the institution–31,815 records associated with this action label
      application withdrawn by applicant–20,878 records associated with this action label
      file closed for incompleteness--8,946 records associated with this action label
      application approved but not accepted–6,064 records associated with this action label
      preapproval request denied by financial institution–12 records associated with this action label
      preapproval request approved but not accepted–7 records associated with this action label
    This is not an identifier nor are the values unique
    This value will not be used to identify duplicate records
    This is a required field since it classifies what happened to the loan application 
    This will actually be our target variable in our analysis 
    This field does not contain sensitive information
9. rate_spread
    Data Type—float64 
    Default Value—0
    Range of Values—1.5-14: 
    Distribution of Values:
      Mean: 2.78
      Min: 1.5
      25% Quartile: 1.62
      50% Quartile: 1.87
      75% Quartile:  3.68
      Max: 14
This is not an identifier nor are the values unique
This value will not be used to identify duplicate records
This is not a required field
We are not sure if we would use this variable in our analysis



10. denial_reason_name_1/denial_reason_name_2/denial_reason_name_3
      Data Type—string 
      Default Value—empty string
      Range of Values—nine possible denial reason values are represented: 
          other
          debt-to-income ratio
          credit history
          collateral
          credit application incomplete
          insufficient cash (downpayment, closing costs)
          unverifiable information
          employment history      
          mortgage insurance denied
      Distribution of Values:
          credit history–5,658 records associated with this label
          debt-to-income ratio–5,011 records associated with this label
          collateral–4,918 records associated with this label
          credit application incomplete–2,349 records associated with this label
          other–1,994 records associated with this label
          unverifiable information–867 records associated with this label
          insufficient cash (downpayment, closing costs)–558 records associated with this label
          employment history–263 records associated with this label
          mortgage insurance denied–16 records associated with this label
      This is not an identifier nor are the values unique
      This value will not be used to identify duplicate records
      This is not required field
      We will want to use this feature to see why applications are being denied 
      This field does not contain sensitive information




