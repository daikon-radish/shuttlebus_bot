from telegram.ext import *
from datetime import datetime

WeekDayCondoTime = [600,620,640,700,720,740,800,820,840,900,930,1000,1700,1730,1800,1820,1840,1900,1930,2000,2030]
WeekDayMrtTime = [610,630,650,710,730,750,810,830,850,915,945,1710,1740,1810,1830,1850,1915,1945,2015,2045]
SaturdayCondoTime = [700,720,740,800,820,840,900,930,1000,1700,1730,1800,1820,1840,1900,1930,2000,2030]
SaturdayMrtTime = [710,730,750,810,830,850,915,945,1710,1740,1810,1830,1850,1915,1945,2015,2045]
SundayCondoTime = [930,1000,1030,1100,1130,1200,1230,1300,1330]
SundayMrtTime = [945,1015,1045,1115,1145,1215,1245,1315]

time_difference_list = []

def time():
    now = datetime.now()
    current_time = int((now.strftime("%H%M")))
    return current_time

def day():
    now = datetime.now()
    day = now.weekday()
    return day

def main_calculation_condo(final_time, final_day):
    time_difference_list.clear()
    if final_day <= 4: #0, 1, 2, 3, 4
        bus_schedule = WeekDayCondoTime
    elif final_day == 5:
        bus_schedule = SaturdayCondoTime
    elif final_day == 6:
        bus_schedule = SundayCondoTime

    for item in bus_schedule:
        if (item - final_time)>=0:
            time_difference_list.append(item - final_time) #to-do: if time is too short recommend SBS instead
    
    if final_time > bus_schedule[-1]:
        response = ('No more shuttlebus today!')
    else:
        response = ('The time is ' +str(final_time) + ' now and the next bus is coming to Watercolours EC at ' +str(final_time + time_difference_list[0]))
    return response



def main_calculation_MRT(final_time, final_day):
    time_difference_list.clear()
    if final_day <= 4: #0, 1, 2, 3, 4
        bus_schedule = WeekDayMrtTime
    elif final_day == 5:
        bus_schedule = SaturdayMrtTime
    elif final_day == 6:
        bus_schedule = SundayMrtTime

    for item in bus_schedule:
        if (item-final_time)>=0:
            time_difference_list.append(item-final_time)
    
    if final_time > bus_schedule[-1]:
        response = ('No more shuttlebus today!')
    else:
        response = ('The time is ' +str(final_time) + ' now and the next bus is coming to the MRT at ' +str(final_time + time_difference_list[0]))
    return response


def condo_command(update, context):
    CondoTime = time()
    CondoDay = day()
    Reply = main_calculation_condo(CondoTime, CondoDay)
    update.message.reply_text(Reply)
    
def mrt_command(update, context):
    MrtTime = time()
    MrtDay = day()
    Reply = main_calculation_MRT(MrtTime, MrtDay)
    update.message.reply_text(Reply)

def help_command(update, context):
    update.message.reply_text("If you are at condo now, type /condo , If you are at MRT now, type /mrt")

def start_command(update, context):
    update.message.reply_text("If you are at condo now, type /condo , If you are at MRT now, type /mrt")

def main():
    updater = Updater("1869077796:AAHaySD04H1DPqhFhPQcTvhdUWIwLad4E2w")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command)) #command handler is only for "/" kinda stuff
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("condo", condo_command))
    dp.add_handler(CommandHandler("mrt", mrt_command))
    updater.start_polling()
    updater.idle()


print("Bot started... ")
main()
