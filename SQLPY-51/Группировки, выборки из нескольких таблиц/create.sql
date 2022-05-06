create table if not exists Genre (
    genre_id serial primary key,
    genre_name varchar (40) not null
);

create table if not exists Artist (
    artist_id serial primary key,
    artist_name varchar(40) not null
);

create table if not exists Genre_Artist (
    genre_id int references Genre(genre_id),
    artist_id int references Artist(artist_id),
    constraint pkey0 primary key (genre_id, artist_id)
); 

create table if not exists Album (
    album_id serial primary key,
    album_name varchar (40) not null,
    release_year int not null check(release_year > 0)
);

create table if not exists Artist_Album (
    artist_id int references Artist(artist_id),
    album_id int references Album(album_id),
    constraint pkey1 primary key (artist_id, album_id)
);

create table if NOT EXISTS Track (
    track_id serial primary key,
    track_name varchar (40) NOT null,
    duration real NOT null,
    album_id int references Album(album_id)
    );

create table if not exists MCollection (
    mcollection_id serial primary key,
    mcollection_name varchar(40) not null,
    mcollection_year int not null check(mcollection_year > 0)
);

create table if not exists Track_Collection (
    mcollection_id int references MCollection(mcollection_id),
    track_id int references Track(track_id),
    constraint pkey2 primary key (mcollection_id, track_id)
);
