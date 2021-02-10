from mypack.data_generator import User
from mypack.tables import *
from mypack.config.utils import config_parser


users = 500
config_path = os.path.dirname(mypack.__file__ )+ '/config/database.ini'


def main(config_path = config_path):
    params = config_parser(config_path)
    
    db_url = f"postgresql://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['database']}"
    engine = create_engine(db_url, echo=False)
    Session_db = sessionmaker(bind=engine)
    db_session = Session_db()

    for company_id in range(users):
        user = User(company_id)
        company_x = Company(company_id = user.company_id, company_size= user.company_size, industry=user.industry)
        subscription_x = Subscription(company_id = user.company_id, subscription_amount = user.subscription_fee)

        db_session.add_all([company_x, subscription_x])
        db_session.commit()

        for month in range(1, 13):
            user_sessions_timestamp = user.gen_rand_sessions(month)
            if not user_sessions_timestamp: break

            user_sessions = [Session(company_id = user.company_id, created_at = s) for s in user_sessions_timestamp]
            
            db_session.add_all(user_sessions)
            db_session.commit()





if __name__ == "__main__":
    main()