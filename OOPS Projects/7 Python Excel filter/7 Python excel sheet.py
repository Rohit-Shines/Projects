import pandas as pd
df = pd.read_csv('trails.csv',index_col=['OBJECTID', 'TRAIL_NAME','CONDITION','HIKING','BIKING','ATV'])

# print(df.head()) #print top 5 lines
#
# print(df.tail()) #print botoom 5 lines

status = df[(df['STATUS']=='ACTIVE') & df['INST_YEAR']>2000 & (df['LIGHT']=='Y') & (df['WALKING']=='Y')& (df['BIKING']=='Y')] #filtering only active status files
print(status)


# status.to_csv('StatusActive.csv')ff
