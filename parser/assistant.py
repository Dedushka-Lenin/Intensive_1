# import os

# def delete_files_in_folder(directory):
#     print(directory)

#     for file in os.listdir(directory):
#         if file.endswith(".csv"):
#             os.remove(file)


# while(True):
#     print('\n-------------------------------------------------------------------------------------\n')
#     command = input('Введите команду: ').lower()

#     match command:
#         case 'стереть мусор':
#             delete_files_in_folder('parser/gathering_base')
#             # delete_files_in_folder(os.getcwd())

#         case 'стереть базу':
#             delete_files_in_folder('parser/base')

#         case 'мусор в базу':
#             break
        
#         case 'Выход':
#             break

#         case _:
#             print('\nОшибка')Ы



# import glob
# import pandas as pd

# path = 'parser\gathering_base'
# filenames = glob.glob(path + "/*.csv")

# dfs = []

# for filename in filenames:
#     dfs.append(pd.read_csv(filename))


# big_frame = pd.concat(dfs, ignore_index=True)
# big_frame.to_csv("parser/base/base.csv", index=False)

import os

os.system('C:\Users\Игорь.А\OneDrive\Документы\GitHub\Intensive_1\parser\gathering_base copy *.csv base.csv')