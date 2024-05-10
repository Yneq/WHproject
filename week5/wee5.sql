 CREATE TABLE member(
     id BIGINT PRIMARY KEY AUTO_INCREMENT,
     name VARCHAR(255) NOT NULL,
     username VARCHAR(255) NOT NULL,
     password VARCHAR(255) NOT NULL,
     follower_count INT UNSIGNED NOT NULL DEFAULT 0, 
     time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
     );

INSERT INTO member (name, username, password) VALUES ('test', 'test', 'test');
INSERT INTO member (name, username, password) VALUES ('vance', 'vance', 'password1');
INSERT INTO member (name, username, password) VALUES ('kiko', 'kiko', 'password2');
INSERT INTO member (name, username, password) VALUES ('amor', 'amor', 'password3');
INSERT INTO member (name, username, password) VALUES ('esther', 'esther', 'password4');

CREATE TABLE message(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    member_id BIGINT NOT NULL, 
    FOREIGN KEY (member_id) REFERENCES member(id),
    content VARCHAR(255) NOT NULL,
    like_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO message (member_id, content, like_count) VALUES ('1', '紅茶', '5');
INSERT INTO message (member_id, content, like_count) VALUES ('2', '奶茶', '4');
INSERT INTO message (member_id, content, like_count) VALUES ('3', '綠茶', '3');
INSERT INTO message (member_id, content, like_count) VALUES ('4', '美式', '2');
INSERT INTO message (member_id, content, like_count) VALUES ('5', '拿鐵', '1');

SELECT member.username, AVG(message.like_count) FROM message INNER JOIN member ON message.member_id =member.id GROUP BY member.username;

mysqldump -u root -p database_member > '/Users/vanceweng/文件/WeHelp/week5/data.sql'

