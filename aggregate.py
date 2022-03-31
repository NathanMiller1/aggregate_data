import pandas as pd


def inspect_data(df_to_inspect, title):
    # Inspect the data to make sure it is being read properly
    print(title)
    print(df_to_inspect.head())
    print(f'{len(df_to_inspect)} rows x {len(df_to_inspect.columns)} columns')
    print('')


# Make it so all columns of the output are shown
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 320)

# Read csv data into pandas dataframe
df = pd.read_csv('us_powerplants.csv')

# Inspect the data to make sure it is being read properly
inspect_data(df, 'original dataframe')

# Aggregate by state and primary_fuel
df_state_fuel = df.groupby(['state', 'primary_fuel']).agg({'capacity_mw': 'sum', 'generation_gwh': 'sum', 'capacity_factor': 'mean'})

# Inspect the state and primary_fuel aggregation
inspect_data(df_state_fuel, 'state and fuel aggregation')

# Aggregate by state only
df_state = df.groupby('state').agg({'capacity_mw': 'sum', 'generation_gwh': 'sum'})

# Edit state data column names
df_state = df_state.rename(columns={'capacity_mw': 'state_capacity', 'generation_gwh': 'state_generation'})

# Inspect the state only aggregation
inspect_data(df_state, 'state only aggregation')

# Save the merged state data
df_state.to_csv('state_data.csv')

# Add state only data to state and fuel data
df_merged = df_state_fuel.join(df_state, on='state')

# Add new columns for the percent of total capacity and generation each fuel type accounts for
df_merged['percent_state_capacity'] = df_merged['capacity_mw'] / df_merged['state_capacity']
df_merged['percent_state_generation'] = df_merged['generation_gwh'] / df_merged['state_generation']

# Inspect the merged dataframe
inspect_data(df_merged, 'merged data')

# Save the merged dataframe
df_merged.to_csv('state_fuel_data.csv')
