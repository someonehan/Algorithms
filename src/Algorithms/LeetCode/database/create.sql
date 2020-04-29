create table Scores(
    Id INTEGER PRIMARY KEY,
    Score INTEGER NOT NULL
)

alter table Scores add INDEX id_Score(Score)

insert into Scores VALUES(1, 35), (2, 36), (3, 35), (4, 40);


drop table Souece;
