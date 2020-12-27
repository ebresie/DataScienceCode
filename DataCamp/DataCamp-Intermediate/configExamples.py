import matplotlib.pyplot as plt
year = [ 1950, 1970, 1990, 2010] 
pop = [2.519, 3.692, 5.263, 6.972] 

# add more data
year = [1800,1850,1900] + year
pop = [1.0, 1.262, 1.650] + pop
plt.plot(year, pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projection')
plt.yticks([0,2,4,6,8,10], ['0B','2B','4B','6B', '8B','10B'])
plt.show()