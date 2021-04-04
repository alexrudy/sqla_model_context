from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqla_model_context import ModelRelativeContextManager

Base = declarative_base()


class Manager(Base):
    __tablename__ = "manager"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    manager_id = Column(Integer, ForeignKey("manager.id"))
    manager = relationship(Manager)


def main():

    uri = "sqlite:///:memory:"
    engine = create_engine(uri)
    Base.metadata.create_all(engine)

    ctx = ModelRelativeContextManager(Employee, "manager", enforce="LOG")

    s = Manager(name="Darren")
    m = Manager(name="Cato")

    with ctx.push(s):
        e = Employee(name="Bernard", manager=m)

    assert e.manager == m

    with ctx.push(s):
        e2 = Employee(name="Edward")

    assert e2.manager == s


if __name__ == "__main__":
    main()
