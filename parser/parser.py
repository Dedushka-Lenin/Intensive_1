import cianparser

import time
import csv
import ramdom

######################################################################################

location_list = ['Москва', 'Москва и МО']
room = range(1, 5)

######################################################################################


for loc in location_list:
    for i in room:
        for j in range(1, 54):
                parser = cianparser.CianParser(location=loc)

                data = parser.get_flats(
                    deal_type="sale", rooms=(i), 
                    with_saving_csv=False,
                    with_extra_data=True,
                    additional_settings={"start_page":j, "end_page":j}
                )

                with open(f'parser/base/base_{loc}_{i}_{j}.csv', 'w', newline='', encoding="utf-8") as file:
                    writer = csv.DictWriter(file, fieldnames=data[0].keys())
                    writer.writeheader()

                    for dict_item in data:
                        writer.writerow(dict_item)

                time.sleep(random.randint(5, 10))

# начал в 17:00