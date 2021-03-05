## 369game
It is a code that plays 369 games, a popular mini game in Korea.

The way to play this game is that several people take turns to say the number from 1, and if the number contains 3, 6, or 9, clap as much as the number.

---
### Code Description & process
First, write a code to input the last number of 369 game in 'number'. And I print '369 369, 369 369', the first start of the 369 game.

'''python
number = input('Please input an end number:')
print('369 369, 369 369 !!')
'''

Second, create a function, 'claptime', to determine if the factor ' i '  has 3 or 6 or 9 and add 1 to the 'number_count' initialized to 0. 
If number_count is zero, output the number i, otherwise output the number_count as many 'clap!'

![image](https://user-images.githubusercontent.com/79324847/109376406-92d38600-7907-11eb-9fd6-b81ece8abd91.png)

Finally, put the numbers from 1 to 'number' in the factor 'i'.

![image](https://user-images.githubusercontent.com/79324847/109376461-f067d280-7907-11eb-855e-4b3509a08c42.png)

### Execution Result

![image](https://user-images.githubusercontent.com/79324847/109376449-da5a1200-7907-11eb-81b9-e57d8a5c6c3a.png)

---

Thank you for watching my '369 game' code.
