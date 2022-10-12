drop table if exists users;
drop table if exists albums;
drop table if exists musicians;
create table if not exists users(
    UE VARCHAR(255) NOT NULL,
    UN VARCHAR(255) NOT NULL,
    AVATAR VARCHAR(255),
    PW VARCHAR(255) NOT NULL,
    UTP INT NOT NULL,
    UB TEXT
);

create table if not exists musicians(
    MID VARCHAR(255) NOT NULL,
    MN  VARCHAR(255) NOT NULL,
    PH  VARCHAR(255),
    OC  TEXT NOT NULL,
    LC  TEXT,
    LT  TEXT,
    FY  DATETIME,
    INFO TEXT,
    PRIMARY KEY(MID)
);

create table if not exists albums(
    AID INT UNSIGNED AUTO_INCREMENT,
    AN  VARCHAR(255) NOT NULL,
    AP  INT     NOT NULL,
    AU  VARCHAR(255) NOT NULL,
    MN  VARCHAR(255) NOT NULL,
    PRIMARY KEY(AID),
    FOREIGN KEY(MN) REFERENCES musicians(MID)
);