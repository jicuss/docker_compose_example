SELECT * FROM pg_timezone_names;
ALTER DATABASE postgres SET timezone TO 'America/Los_Angeles';

-- kill all active connections
select pg_terminate_backend(pg_stat_activity.pid) from pg_stat_activity where pg_stat_activity.datname = 'postgres' and pid <> pg_backend_pid();


drop table if exists example_table;
create table example_table ( content_string varchar(500) , created_at timestamp default now() ) ;
    
insert into example_table ( content_string ) values ( 'example string' ) ;

select * from example_table; 