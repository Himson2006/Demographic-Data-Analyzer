import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)
    

    # What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)
    total_bachelors = (df['education'] == 'Bachelors').sum()
    percentage_bachelors = ((total_bachelors/total_people)*100).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]
    high_50 = len(higher_education[higher_education['salary'] == ">50K"])
    lower_education = df[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]
    low_50 = len(lower_education[lower_education['salary'] == ">50K"])


    # percentage with salary >50K
    higher_education_rich = round((high_50/len(higher_education))*100, 1)
    lower_education_rich = round((low_50/len(lower_education))*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    min_50k = num_min_workers[num_min_workers['salary'] == '>50K']

    rich_percentage = round((len(min_50k)/len(num_min_workers))*100,1)

    # What country has the highest percentage of people that earn >50K?
    total_country_people = df['native-country'].value_counts()
    total_rich_people = df[df['salary'] == ">50K"]['native-country'].value_counts()
    highest_earning_country = (total_rich_people/total_country_people * 100).idxmax()
    highest_earning_country_percentage = round((total_rich_people/total_country_people * 100).max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    occupation_df = df[(df['native-country'] == 'India') & (df['salary'] == ">50K")]['occupation'].value_counts()
    top_IN_occupation = occupation_df.idxmax()

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
