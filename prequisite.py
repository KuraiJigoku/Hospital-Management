import mysqlc
import management.values as values
con,cur=mysqlc.connection()
values.audoctor()
values.aupatient()
