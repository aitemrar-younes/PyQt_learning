-- Table: public.fournisseur

-- DROP TABLE IF EXISTS public.fournisseur;

CREATE TABLE IF NOT EXISTS public.fournisseur
(
    id integer NOT NULL DEFAULT nextval('fournisseur_id_seq'::regclass),
    nom character varying(50) COLLATE pg_catalog."default" NOT NULL,
    prenom character varying(50) COLLATE pg_catalog."default" NOT NULL,
    num character varying(20) COLLATE pg_catalog."default",
    adrress character varying(150) COLLATE pg_catalog."default",
    deleted boolean DEFAULT false,
    CONSTRAINT fournisseur_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.fournisseur
    OWNER to postgres;


	-- Table: public.item

-- DROP TABLE IF EXISTS public.item;

CREATE TABLE IF NOT EXISTS public.item
(
    nom character varying(150) COLLATE pg_catalog."default" NOT NULL,
    designation character varying(150) COLLATE pg_catalog."default",
    quantity integer NOT NULL DEFAULT 0,
    prix_achat double precision DEFAULT 0,
    prix_vente double precision DEFAULT 0,
    date_ajout date,
    date_maj date,
    CONSTRAINT item_pkey PRIMARY KEY (nom)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.item
    OWNER to postgres;