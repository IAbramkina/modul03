
from datetime import datetime

def get_days_from_today(in_date):
    try:
        in_date = datetime.strptime(in_date, "%Y-%m-%d").date()
        now = datetime.today().date()
        return (now - in_date).days
    except:
        print('Неправильний формат вхідних даних!')
    
    
print(f"Різниця: {get_days_from_today('2024.06-03')} днів")

