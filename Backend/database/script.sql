
--TABLES CREATION--
CREATE TABLE IF NOT EXISTS rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT(20) NOT NULL,
    description TEXT(255),
    positions TEXT NOT NULL,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS shelvings (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    room_id INTEGER NOT NULL,
    name TEXT(3) NOT NULL,
    description TEXT(255),
    positions INTEGER NOT NULL,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);

CREATE TABLE IF NOT EXISTS shelves (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    shelving_id INTEGER NOT NULL,
    name TEXT(6) NOT NULL,
    description TEXT(255),
    position INTEGER NOT NULL,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (shelving_id) REFERENCES shelvings(id)
);

CREATE TABLE IF NOT EXISTS item_types (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    name TEXT(20) NOT NULL,
    description TEXT(255),
    positions INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS items (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    shelf_id INTEGER,
    item_type_id INTEGER NOT NULL,
    position INTEGER NOT NULL,
    name TEXT(25) NOT NULL,
    description TEXT(255),
    FOREIGN KEY (shelf_id) REFERENCES shelves(id),
    FOREIGN KEY (item_type_id) REFERENCES item_types(id)
);