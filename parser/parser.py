import cianparser

import time
import os
import shutil

######################################################################################

def find_txt_files(directory):
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            shutil.move(file, f"parser/gathering_base/{file}")


######################################################################################

location_list = ['Москва', 'Москва и МО']
room = range(1, 5)

######################################################################################

for loc in location_list:
    for i in room:

        parser = cianparser.CianParser(location=loc)

        data = parser.get_flats(
            deal_type="sale", rooms=(i), 
            with_saving_csv=True, 
            additional_settings={"start_page":1, "end_page":54}
        )

        find_txt_files(os.getcwd())

        time.sleep(5)