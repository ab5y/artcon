-- 1
drop table if exists user_type;
create table user_type (
	id integer primary key autoincrement,
	type text not null
);

-- 2
drop table if exists user;
create table user (
	id integer primary key autoincrement,
	user_type_id integer not null,
	name text not null,
	foreign key(user_type_id) references user_type(id)
);

-- 3
drop table if exists artist_type;
create table artist_type (
	id integer primary key autoincrement,
	type text not null
);

-- 4
drop table if exists employer_type;
create table employer_type (
	id integer primary key autoincrement,
	type text not null
);

-- 5
drop table if exists genre;
create table genre (
	id integer primary key autoincrement,
	type text not null
);

-- 6
drop table if exists artist;
create table artist (
	id integer primary key autoincrement,
	user_id integer not null,
	foreign key(user_id) references user(id)
);

-- 7
drop table if exists artist_genre;
create table artist_genre (
	id integer primary key autoincrement,
	artist_id integer not null,
	genre_id integer not null,
	foreign key(artist_id) references artist(id),
	foreign key(genre_id) references genre(id)
);

-- 8
drop table if exists artist_artist_type;
create table artist_artist_type (
	id integer primary key autoincrement,
	artist_id integer not null,
	artist_type_id integer not null,
	foreign key(artist_id) references artist(id),
	foreign key(artist_type_id) references artist_type(id)
);

-- 9
drop table if exists employer;
create table employer(
	id integer primary key autoincrement,
	user_id integer not null,
	employer_type_id integer not null,
	foreign key(user_id) references user(id),
	foreign key(employer_type_id) references employer_type(id)
);

-- 10
drop table if exists fan;
create table fan(
	id integer primary key autoincrement,
	user_id integer not null,
	foreign key(user_id) references user(id)
);

-- 11
drop table if exists contact_type;
create table contact_type(
	id integer primary key autoincrement,
	type text not null
);

-- 12
drop table if exists user_contact;
create table user_contact (
	id integer primary key autoincrement,
	user_id integer not null,
	contact_type_id integer not null,
	contact text not null,
	foreign key(user_id) references user(id),
	foreign key(contact_type_id) references contact_type(id)
);

-- 13
drop table if exists associated_act;
create table associated_act (
	id integer primary key autoincrement,
	artist_id integer not null,
	associated_act_id integer not null,
	foreign key(artist_id) references artist(id),
	foreign key(associated_act_id) references artist(id)
);

-- 14
drop table if exists address;
create table address (
	id integer primary key autoincrement,
	name text,
	administrative_area text,
	sub_administrative_area text,
	locality text not null,
	dependent_locality text,
	postal_code integer,
	thoroughfare text,
	premise text,
	sub_premise text
);

-- 15
drop table if exists venue_type;
create table venue_type (
	id integer primary key autoincrement,
	type text not null
);

-- 16
drop table if exists venue;
create table venue(
	id integer primary key autoincrement,
	address_id integer not null,
	venue_type_id integer not null,
	name text,
	foreign key(address_id) references address(id),
	foreign key(venue_type_id) references venue_type(id)
);

-- 17
drop table if exists performance;
create table performance(
	id integer primary key autoincrement,
	venue_id integer not null,
	date_from date not null,
	date_to date,
	foreign key(venue_id) references venue(id)
);

-- 18
drop table if exists media_type;
create table media_type(
	id integer primary key autoincrement,
	mime_type text not null
);

-- 19
drop table if exists media;
create table media(
	id integer primary key autoincrement,
	media_type_id integer not null,
	media_path text not null,
	foreign key(media_type_id) references media_type(id)
);

-- 20
drop table if exists performance_media;
create table performance_media (
	id integer primary key autoincrement,
	performance_id integer not null,
	media_id integer not null,
	foreign key(performance_id) references performance(id),
	foreign key(media_id) references media(id)
);

-- 21
drop table if exists media_artist;
create table media_artist (
	id integer primary key autoincrement,
	media_id integer not null,
	artist_id integer not null,
	foreign key (media_id) references media(id),
	foreign key(artist_id) references artist(id)
);

-- 22
drop table if exists artist_supported;
create table artist_supported (
	id integer primary key autoincrement,
	employer_id integer not null,
	artist_id integer not null,
	foreign key(employer_id) references employer(id),
	foreign key(artist_id) references artist(id)
);

-- 23
drop table if exists event_type;
create table event_type (
	id integer primary key autoincrement,
	type text not null
);

-- 24
drop table if exists event;
create table event (
	id integer primary key autoincrement,
	event_type_id integer not null,
	organizer_id integer not null,
	foreign key(event_type_id) references event_type(id),
	foreign key(organizer_id) references employer(id)
);

-- 25
drop table if exists event_venue;
create table  event_venue (
	id integer primary key autoincrement,
	event_id integer not null,
	venue_id integer not null,
	foreign key(event_id) references event(id),
	foreign key(venue_id) references venue(id)
);

-- 26
drop table if exists event_meta;
create table event_meta (
	id integer primary key autoincrement,
	event_id integer not null,
	repeat_start integer,
	repeat_interval integer,
	repeat_year integer,
	repeat_month integer,
	repeat_day integer,
	repeat_week integer,
	repeat_weekday integer,
	foreign key(event_id) references event(id)
);

-- 27
drop table if exists audition_type;
create table audition_type (
	id integer primary key autoincrement,
	type text not null
);

-- 28
drop table if exists audition;
create table audition (
	id integer primary key autoincrement,
	employer_id integer not null,
	event_id integer,
	audition_type_id integer not null,
	foreign key(employer_id) references employer(id),
	foreign key(event_id) references event(id),
	foreign key(audition_type_id) references audition_type(id)
);

-- 29
drop table if exists suggestion;
create table suggestion (
	id integer primary key autoincrement,
	employer_id integer not null,
	user_id integer not null,
	suggestion text not null,
	foreign key(employer_id) references employer(id),
	foreign key(user_id) references user(id)
);

-- 30
drop table if exists artist_follower;
create table artist_follower (
	id integer primary key autoincrement,
	artist_id integer not null,
	follower_id integer not null,
	foreign key(artist_id) references artist(id),
	foreign key(follower_id) references user(id)
);

-- 31
drop table if exists portfolio;
create table portfolio (
	id integer primary key autoincrement,
	artist_id integer not null
);

-- 32
drop table if exists portfolio_group;
create table portfolio_group (
	id integer primary key autoincrement,
	name text,
	portfolio_id integer not null,
	foreign key(portfolio_id) references portfolio(id)
);

-- 33
drop table if exists portfolio_media;
create table portfolio_media (
	id integer primary key autoincrement,
	portfolio_id integer not null,
	media_id integer not null,
	portfolio_group_id integer,
	foreign key(portfolio_id) references portfolio(id),
	foreign key(media_id) references media(id),
	foreign key(portfolio_group_id) references portfolio_group(id)
);

