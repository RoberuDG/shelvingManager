
--TABLES CREATION--
CREATE TABLE IF NOT EXISTS rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT(20) NOT NULL,
    description TEXT(255),
    positions INTEGER NOT NULL,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS shelvings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id INTEGER NOT NULL,
    code INTEGER NOT NULL,
    positions INTEGER NOT NULL,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES rooms(id),
    is_active BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS shelves (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shelving_id INTEGER NOT NULL,
    code INTEGER NOT NULL,
    order INTEGER NOT NULL,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (shelving_id) REFERENCES shelvings(id),
    is_active BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS item_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT(20) NOT NULL,
    description TEXT(255),
    positions INTEGER NOT NULL,
    is_active BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shelve_id INTEGER,
    item_type_id INTEGER NOT NULL,
    position INTEGER NOT NULL,
    name TEXT(25) NOT NULL,
    description TEXT(255),
    is_active BOOLEAN NOT NULL,
    FOREIGN KEY (shelving_id) REFERENCES shelvings(id),
    FOREIGN KEY (item_type_id) REFERENCES item_types(id),
);