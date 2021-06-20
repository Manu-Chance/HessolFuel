import csv
import datetime as dt
import requests
import bs4
import time

'''
with open('fuelprices.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)


	with open('new_file.csv', 'w') as new_file:
		csv_writer = csv.writer(new_file)


		for line in csv_reader:
			csv_writer.writerow(line)
'''
def new_entry():
	current_date = str(dt.datetime.now().date())
	#print(current_date)

	current_time = str(dt.datetime.now().time())[:8]
	#print(current_time)
	
	current_page = requests.get('https://www.benzinpreis-aktuell.de/tanken-hessol-tankstelle-bad-vilbel-61118-9e45.html')
	pageSoup = bs4.BeautifulSoup(current_page.text, 'html.parser')
	relevant_info = pageSoup.findAll('div', {'class': 'div-2'})

	current_petrol = str(relevant_info[0].getText())[:-1].replace(',', '.')
	#print(current_petrol)

	current_diesel = str(relevant_info[2].getText())[:-1].replace(',', '.')
	#print(current_diesel)

	with open('fuelprices.csv', 'a+', newline='') as new_file:
		csv_writer = csv.writer(new_file)

		line = [current_date, current_time, current_petrol, current_diesel]
		csv_writer.writerow(line)


def logger(entry_count):
	print("\n\n[GENERATING ENTRY]")
	print("Entry Number:> " + str(entry_count) + '\n\n')
	#print('Current Time:> ' + str(dt.datetime.now().time())[:8])
	new_entry()
	time.sleep(10) # change to 600 seconds for 10 min intervals
	entry_count += 1
	logger(entry_count)


def starter():
	print('Current Time:> ' + str(dt.datetime.now().time())[:8])

	while True:
		time.sleep(0.5)
		if str(dt.datetime.now().time())[:8] == '16:00:00':
			print("[EXECUTING]")
			break

	logger(0)


def main():
	print("[INITIALIZING]")
	input("Press enter to launch")
	starter()


if __name__ == '__main__':
	main()