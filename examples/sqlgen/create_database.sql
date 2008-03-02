create database if not exists movie_db;

grant all on movie_db.*
   to movie_admin identified by 'admin_pw';
grant select, insert, update, delete on movie_db.*
   to movie_user identified by 'user_pw';
