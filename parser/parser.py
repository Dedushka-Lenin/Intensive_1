import cianparser

import time
import csv
import random

######################################################################################

location_list = ['Москва и МО', 'Москва']
room = range(1, 5)

######################################################################################

for c in range(1, 4):
    for loc in location_list:
        for i in room:
            for j in range(1, 54):
                    parser = cianparser.CianParser(location=loc)

                    data = parser.get_flats(
                        deal_type="sale", rooms=(i), 
                        with_saving_csv=False,
                        additional_settings={"start_page":j, "end_page":j}
                    )


                    if data:

                        try:
                            with open(f'parser/base/base_{c}_{loc}_{i}_{j}.csv', 'w', newline='', encoding="utf-8") as file:
                                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                                writer.writeheader()

                                for dict_item in data:
                                    writer.writerow(dict_item)
                        except:
                            print("Ошибка")

                    time.sleep(random.randint(5, 10))