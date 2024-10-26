import cianparser

import time
import csv

######################################################################################

location_list = ['Москва', 'Москва и МО']
room = range(1, 5)

######################################################################################

for loc in location_list:
    for i in room:
        for j in range(1, 20):

            parser = cianparser.CianParser(location=loc)

            data = parser.get_flats(
                deal_type="sale", rooms=(i), 
                with_saving_csv=False,
                with_extra_data=True,
                additional_settings={"start_page":1, "end_page":54}
            )

            with open(f'parser/base/base_{j}_{loc}_{i}.csv', 'w', newline='', encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()

                for dict_item in data:
                    writer.writerow(dict_item)

            time.sleep(5)

# начал в 17:00