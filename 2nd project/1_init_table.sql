-- Table: fournisseur
CREATE TABLE fournisseur (
    id SERIAL PRIMARY KEY,
    nom VARCHAR,
    prenom VARCHAR,
    num VARCHAR unique,
    status BOOLEAN DEFAULT TRUE
);

-- Table: item
CREATE TABLE item (
    id SERIAL PRIMARY KEY,
    nom VARCHAR UNIQUE,
    qnt INTEGER DEFAULT 0,
    date DATE DEFAULT CURRENT_DATE,
    cout NUMERIC DEFAULT 0,
    last_date_price_modified DATE DEFAULT CURRENT_DATE
);

-- Table: division
CREATE TABLE division (
    id SERIAL PRIMARY KEY,
    nom VARCHAR UNIQUE,
    libelle VARCHAR
);

-- Table: pole
CREATE TABLE pole (
    id SERIAL PRIMARY KEY,
    nom VARCHAR UNIQUE,
    libelle VARCHAR,
    date_creation DATE DEFAULT CURRENT_DATE,
    division_id INTEGER REFERENCES division(id)
);

-- Table: achat
CREATE TABLE achat (
    id SERIAL PRIMARY KEY,
    item_id INTEGER REFERENCES item(id),
    qnt INTEGER check( qnt>0 ),
    price NUMERIC,
    date DATE DEFAULT CURRENT_DATE
);

-- Table: projet
CREATE TABLE projet (
    id SERIAL PRIMARY KEY,
    pole_id INTEGER REFERENCES pole(id),
    date_ouverture DATE,
    budget INTEGER
);

-- Table: project_items
CREATE TABLE project_items (
    id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projet(id),
    item_id INTEGER REFERENCES item(id),
    date DATE,
    price INTEGER
);

-- Table: historique_item_price
CREATE TABLE historique_item_price (
    id SERIAL PRIMARY KEY,
    item_id INTEGER REFERENCES item(id),
    price NUMERIC,
    date_debut DATE,
    date_fin DATE
);

alter table public.projet
add column intitule VARCHAR;

alter table public.project_items
add column qnt INTEGER check (qnt>0);