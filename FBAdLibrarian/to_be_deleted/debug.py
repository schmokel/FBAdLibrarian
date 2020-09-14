def load_txt_to_list(list_name:str):
    out_list = []              
    with open(list_name, 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            #currentPlace = line[:-1]
            line = line.replace('\n', '')
            # add item to the list
            out_list.append(line)
        lines = [line for line in out_list if line is not '']
    return lines

import facebookScraper.helpers as helpers
url = load_txt_to_list(r"C:\Users\rasmu\Documents\Repositories\fbtest\temp\url_list_20200709092846.txt")
#url_list = helpers.clean_url(url, facebookAccesToken)



'''
out_list = []              
with open(r"C:\Users\rasmu\Documents\Repositories\fbscraperTest\temp\url_list_20200705205926.txt", 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        #currentPlace = line[:-1]

        # add item to the list
        out_list.append(line)
print(len(out_list))
'''
adid = load_txt_to_list(r"C:\Users\rasmu\Documents\Repositories\test2\temp\adid_list_20200708194054.txt")

print(len(url))
print(len(adid))

len(url) == len(adid)

for n in url:
    print(n)


folder = r"C:\Users\rasmu\Documents\Repositories\fbtest\temp"
files = os.listdir(folder)

adid_pattern = re.compile(r'adid_list_\d{14}\.txt$')
adid_file = max(filter(adid_pattern.search, files))

url_pattern = re.compile(r'url_list_\d{14}\.txt$')
url_file = max(filter(url_pattern.search, files))

a = 1
b = 1
try:
    if a == 1:
        print("a er lig 1")

        try:
            if b == 1:
                print("b er lige med 1")
                raise helpers.CSSClassError("Writing log at {}".format(ts))
            else:
                #raise Exception
                pass
                
        except:
            print('inner exception')
            raise Exception

except:
    print('ydre exception')

finally:
    print('finale statement')


