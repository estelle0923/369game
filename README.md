## 369game
It is a code that plays 369 games, a popular mini game in Korea.

The way to play this game is that several people take turns to say the number from 1, and if the number contains 3, 6, or 9, clap as much as the number.

---
### Code Description & process
First, write a code to input the last number of 369 game in 'number'. And I print '369 369, 369 369', the first start of the 369 game.
``` python
for i in range(len(drinks_data)):
    if drinks_data[i, 0] == 'Russian Federation':
        a = float(drinks_data[i, 4])
    elif drinks_data[i, 0] == 'Canada':
        b = float(drinks_data[i, 4])
    elif drinks_data[i, 0] == 'Mongolia':
        c = float(drinks_data[i, 4])
    elif drinks_data[i, 0] == 'Libya':
        d = float(drinks_data[i, 4])
    elif drinks_data[i, 0] == 'Saudi Arabia':
        e = float(drinks_data[i, 4])
    elif drinks_data[i, 0] == 'Iraq':
        f = float(drinks_data[i, 4])

ax1 = plt.subplot(121)
ax1.bar(['Russia', 'Canada', 'Mongolia'], [a, b, c],
        color=['darkblue', 'royalblue', 'cornflowerblue'], alpha=0.5, label='total litres')
plt.xlabel('Country',  fontsize=20)
plt.ylabel('Total Alcohol', fontsize=20)
plt.title('Total of Pure Alcohol in Cold Country',  fontsize=24)
plt.legend()

ax2 = plt.subplot(122)
ax2.bar(['Libya', 'Saudi Arabia', 'Iraq'], [d, e, f],
        color='red', alpha=0.5, label='total litres')
plt.xlabel('Country',  fontsize=20)
plt.ylabel('Total Alcohol', fontsize=20)
plt.ylim(0, 12)
plt.title('Total of Pure Alcohol in Hot Country',  fontsize=24)
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
