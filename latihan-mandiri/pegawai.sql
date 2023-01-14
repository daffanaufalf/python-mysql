CREATE DATABASE db_pegawai;
USE db_pegawai;
CREATE TABLE pegawai (
    NIP char(4) NOT NULL,
    NAMA varchar(50),
    JABATAN varchar(30),
    DIVISI varchar(50),
    GAJI integer(50),
    primary key(NIP)
);
ALTER TABLE pegawai
ALTER COLUMN NIP
SET DEFAULT '';