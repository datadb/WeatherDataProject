import re

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

@transformer
def transform(data, *args, **kwargs):

    new_cols=[]
    count = 0
    for column in data.columns:

        if any(char.isupper() for char in column): 
            column = camel_to_snake(column)
            count+=1
        new_cols.append(column)
    data.columns = new_cols
#    data.head()

    print("Rows with null datetime:", data['dt'].isna().sum())
    print("Rows with null average temperature:", data['average_temperature'].isna().sum())
    print("Rows with null average temperature uncertainty:", data['average_temperature_uncertainty'].isna().sum())
    print("Rows with null country:", data['country'].isna().sum())
    # print (data.dtypes)
    # data.head()
#   The dt. date attribute extracts the date part of the DateTime objects in a Pandas Series.
#   data['dt'] = data['dt'].dt.date
    # print (data.dtypes)
    return data


# @test
# def test_dts(output, *args):
#     assert output['dt'].isna().sum() == 0, 'There are rows with null datetime'

# @test
# def test_avg_temp(output, *args):
#     assert output['average_temperature'].isna().sum() == 0, 'There are rows with null average temperature'

# @test
# def test_avg_temp_uncertainty(output, *args):
#     assert output['average_temperature_uncertainty'].isna().sum() == 0, 'There are rows with null average temperature uncertainty'

# @test
# def test_country(output, *args):
#     assert output['country'].isna().sum() == 0, 'There are rows with null country'