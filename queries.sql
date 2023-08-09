-- удаляем таблицы, если есть
drop table if exists vacancies_db.public.vacancies;
drop table if exists vacancies_db.public.employers;
drop table if exists vacancies_db.public.selected;

-- таблица работодателей
create table public.employers (id int8 primary key,
					   name varchar(1000),
					   city varchar(100)
					  );

-- таблица вакансий
create table public.vacancies (id int8 primary key,
                                            employer_id int8,
                                           name varchar(1000),
                                           job_url varchar(1000),
                                           requirement varchar(4000),
                                           salary_from int4,
                                           salary_to int4,
                                           currency varchar(10),
                                           CONSTRAINT fk_vacancies_employers FOREIGN KEY (employer_id)
                                            REFERENCES public.employers (id) MATCH SIMPLE
                                            ON UPDATE CASCADE
                                            ON DELETE CASCADE
                                          );

-- таблица с интересующими нас компаниями
create table public.selected (id int8 primary key,
					   name varchar(1000)
					  );


insert into  public.selected (id, name)
values (3529,'СБЕР'),(3776,'МТС'),(1272486,'СберМаркет'),(4934,'билайн'),(78638,'Тинькофф'),(882,'1С'),
        (3127,'Мегафон'),(3388,'Газпромбанк'),(154,'Диасофт'),(4620,'ГЛОРИЯ ДЖИНС');