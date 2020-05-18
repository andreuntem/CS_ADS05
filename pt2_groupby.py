# Part 2: GROUP BY


def freq_risk_per_violation():
    """
    Find out the distribution of the risk exposure of all the violations reported in the database
    The first column of the result should 'risk_category' and the second column the count.
    :return: a string representing the SQL query
    :rtype: str
    """
    query = '''
    SELECT risk_category, COUNT (date)
    FROM violations
    GROUP BY risk_category
    '''
    return query


def freq_risk_per_violation_water():
    """
    Find out the distribution of the risk exposure of all the violations reported in the database
    that are *water related*. Sort them by frequency from high to low.
    :return: a string representing the SQL query
    :rtype: str
    """
    query = '''
    SELECT risk_category, COUNT(date) as frequency
    FROM violations
    WHERE
        description like '%water%'
    GROUP BY risk_category
    ORDER BY frequency DESC
    '''
    return query


def frequency_of_inspections_types():
    """
    What types of inspections does the authorities conduct and how often do they occur in general.
    Calculate the distribution of different types of inspections with their frequency (type, frequency)
    based on inspections records. Sort them in ascending order based on frequency.
    :return: a string representing the SQL query
    :rtype: str
    """
    query = '''
    SELECT type, COUNT(date) as frequency
    FROM inspections
    GROUP BY type
    ORDER BY frequency ASC
    '''
    return query


def avg_score_by_inspection_type():
    """
    What is the average score given to restaurants based on the type of inspection?
    Based on the results, identify the types of inspections that are not scored (NULL)
    and remove those categories from the resultset. The 'average_score' should be rounded
    to one decimal. Sort the results in ascending order based on the average score.
    Hint: use the function ROUND(score, 1)
    :return: a string representing the SQL query
    :rtype: str
    """
    query = '''
    SELECT type, round(AVG(Score),1) as average_score
    FROM inspections
    WHERE
        inspections.type = 'New Ownership' OR
        inspections.type = 'Reinspection/Followup' OR
        inspections.type = 'Routine - Unscheduled'
    GROUP BY type
    ORDER BY average_score ASC
    '''
    return query


def owner_per_restaurant_count():
    """
    Find the restaurant owners (owner_name) that own one or multiple restaurants in the city
    with the number of restaurants (num_restaurants) they own.
    Find the first top 10 owners ordered by descending order using the number of restaurants.
    :return: a string representing the SQL query
    :rtype: str
    """
    query = '''
    SELECT owner_name, COUNT (name) AS num_restaurants
    FROM businesses
    GROUP BY owner_name
    ORDER BY num_restaurants DESC
    LIMIT 10
    '''
    return query
