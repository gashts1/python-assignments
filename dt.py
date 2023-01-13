from datetime import datetime
birthday = "1-May-12"
date_format = "%d-%B-%y"

parsed_date = datetime.strptime(birthday, date_format)
print(parsed_date)

date_str = parsed_date.strftime("%-m/%-d/%Y")
print(date_str)
