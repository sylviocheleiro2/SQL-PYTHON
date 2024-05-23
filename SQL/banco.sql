drop database if exists banco;
create database banco;
use banco;

create table conta
(
id integer primary key auto_increment,
nome varchar(50) not null,
saldo float not null
);

insert into conta value (0, "Gabriel", 1000);
insert into conta value (0, "Lucas", 2000);
insert into conta value (0, "Sylvio", 3000);
insert into conta value (0, "Pedro", 4000);


