from random import choices, randint, choice, random
import calendar
from dateutil.relativedelta import relativedelta
from datetime import datetime



class User(object):
    def __init__(self, company_id):
        self.company_id = company_id
        self.company_size = self.gen_company_size()
        self.subscription_fee = 19 if self.company_size == 'small' else 99
        self.industry = choice([1,2,3,4,5])

    def gen_company_size(self):
        population = ['small', 'big']
        weights = [0.7, 0.3]
        return choices(population, weights)[0]
    
    def gen_rand_session_number(self):
        if self.company_size == 'small' : return 5 + randint(-5,5)
        else: return 10 + randint(-10,10)

    def gen_rand_timestamp(self, month, year = 2020):
        start = datetime(year, month, 1, 00, 00, 00)
        end = start + relativedelta(months=1)
        return start + (end - start) * random()
    
    def gen_rand_sessions(self, month, year = 2020):
        sessions = []
        for session in range(self.gen_rand_session_number()):
            sessions.append(self.gen_rand_timestamp(month, year))
        return sessions