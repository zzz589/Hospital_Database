\c hospital;

create table department(
department_id  varchar(64) primary key NOT NULL,
department_director  varchar(64)
);


create table doctor(
doctor_id varchar(64) primary key NOT NULL,
doctor_name varchar(64),
doctor_sex varchar(2) default '男'  check (doctor_sex in ('男', '女')) 
);

create table registered_user (
registered_user_id varchar(64) primary key NOT NULL,
user_name varchar(64),
user_sex varchar(2) default '男'  check (user_sex in ('男', '女'))
);

create table doctor_visits (
doctor_visits_id varchar(64) primary key NOT NULL,
doctor_id varchar(64),
registered_user_id varchar(64) ,
user_situation varchar(64) ,
foreign key(registered_user_id) references registered_user
);

create table administer(
admin varchar(64) primary key NOT NULL,
password varchar(64)
);


create table registration (
registration_id varchar(64) primary key NOT NULL,
doctor_visits_id varchar(64),
foreign key(doctor_visits_id) references doctor_visits
);

