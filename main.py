from sqlalchemy import create_engine
import pandas
import matplotlib.pyplot as plt
import plotly.express as px

engine = create_engine("postgresql://postgres:ym09280601@192.168.0.8:5432/postgres",encoding='utf-8')

try:
    conn = engine.connect()

    print("연결성공")
except Exception as e :
    print("오류")


sql = "select avrtemp, updated,absvibr from meas"
df = pandas.read_sql_query(sql,engine)
df = pandas.DataFrame(df)
plt.plot(df.get('updated'),df.get('absvibr'),'r',label = 'impact',linewidth=1)
plt.plot(df.get('updated'),df.get('avrtemp'),'b',label='temp')


plt.legend(loc='best')
plt.show()


fig = px.line(df,x=df.get('updated'),y=[df.get('avrtemp'),df.get('absvibr')])

fig.show()
