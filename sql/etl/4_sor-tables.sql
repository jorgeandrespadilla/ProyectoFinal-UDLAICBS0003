USE dbsor;

CREATE TABLE PROVINCIAS ( 
    ID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ID_PROVINCIA INTEGER NOT NULL,
    NOMBRE_PROVINCIA VARCHAR (50) NOT NULL
);

CREATE TABLE SERVICIOS ( 
    ID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ID_SERVICIO INTEGER NOT NULL,
    DESCRIPCION_SERVICIO VARCHAR (50) NOT NULL,
    VALOR_SERVICIO DECIMAL (8,2) NOT NULL,
    TIEMPO_SUBSCRIPCION INTEGER (5) NOT NULL,
    BENEFICIOS_SERVICIO VARCHAR (100) NOT NULL
);

CREATE TABLE MOTIVOS ( 
    ID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ID_MOTIVO INTEGER NOT NULL,
    DESCRIPCION_MOTIVO VARCHAR (100) NOT NULL
);

CREATE TABLE CLIENTES ( 
    ID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ID_CLIENTE INTEGER NOT NULL,
    ID_PROVINCIA INTEGER NOT NULL,
    NOMBRE_CLIENTE VARCHAR (50) NOT NULL,
    TIPO_CLIENTE VARCHAR (10) NOT NULL
);

CREATE TABLE ORDENES ( 
    ID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ID_ORDEN INTEGER NOT NULL,
    ID_CLIENTE INTEGER NOT NULL,
    ID_SERVICIO INTEGER NOT NULL,
    ID_PROVINCIA INTEGER NOT NULL,
    ID_MOTIVO INTEGER NOT NULL,
    ESTADO_ORDEN VARCHAR (10) NOT NULL,
    FECHA_ADQUISICION DATE NOT NULL
);

CREATE TABLE PREMIOS (
    ID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ID_PREMIO INTEGER NOT NULL,
    ID_CLIENTE INTEGER NOT NULL,
    DESCRIPCION_PREMIO VARCHAR (100) NOT NULL,
    VALOR_PREMIO DECIMAL (8,2) NOT NULL,
    CANJEADO VARCHAR (1) NOT NULL
);


ALTER TABLE CLIENTES 
ADD CONSTRAINT CLIENTES_PROVINCIAS_FK FOREIGN KEY ( 
    ID_PROVINCIA
)
REFERENCES PROVINCIAS (
    ID
);

ALTER TABLE ORDENES 
ADD CONSTRAINT ORDENES_CLIENTES_FK FOREIGN KEY ( 
    ID_CLIENTE
)
REFERENCES CLIENTES (
    ID
);

ALTER TABLE ORDENES
ADD CONSTRAINT ORDENES_SERVICIOS_FK FOREIGN KEY ( 
    ID_SERVICIO
)
REFERENCES SERVICIOS (
    ID
);

ALTER TABLE ORDENES
ADD CONSTRAINT ORDENES_PROVINCIAS_FK FOREIGN KEY ( 
    ID_PROVINCIA
)
REFERENCES PROVINCIAS (
    ID
);

ALTER TABLE ORDENES
ADD CONSTRAINT ORDENES_MOTIVOS_FK FOREIGN KEY ( 
    ID_MOTIVO
)
REFERENCES MOTIVOS (
    ID
);

ALTER TABLE PREMIOS
ADD CONSTRAINT PREMIOS_CLIENTES_FK FOREIGN KEY ( 
    ID_CLIENTE
)
REFERENCES CLIENTES (
    ID
);