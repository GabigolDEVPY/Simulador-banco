
DROP TABLE users;

CREATE TABLE IF NOT exists users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(50) NOT NULL,
    user_login VARCHAR(50) NOT NULL,
    user_password VARCHAR(50) NOT NULL,
    chave_pix VARCHAR(70) NOT NULL,
    user_score INT DEFAULT 0, 
    user_found DOUBLE DEFAULT 0, 
    user_notifications INT DEFAULT 0,
    user_date_created DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_date_ DATETIME DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE user_history;

CREATE TABLE IF NOT exists user_history (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    title_history VARCHAR(50),
    subtitle_history VARCHAR(70),
    date_history DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE pigs (
    pig_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    meta_pig DOUBLE,
    total_bruto DOUBLE,
    image_pig VARCHAR(60),
    nome_pig VARCHAR(30),
    ganhos_total DOUBLE,
    ultimos_ganhos_pig DOUBLE
);

DROP TABLE pigs;

CREATE TABLE user_notifications (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    title_notify VARCHAR(40),
    subtitle_notify VARCHAR(70),
    date_notify TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE invest(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    bitcoin_invest DOUBLE DEFAULT 0,
    ethereum_invest DOUBLE DEFAULT 0,
    dolar_invest DOUBLE DEFAULT 0
);


SELECT * from users;
