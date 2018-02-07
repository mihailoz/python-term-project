DROP TABLE IF EXISTS reservation_service;
DROP TABLE IF EXISTS reservation;
DROP TABLE IF EXISTS hotel_service;
DROP TABLE IF EXISTS hotel_room;
DROP TABLE IF EXISTS room;
DROP TABLE IF EXISTS hotel;
DROP TABLE IF EXISTS service;
DROP TABLE IF EXISTS person_permission;
DROP TABLE IF EXISTS permission;
DROP TABLE IF EXISTS person;

CREATE TABLE permission (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

INSERT INTO permission(name, description) VALUES ("VIEW_HOTEL", "Allows the user view hotels, rooms and services");
INSERT INTO permission(name, description) VALUES ("ADD_HOTEL", "Allows the user to add new hotels, rooms and services");
INSERT INTO permission(name, description) VALUES ("VIEW_USERS", "Allows the user to view other users and their permissions");
INSERT INTO permission(name, description) VALUES ("ADD_USERS", "Allows the user to add other users with basic permissions");
INSERT INTO permission(name, description) VALUES ("EDIT_PERMISSIONS", "Allows the user to give/take permissions from other users");

CREATE TABLE person(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

INSERT INTO person(username, password, first_name, last_name) VALUES ("mihailoz", "mz123", "Mihailo", "Zdravkovic");

CREATE TABLE person_permission (
    person_id INTEGER,
    permission_id INTEGER,
    FOREIGN KEY (person_id) REFERENCES person(id),
    FOREIGN KEY (permission_id) REFERENCES permission(id),
    PRIMARY KEY (person_id, permission_id)
);

INSERT INTO person_permission(person_id, permission_id) VALUES (1, 1);
INSERT INTO person_permission(person_id, permission_id) VALUES (1, 2);
INSERT INTO person_permission(person_id, permission_id) VALUES (1, 3);
INSERT INTO person_permission(person_id, permission_id) VALUES (1, 4);
INSERT INTO person_permission(person_id, permission_id) VALUES (1, 5);

CREATE TABLE hotel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    rating REAL
);

INSERT INTO hotel(name, city, country, rating) VALUES ("MGM Grand", "Las Vegas", "USA", 0);

CREATE TABLE room (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    number_of_people INTEGER NOT NULL
);

INSERT INTO room(description, number_of_people) VALUES ("Bedroom with a kitchen and bathroom for two", 2);

CREATE TABLE hotel_room (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hotel_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    price_per_day REAL NOT NULL,
    room_count INTEGER NOT NULL,
    FOREIGN KEY (hotel_id) REFERENCES hotel(id),
    FOREIGN KEY (room_id) REFERENCES room(id)
);

INSERT INTO hotel_room(hotel_id, room_id, price_per_day, room_count) VALUES (1, 1, 319.99, 5);

CREATE TABLE service (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

INSERT INTO service(name, description) VALUES ("Indoor pool", "An indoor pool where guests can relax and take a swim");

CREATE TABLE hotel_service (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    price REAL NOT NULL,
    hotel_id INTEGER,
    service_id INTEGER,
    FOREIGN KEY(hotel_id) REFERENCES hotel(id),
    FOREIGN KEY(service_id) REFERENCES service(id)
);

INSERT INTO hotel_service(hotel_id, service_id, price) VALUES (1, 1, 50.0);

CREATE TABLE reservation(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hotel_room_id INTEGER,
    person_id INTEGER,
    from_date DATE NOT NULL,
    to_date DATE NOT NULL,
    FOREIGN KEY(hotel_room_id) REFERENCES hotel_room(id),
    FOREIGN KEY(person_id) REFERENCES person(id)
);

CREATE TABLE reservation_service (
    reservation_id INTEGER,
    service_id INTEGER,
    FOREIGN KEY(reservation_id) REFERENCES reservation(id),
    FOREIGN KEY(service_id) REFERENCES service(id),
    PRIMARY KEY (reservation_id, service_id)
);