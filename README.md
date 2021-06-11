## 369game
It is a code that plays 369 games, a popular mini game in Korea.

The way to play this game is that several people take turns to say the number from 1, and if the number contains 3, 6, or 9, clap as much as the number.

---
### Code Description & process
First, write a code to input the last number of 369 game in 'number'. And I print '369 369, 369 369', the first start of the 369 game.
``` python
continent = ['AS', 'EU', 'AF', 'NA', 'SA', 'OC']
continent_alcohol = {'AS': 0, 'EU': 0, 'AF': 0, 'NA': 0, 'SA': 0, 'OC': 0}
for i in range(1, len(drinks_data)):
    continent_alcohol[drinks_data[i][5]] += float(drinks_data[i][4])
plt.bar(continent, continent_alcohol.values(), label='total litres')
plt.xlabel("Continent", fontsize=20)
plt.ylabel("Total Litres of Pure Alcohol", fontsize=20)
plt.title('Total Litres of Alcohol on Six Continents', fontsize=24)
plt.legend()
plt.show()
```
Second, create a function, 'claptime', to determine if the factor ' i '  has 3 or 6 or 9 and add 1 to the 'number_count' initialized to 0. 
If number_count is zero, output the number i, otherwise output the number_count as many 'clap!'
``` python
def claptime(i):
    number_count = 0
    a = str(i)
    for x in a:
        if x in '369':
            number_count += 1
    if number_count == 0:
        print(i)
    else:
        print('clap!' * number_count)
```
Finally, put the numbers from 1 to 'number' in the factor 'i'.
``` python
for j in range(1, int(number)+1):
    claptime(j)
```
### Execution Result

![image](https://user-images.githubusercontent.com/79324847/109376449-da5a1200-7907-11eb-81b9-e57d8a5c6c3a.png)

---

Thank you for watching my '369 game' code.
