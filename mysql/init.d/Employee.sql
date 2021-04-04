USE sample_db;

CREATE TABLE exchange (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(32) NOT NULL,
    value INT NOT NULL,
    PRIMARY KEY (id)
);
