## 369game
It is a code that plays 369 games, a popular mini game in Korea.

The way to play this game is that several people take turns to say the number from 1, and if the number contains 3, 6, or 9, clap as much as the number.

---
### Code Description & process
First, write a code to input the last number of 369 game in 'number'. And I print '369 369, 369 369', the first start of the 369 game.
``` python
folder_names = os.listdir('output')
for folder_name in folder_names:
    if not os.path.exists('resized/' + folder_name):
        os.makedirs('resized/' + folder_name)
    output_folder = folder_name
    folder_name = 'output/{}'.format(folder_name)
    file_names = os.listdir(folder_name)
    for file_name in file_names:
        output_name = '{}/{}'.format(output_folder, file_name)
        file_name = '{}/{}'.format(folder_name, file_name)
        image = cv2.imread(file_name, cv2.IMREAD_COLOR)
        resized_image = cv2.resize(image, dsize=(256, 256))
        cv2.imwrite('resized/' + output_name, resized_image)
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
