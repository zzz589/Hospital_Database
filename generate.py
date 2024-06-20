
import random
from app.sql import SQL_Server

sql=SQL_Server()

# Department
department_id_list = []
for k in range(5):
    statement = "("
    department_id = "'dept" + str(k) + "'"
    department_director = "'" + random.choice(['Dr. Smith', 'Dr. Johnson', 'Dr. Wang', 'Dr. Patel']) + "'"
    statement += department_id + ',' + department_director+')'
    print(statement)
    department_id_list.append(department_id)

    SF=sql.insertIntoTable('department',statement)





# Doctor
doctor_id_list = []
for k in range(10):
    statement = "("
    doctor_id = "'doc" + str(k) + "'"
    doctor_name = "'" + random.choice(['Dr. Lee', 'Dr. Chen', 'Dr. Gupta', 'Dr. Kim', 'Dr. Mi', 'Dr. Liu', 'Dr. Li', 'Dr. Ma']) + "'"
    doctor_sex = "'" + random.choice(['男', '女']) + "'"
    statement += doctor_id + ',' + doctor_name + ',' + doctor_sex + ')'
    print(statement)
    insertSQL = statement
    SF=sql.insertIntoTable('doctor',statement)
    doctor_id_list.append(doctor_id)


# Registered User
registered_user_id_list = []
for k in range(30):
    statement = "("
    registered_user_id = "'user" + str(k) + "'"
    user_name = "'" + random.choice(['John Doe', 'Jane Smith', 'Robert Johnson', 'Emily Wang', 'CC W', 'MCA', 'Jay John']) + "'"
    user_sex = "'" + random.choice(['男', '女']) + "'"

    statement += registered_user_id + ',' + user_name + ',' + user_sex + ')'
    print(statement)
    registered_user_id_list.append(registered_user_id)
    SF=sql.insertIntoTable('registered_user',statement)

# Doctor Visits
doctor_visits_id_list = []
for k in range(20):
    statement = "("
    doctor_visits_id = "'dv" + str(k) + "'"
    doctor_id = random.choice(doctor_id_list)
    registered_user_id = random.choice(registered_user_id_list)
    user_situation = "'" + random.choice(['Emergency', 'Routine Checkup', 'Follow-up']) + "'"
    statement += doctor_visits_id + ',' + doctor_id + ',' + registered_user_id + ',' + user_situation + ')'
    print(statement)

    SF = sql.insertIntoTable('doctor_visits', statement)

    doctor_visits_id_list.append(doctor_visits_id)


# Administer
admin_list = []
for k in range(5):
    statement = "("
    admin = "'admin" + str(k) + "'"
    password = "'password" + str(k) + "'"
    statement += admin + ',' + password + ')'
    print(statement)
    admin_list.append(admin)

    SF = sql.insertIntoTable('administer', statement)





# Registration
for k in range(20):
    statement = "("
    registration_id = "'reg" + str(k) + "'"


    doctor_visits_id = doctor_visits_id_list[k]
    statement += registration_id + ',' + doctor_visits_id + ')'
    print(statement)

    SF = sql.insertIntoTable('registration', statement)



