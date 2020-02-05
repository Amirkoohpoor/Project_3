#import dependencies
import csv
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# imported Column, ForeignKey, Integer, and String to define our database table columns.
from sqlalchemy import Column, ForeignKey, Integer, String, Float

# constructs a base class for the declarative class definition and assigns it to the Base variable.
Base = declarative_base()

#create the class Real_Estate and extend it from the Base Class
class Real_estate(Base):
   __tablename__ = 'real_estate'

   Mls_Number = Column(String(9), primary_key=True)
   Lat = Column(Float, nullable=False)
   Long = Column(Float, nullable=False)
   Street = Column(String(100), nullable=False)
   City = Column(String(10),nullable=False)
   Province = Column(String(10),nullable=False)
   Postal_Code = Column(String(10),nullable=False)
   Age = Column(String(10))
   Listed_By = Column(String(50))
   Lot_Size = Column(String(50))
   Size = Column(String(50))
   Style = Column(String(50))
   Taxes = Column(String(50))
   Type = Column(String(25))
   Walk_Score = Column(Integer)
   Neighbourhood = Column(String(20))
   Price = Column(Integer)
   Business_Type = Column(String(20))
   Property_Type = Column(String(20))
   Zoning = Column(String(20))
   Photo_file = Column(String(250))
   Photo_url = Column(String(250))
   Date_posted_MLS = Column(String(15))


# create an instance of our create engine class which points to the database 
engine = create_engine('sqlite:///toronto-real-estate.db')

# add the classes as new tables in the database created
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
session = DBSession()

# with open('merge_data.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file,delimiter=',')
#     next(csv_reader)
#     for row in csv_reader:
#         posting = Real_estate(Mls_Number=row[0],
#         Lat=float(row[1]),
#         Long=float(row[2]),
#         Street=row[3],
#         City = row[4],
#         Province = row[5],
#         Postal_Code = row[6],
#         Age = row[7],
#         Listed_By = row[8],
#         Lot_Size = row[9],
#         Size = row[10],
#         Style = row[11],
#         Taxes = row[12],
#         Type = row[13],
#         Walk_Score = int(row[14]),
#         Neighbourhood = row[15],
#         Price = int(row[16]),
#         Business_Type = row[17],
#         Property_Type = row[18],
#         Zoning = row[19],
#         Photo_file = row[20],
#         Photo_url = row[21],
#         Date_posted_MLS = row[22])
#         session.add(posting)
#         session.commit()



