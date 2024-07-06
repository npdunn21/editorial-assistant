create table CLIENT (
    ID UUID not null,
    NAME varchar(100) not null,
    DESCRIPTION varchar(100) not null
);

create table CONTENT (
    ID UUID not null,
    CLIENT_ID UUID not null,
    TEXT varchar not null,
    POST_TYPE varchar not null,
    AUTHOR varchar not null,
    COMMENT_COUNT int default 0,
    LIKE_COUNT int default 0,
    IMPRESSION_COUNT int default 0
);