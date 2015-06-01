from sqlalchemy import create_engine
from sqlalchemy import Column, DateTime, Integer, ForeignKey, String
from sqlalchemy.orm import backref, relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Report(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    uuid = Column(String)
    time = Column(DateTime)

    hosts = relationship('Host', backref='report')
    vulns = relationship('Vuln', backref='report')


class Host(Base):
    __tablename__ = 'hosts'
    id = Column(Integer, primary_key=True)
    hostname = Column(String)
    info = Column(Integer)
    low = Column(Integer)
    med = Column(Integer)
    high = Column(Integer)
    crit = Column(Integer)
    cpe = Column(String)

    report_id = Column(Integer, ForeignKey('reports.id'))

    @property
    def counts(self):
        return [self.info, self.low, self.med, self.high, self.crit]


class Vuln(Base):
    __tablename__ = 'vulns'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    family = Column(String)
    severity = Column(Integer)
    plugin = Column(Integer)
    hosts_affected = Column(Integer)

    report_id = Column(Integer, ForeignKey('reports.id'))
