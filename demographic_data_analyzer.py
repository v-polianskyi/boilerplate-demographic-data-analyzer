import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
  
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series([
      df.race.str.contains("White").sum(),
      df.race.str.contains("Black").sum(),
      df.race.str.contains("Asian-Pac-Islander").sum(),
      df.race.str.contains("Amer-Indian-Eskimo").sum(),
      df.race.str.contains("Other").sum()], 
                           index=df.race.unique())

    # What is the average age of men?
    average_age_men = round(df.loc[df.sex=='Male'].age.mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df.loc[df.education=='Bachelors'])*100/len(df),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(df.loc[df.education.isin(['Bachelors','Masters','Doctorate'])])
    lower_education = len(df)-higher_education

    # percentage with salary >50K
    higher_education_rich = round(len(df.loc[(df.education.isin(['Bachelors','Masters','Doctorate'])) & (df.salary=='>50K')])*100/higher_education,1)
    lower_education_rich = round(len(df.loc[(~df.education.isin(['Bachelors','Masters','Doctorate'])) & (df.salary=='>50K')])*100/lower_education,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df.loc[(df['hours-per-week']==1) & (df.salary=='>50K')])

    rich_percentage = num_min_workers*100/len(df.loc[df['hours-per-week']==1])

    # What country has the highest percentage of people that earn >50K?
    result = {}
    for country in df['native-country'].unique():
      number = len(df.loc[(df.salary=='>50K')&(df['native-country']==country)])
      percent = round(number*100/len(df.loc[df['native-country']==country]),1)
      result.update({country: percent})
  
    highest_earning_country = max(result, key = lambda k: result[k])
    highest_earning_country_percentage = max(result.values())

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[
      (df['native-country']=="India") &
      (df.salary==">50K") 
      ].occupation.mode().values

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
