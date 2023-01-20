/* 
 *  Todas os códigos de criação de tabelas se encontram nesse arquivo, eles estão sendo separados por: /************/

-- Table: public.clima_fatos

-- DROP TABLE IF EXISTS public.clima_fatos;

CREATE TABLE IF NOT EXISTS public.clima_fatos
(
    "fkData" integer NOT NULL,
    "fkEstacao" integer NOT NULL,
    "PrecipitacaoTotal" real,
    "TempMax" real,
    "TempMin" real,
    "UmidMax" real,
    "UmidMin" real,
    "Vento" real,
    CONSTRAINT chave_estrangeira_data FOREIGN KEY ("fkData")
        REFERENCES public.data ("pkData") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT chave_estrangeira_local FOREIGN KEY ("fkEstacao")
        REFERENCES public.clima_local ("pkEstacao") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.clima_fatos
    OWNER to postgres;

/************/

-- Table: public.clima_local

-- DROP TABLE IF EXISTS public.clima_local;

CREATE TABLE IF NOT EXISTS public.clima_local
(
    "pkEstacao" integer NOT NULL,
    station character varying(50) COLLATE pg_catalog."default",
    region character varying(2) COLLATE pg_catalog."default",
    state character varying(2) COLLATE pg_catalog."default",
    station_code character varying(5) COLLATE pg_catalog."default",
    "Pais" character varying(3) COLLATE pg_catalog."default",
    CONSTRAINT clima_local_pkey PRIMARY KEY ("pkEstacao")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.clima_local
    OWNER to postgres;

/************/

-- Table: public.data

-- DROP TABLE IF EXISTS public.data;

CREATE TABLE IF NOT EXISTS public.data
(
    "pkData" integer NOT NULL,
    "DataCompleta" date,
    "Dia" character varying(2) COLLATE pg_catalog."default",
    "Semana" character varying(2) COLLATE pg_catalog."default",
    "Mes" character varying(2) COLLATE pg_catalog."default",
    "MesNome" character varying(9) COLLATE pg_catalog."default",
    "Ano" character varying(4) COLLATE pg_catalog."default",
    "Mes-Ano" character varying(7) COLLATE pg_catalog."default",
    "Trimestre" character varying(1) COLLATE pg_catalog."default",
    "Trimestre-Ano" character varying(6) COLLATE pg_catalog."default",
    "Semestre" character varying(1) COLLATE pg_catalog."default",
    "Semestre-Ano" character varying(6) COLLATE pg_catalog."default",
    CONSTRAINT data_pkey PRIMARY KEY ("pkData")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.data
    OWNER to postgres;

/************/

-- Table: public.saude_doencas

-- DROP TABLE IF EXISTS public.saude_doencas;

CREATE TABLE IF NOT EXISTS public.saude_doencas
(
    "pkDoenca" integer NOT NULL,
    doenca character varying(30) COLLATE pg_catalog."default",
    CONSTRAINT saude_doencas_pkey PRIMARY KEY ("pkDoenca")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.saude_doencas
    OWNER to postgres;

/*************/

-- Table: public.saude_doencas_grupo

-- DROP TABLE IF EXISTS public.saude_doencas_grupo;

CREATE TABLE IF NOT EXISTS public.saude_doencas_grupo
(
    "pkGrupoDoenca" integer NOT NULL,
    "influenza_A" character varying(1) COLLATE pg_catalog."default",
    "influenza_B" character varying(1) COLLATE pg_catalog."default",
    "VSR" character varying(1) COLLATE pg_catalog."default",
    "SarsCov2" character varying(1) COLLATE pg_catalog."default",
    "Parainfluenza_1" character varying(1) COLLATE pg_catalog."default",
    "Parainfluenza_2" character varying(1) COLLATE pg_catalog."default",
    "Parainfluenza_3" character varying(1) COLLATE pg_catalog."default",
    "Parainfluenza_4" character varying(1) COLLATE pg_catalog."default",
    "Adenovirus" character varying(1) COLLATE pg_catalog."default",
    "Metapneumovirus" character varying(1) COLLATE pg_catalog."default",
    "Bocavirus" character varying(1) COLLATE pg_catalog."default",
    "Rinovirus" character varying(1) COLLATE pg_catalog."default",
    "Outro_virus" character varying(1) COLLATE pg_catalog."default",
    CONSTRAINT saude_doencas_grupo_pkey PRIMARY KEY ("pkGrupoDoenca")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.saude_doencas_grupo
    OWNER to postgres;

/*************/

-- Table: public.saude_doencas_ponte

-- DROP TABLE IF EXISTS public.saude_doencas_ponte;

CREATE TABLE IF NOT EXISTS public.saude_doencas_ponte
(
    "fkGrupo" integer NOT NULL,
    "fkDoenca" integer NOT NULL,
    CONSTRAINT saude_doencas_ponte_pkey PRIMARY KEY ("fkGrupo", "fkDoenca"),
    CONSTRAINT doencas_grupo_para_ponte FOREIGN KEY ("fkGrupo")
        REFERENCES public.saude_doencas_grupo ("pkGrupoDoenca") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT doencas_para_ponte FOREIGN KEY ("fkDoenca")
        REFERENCES public.saude_doencas ("pkDoenca") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.saude_doencas_ponte
    OWNER to postgres;

/*************/

-- Table: public.saude_fatos

-- DROP TABLE IF EXISTS public.saude_fatos;

CREATE TABLE IF NOT EXISTS public.saude_fatos
(
    "fkData" integer NOT NULL,
    "fkLocal" integer NOT NULL,
    "fkPaciente" integer NOT NULL,
    "fkGrupoSintoma" integer NOT NULL,
    "fkGrupoDoenca" integer NOT NULL,
    "fkSituacao" integer NOT NULL,
    "Gestante" integer NOT NULL,
    "Registro_ocorrencia" integer NOT NULL,
    CONSTRAINT fk_data FOREIGN KEY ("fkData")
        REFERENCES public.data ("pkData") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_grupo_doenca FOREIGN KEY ("fkGrupoDoenca")
        REFERENCES public.saude_doencas_grupo ("pkGrupoDoenca") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_grupo_sintoma FOREIGN KEY ("fkGrupoSintoma")
        REFERENCES public.saude_sintomas_grupo ("pkGrupoSintoma") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_local FOREIGN KEY ("fkLocal")
        REFERENCES public.saude_local ("pkLocal") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_paciente FOREIGN KEY ("fkPaciente")
        REFERENCES public.saude_paciente ("pkPaciente") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_situacao FOREIGN KEY ("fkSituacao")
        REFERENCES public.saude_situacao ("pkSituacao") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.saude_fatos
    OWNER to postgres;

/*************/

-- Table: public.saude_local

-- DROP TABLE IF EXISTS public.saude_local;

CREATE TABLE IF NOT EXISTS public.saude_local
(
    "pkLocal" integer NOT NULL,
    "Estado" character varying(2) COLLATE pg_catalog."default",
    "Regiao" character varying(80) COLLATE pg_catalog."default",
    "Regiao_numero" character varying(6) COLLATE pg_catalog."default",
    "Municipio" character varying(35) COLLATE pg_catalog."default",
    "Municipio_numero" character varying(6) COLLATE pg_catalog."default",
    "Unidade" character varying(80) COLLATE pg_catalog."default",
    "Unidade_numero" character varying(7) COLLATE pg_catalog."default",
    CONSTRAINT saude_local_pkey PRIMARY KEY ("pkLocal")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.saude_local
    OWNER to postgres;

/*************/

-- Table: public.saude_paciente

-- DROP TABLE IF EXISTS public.saude_paciente;

CREATE TABLE IF NOT EXISTS public.saude_paciente
(
    "pkPaciente" integer NOT NULL,
    sexo character varying(1) COLLATE pg_catalog."default",
    data_nascimento date,
    recebeu_vacina character varying(3) COLLATE pg_catalog."default",
    data_dose_1 date,
    data_dose_2 date,
    data_dose_ref date,
    fab_1 character varying(100) COLLATE pg_catalog."default",
    fab_2 character varying(80) COLLATE pg_catalog."default",
    fab_ref character varying(80) COLLATE pg_catalog."default",
    CONSTRAINT saude_paciente_pkey PRIMARY KEY ("pkPaciente")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.saude_paciente
    OWNER to postgres;

/*************/

-- Table: public.saude_sintomas

-- DROP TABLE IF EXISTS public.saude_sintomas;

CREATE TABLE IF NOT EXISTS public.saude_sintomas
(
    "pkSintoma" integer NOT NULL,
    "Sintomas" character varying(30) COLLATE pg_catalog."default",
    CONSTRAINT saude_sintomas_pkey PRIMARY KEY ("pkSintoma")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.saude_sintomas
    OWNER to postgres;

/*************/

-- Table: public.saude_sintomas_grupo

-- DROP TABLE IF EXISTS public.saude_sintomas_grupo;

CREATE TABLE IF NOT EXISTS public.saude_sintomas_grupo
(
    "pkGrupoSintoma" integer NOT NULL,
    "Nosocomial" character varying(1) COLLATE pg_catalog."default",
    "Febre" character varying(1) COLLATE pg_catalog."default",
    "Tosse" character varying(1) COLLATE pg_catalog."default",
    "Garganta" character varying(1) COLLATE pg_catalog."default",
    "Dispneia" character varying(1) COLLATE pg_catalog."default",
    "Desconforto_respiratorio" character varying(1) COLLATE pg_catalog."default",
    "Saturacao" character varying(1) COLLATE pg_catalog."default",
    "Diarreia" character varying(1) COLLATE pg_catalog."default",
    "Vomito" character varying(1) COLLATE pg_catalog."default",
    "Dor_abdominal" character varying(1) COLLATE pg_catalog."default",
    "Fadiga" character varying(1) COLLATE pg_catalog."default",
    "Perda_de_olfato" character varying(1) COLLATE pg_catalog."default",
    "Perda_do_paladar" character varying(1) COLLATE pg_catalog."default",
    CONSTRAINT saude_sintomas_grupo_pkey PRIMARY KEY ("pkGrupoSintoma")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.saude_sintomas_grupo
    OWNER to postgres;

/*************/

-- Table: public.saude_sintomas_ponte

-- DROP TABLE IF EXISTS public.saude_sintomas_ponte;

CREATE TABLE IF NOT EXISTS public.saude_sintomas_ponte
(
    "fkGrupo" integer NOT NULL,
    "fkSintoma" integer NOT NULL,
    CONSTRAINT saude_sintomas_ponte_pkey PRIMARY KEY ("fkGrupo", "fkSintoma"),
    CONSTRAINT sintomas_grupo_para_ponte FOREIGN KEY ("fkGrupo")
        REFERENCES public.saude_sintomas_grupo ("pkGrupoSintoma") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT sintomas_para_ponte FOREIGN KEY ("fkSintoma")
        REFERENCES public.saude_sintomas ("pkSintoma") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.saude_sintomas_ponte
    OWNER to postgres;

/*************/

-- Table: public.saude_situacao

-- DROP TABLE IF EXISTS public.saude_situacao;

CREATE TABLE IF NOT EXISTS public.saude_situacao
(
    "pkSituacao" integer NOT NULL,
    situacao_obito character varying(1) COLLATE pg_catalog."default",
    situacao_doente character varying(1) COLLATE pg_catalog."default",
    CONSTRAINT saude_situacao_pkey PRIMARY KEY ("pkSituacao")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.saude_situacao
    OWNER to postgres;