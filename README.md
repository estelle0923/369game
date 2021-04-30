## 369game
It is a code that plays 369 games, a popular mini game in Korea.

The way to play this game is that several people take turns to say the number from 1, and if the number contains 3, 6, or 9, clap as much as the number.

---
### Code Description & process
First, write a code to input the last number of 369 game in 'number'. And I print '369 369, 369 369', the first start of the 369 game.
``` python
drinks_data = list(drinks_data)
drinks_data.sort(key=lambda x: float(x[1]))
drinks_data = np.array(drinks_data)
country_top = []
for i in range(-5, 0):
    country_top.append(drinks_data[i, 0])
top5 = []
for j in range(-5, 0):
    top5.append(float(drinks_data[j, 1]))
plt.bar(country_top, top5, color='gold', label='beer [L]')
plt.xlabel("Country", fontsize=20)
plt.ylabel("Beer serving", fontsize=20)
plt.title('Top 5 countries with high beer servings', fontsize=24)
plt.ylim(0, 400)
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
