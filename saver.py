from nessusinterface import authenticate
from db import Session
from models import Report, Host, Vuln
from datetime import datetime

def main():
    nessus = authenticate()
    session = Session()

    for report in nessus.reports:
        if report.status != 'completed':
            continue

        if session.query(exists(), where(Report.uuid==report.uuid)).scalar():
            continue

        r = Report(
            name=report.name,
            uuid=report.uuid,
            time=datetime.fromtimestamp(report.timestamp)
        )
        session.add(r)

        for host in report.hosts:
            h = Host(
                hostname=host.hostname,
                info=host.info,
                low=host.low,
                med=host.med,
                high=host.high,
                crit=host.critical,
                cpe=host.cpe.replace('The remote operating system matched the following CPE\'s : \n\n  ', '')
            )

            h.report = r
            session.add(h)

        for vuln in report.vulns:
            v = Vuln(
                name=vuln.name,
                family=vuln.family,
                severity=vuln.severity,
                plugin=vuln.plugin_id,
            )
            v.report = r
            session.add(v)

    session.commit()




if __name__ == '__main__':
    main()
