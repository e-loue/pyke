create table if not exists movie (
    id int not null auto_increment primary key,
    title varchar(100),
    genre_id int not null references genre (id),
    year year,
    length time
) type=InnoDB;

create table if not exists genre (
    id int not null auto_increment primary key,
    genre_name varchar(100),
    unique (genre_name)
) type=InnoDB;

create table if not exists director (
    id int not null auto_increment primary key,
    director_name varchar(100),
    unique (director_name)
) type=InnoDB;

create table if not exists movie_director_link (
    movie_id int not null references movie(id),
    director_id int not null references director(id),
    billing int not null default 1,
    primary key (movie_id, director_id)
) type=InnoDB;

create table if not exists catalog (
    movie_id int not null references movie(id),
    dvd_number int not null,
    selection_number int not null default 1,
    primary key (movie_id, dvd_number, selection_number)
) type=InnoDB;

