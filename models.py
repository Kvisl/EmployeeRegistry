from sqlalchemy import Column, String, Date, Integer, Index
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    gender= Column(String, nullable=False)

    __table_args__ = (
        Index('ix_employee_gender_full_name', 'gender', 'full_name'),
    )

    def __init__(self, full_name, dob, gender):
        self.full_name = full_name
        self.dob = dob
        self.gender = gender
