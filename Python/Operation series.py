import pandas as pd
series = pd.Series([2, 4, 6,8])
squared= series**2
print(f"Squared Result:\n{squared}")
  #write a python code to calcaulate total sales for each product and percentage growth
  
import pandas as pd
data1={'product A':150, 'product B': 200, 'product c': 1200,}    
data2={'product A':30, 'product B': 50, 'product c': 40,}

series1=pd.Series(data1)
series2=pd.Series(data2)
total_sales= series1+series2
print(total_sales)
percentage_growth=((series2-series1)/series1)*100
print(percentage_growth)