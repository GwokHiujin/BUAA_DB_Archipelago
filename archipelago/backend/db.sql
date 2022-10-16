drop table if exists users;
drop table if exists albums;
drop table if exists musicians;
create table if not exists users(
    UE VARCHAR(255) NOT NULL,
    UN VARCHAR(255) NOT NULL,
    AVATAR VARCHAR(255),
    PW VARCHAR(255) NOT NULL,
    UTP INT NOT NULL,
    UB TEXT,
    PRIMARY KEY(UE)
);

create table if not exists musicians(
    MID INTEGER PRIMARY KEY AUTOINCREMENT,
    UE  VARCHAR(255) NOT NULL,
    MN  VARCHAR(255) NOT NULL,
    PH  VARCHAR(255),
    OC  TEXT NOT NULL,
    LC  TEXT,
    LT  TEXT,
    FY  DATETIME,
    INFO TEXT,
    FOREIGN KEY(UE) REFERENCES users(UE) ON DELETE CASCADE
);

create table if not exists albums(
    AID INTEGER PRIMARY KEY AUTOINCREMENT,
    AN  VARCHAR(255) NOT NULL,
    AP  INT          NOT NULL,
    AU  VARCHAR(255) NOT NULL,
    MID VARCHAR(255) NOT NULL,
    RY  DATETIME,
    AC  VARCHAR(255),
    TYP INT NOT NULL,
    SRC VARCHAR(255),
    FOREIGN KEY(MID) REFERENCES musicians(MID) ON DELETE CASCADE
);