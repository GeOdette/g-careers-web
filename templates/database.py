from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://jhjvlkigeuge1p4kd3pn:pscale_pw_uAzPWni0JQDYoUpp4Ze51X8G4r1Zpld23UXtWCVqNov@us-east.connect.psdb.cloud/mycareers?charset=utf8mb4"
engine = create_engine(db_connection_string, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})


