from datetime import datetime


def main():
    # print(countdown())
    return countdown()


def countdown():
    future_date = datetime.strptime('Apr 14 2023 20:30', '%b %d %Y %H:%M')
    # print(future_date)

    now_date = datetime.now()
    # print(now_date)

    count = int((future_date - now_date).total_seconds())
    days = count//86400
    hours = (count-days*86400)//3600
    minutes = (count-days*86400-hours*3600)//60
    seconds = count-days*86400-hours*3600-minutes*60
    print(days, hours, minutes, seconds)
    return days, hours, minutes, seconds
    # return f'{days} days {hours} hours {minutes} minutes {seconds} seconds until VIETNAM!!!'



if __name__ == '__main__':
    main()
