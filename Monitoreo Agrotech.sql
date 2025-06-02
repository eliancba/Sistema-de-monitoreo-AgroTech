--Crear tabla cultivos
CREATE TABLE Cultivos (
  IdCultivo INTEGER AUTO_INCREMENT PRIMARY KEY,
  Nombre VARCHAR(30) NOT NULL
);

--Crear tabla TipoSensores
CREATE TABLE TipoSensores (
  IdTipoSensor INTEGER AUTO_INCREMENT PRIMARY KEY,
  Nombre VARCHAR(30) NOT NULL,
  Unidad VARCHAR(10) NOT NULL
);

--Crear tabla ubicaciones
CREATE TABLE Ubicaciones (
  IdUbicacion INTEGER AUTO_INCREMENT PRIMARY KEY,
  Latitud DECIMAL(10,4) NOT NULL,
  Longitud DECIMAL(10,4) NOT NULL
);

--Crear tabla campos
CREATE TABLE Campos (
  IdCampo INTEGER AUTO_INCREMENT PRIMARY KEY,
  Nombre VARCHAR(30) NOT NULL,
  IdUbicacion INTEGER,
  FOREIGN KEY (IdUbicacion) REFERENCES Ubicaciones(IdUbicacion)
);

--Crear tabla parcelas
CREATE TABLE Parcelas (
  IdParcela INTEGER AUTO_INCREMENT PRIMARY KEY,
  Nombre VARCHAR (20) NOT NULL,
  IdCampo INTEGER,
  FOREIGN KEY (IdCampo) REFERENCES Campos (IdCampo),
  IdCultivo INTEGER,
  FOREIGN KEY (IdCultivo) REFERENCES Cultivos(IdCultivo),
  Has DECIMAL(10, 2) NOT NULL,
  IdUbicacion INTEGER,
  FOREIGN KEY (IdUbicacion) REFERENCES Ubicaciones(IdUbicacion)
);

--Crear tabla sensores
CREATE TABLE Sensores (
  IdSensor INTEGER AUTO_INCREMENT PRIMARY KEY,
  Nombre VARCHAR(20) NOT NULL,
  IdTipoSensor INTEGER,
  FOREIGN KEY (IdTipoSensor) REFERENCES TipoSensores(IdTipoSensor),
  IdUbicacion INTEGER,
  FOREIGN KEY (IdUbicacion) REFERENCES Ubicaciones(IdUbicacion),
  Activado BOOLEAN DEFAULT TRUE
);

--Crear tabla mediciones
CREATE TABLE Mediciones (
  IdMedicion INTEGER AUTO_INCREMENT PRIMARY KEY,
  IdParcela INTEGER,
  FOREIGN KEY (IdParcela) REFERENCES Parcelas(IdParcela),
  IdSensor INTEGER,
  FOREIGN KEY (IdSensor) REFERENCES Sensores(IdSensor),
  Dato DECIMAL(10,2) NOT NULL,
  Fecha DATE NOT NULL
);


--Insertar datos tabla cultivos
INSERT INTO Cultivos(Nombre) VALUES 
('TRIGO'),
('MAIZ'),
('SOJA');

--Insertar datos en la tabla TipoSensores
INSERT INTO TipoSensores(Nombre, Unidad) VALUES 
('HUMEDAD','%'),
('NIVEL PH','PH'),
('TEMPERATURA','°C');

--Insertar datos en la tabla ubicaciones
INSERT INTO Ubicaciones(Latitud, Longitud) VALUES 
(-32.84105,-62.86593),
(-32.84005,-62.86703),
(-32.84115,-62.86599),
(-32.84205,-62.86493),
(-31.4135,-64.18105),
(-31.4235,-64.18125),
(-31.4035,-64.18175),
(-33.3842,-64.7228),
(-33.3842,-64.7228);

--Insertar datos en la tabla campos
INSERT INTO Campos(Nombre, IdUbicacion) VALUES 
('Decandido',1),
('Coronel',5),
('Elguero',8);

--Insertar datos en la tabla parcelas
INSERT INTO Parcelas(Nombre,IdCampo,IdCultivo,Has,IdUbicacion) VALUES 
('Norte',1,2,30,2),
('Centro',1,1,25.82,3),
('Sur',1,3,14,4),
(1,2,1,37,6),
(2,2,3,76.34,7),
('Unica',3,1,100,9);

--Insertar datos en la tabla sensores
INSERT INTO Sensores(Nombre,IdTipoSensor,IdUbicacion,Activado) VALUES 
('ROJO',1,2,TRUE),
('AZUL',2,2,FALSE),
('AMARILLO',3,2,TRUE),
('AZUL',2,3,FALSE),
('ROJO',1,3,TRUE),
('AMARILLO',3,4,FALSE),
('AZUL',2,4,TRUE),
(1,1,6,FALSE),
(2,2,6,FALSE),
(3,3,6,TRUE),
(4,2,7,FALSE),
('HUMEDAD',1,9,TRUE),
('PH',2,9,TRUE),
('TEMPERATURA',3,9,TRUE);

--Insertar datos en la tabla mediciones
INSERT INTO Mediciones (IdParcela, IdSensor, Dato, Fecha) VALUES 
(1, 1, 25.75, '2025-05-31'),
(1, 1, 80.74, '2025-06-01'),
(2, 3, 11.45, '2025-06-02'),
(2, 5, 14.05, '2025-05-31'),
(3, 7, 60.74, '2025-06-01'),
(3, 7, 2.70, '2025-06-02'),
(4, 8, 5.55, '2025-05-31'),
(4, 10, 89.41, '2025-06-01'),
(4, 9, 10.15, '2025-06-02'),
(5, 11, 34.51, '2025-06-02'),
(5, 11, 25.75, '2025-05-31'),
(6, 12, 80.74, '2025-06-01'),
(6, 13, 28.15, '2025-06-02');

--Mostrar todas las parcelas
SELECT * FROM Parcelas

--Mostrar los nombres de las parcelas del campo que contenga IdCampo = 1
SELECT Nombre FROM Parcelas WHERE IdCampo = 1

--Mostrar nombres e IdTipoSensor de los sensores que se encuentren activados
SELECT Nombre,IdTipoSensor FROM Sensores WHERE Activado = TRUE

/*Mostrar el nombre del campo y nombre de la parcela donde hay sembrado maiz*/
SELECT c.nombre AS NOMBRE_CAMPO,
       p.Nombre AS NOMBRE_PARCELA
FROM
    Campos c
JOIN
    Parcelas p ON c.IdCampo = p.IdCampo
JOIN
    Cultivos cu ON p.IdCultivo = cu.IdCultivo
WHERE
    cu.nombre = 'MAIZ';
    
/*Mostrar nombre de las parcelas, nombre del sensor, dato de la medicion, unidad del dato, 
fecha de la medicion de los sensores que miden humedad en el campo de Decandido*/
SELECT p.Nombre AS NOMBRE_PARCELA,
    s.Nombre AS NOMBRE_SENSOR,
    m.Dato AS DATO,
    ts.Unidad as UNIDAD,
    m.Fecha as FECHA
FROM
    Mediciones m
JOIN
    Sensores s ON m.IdSensor = s.IdSensor
JOIN
    Parcelas p ON m.IdParcela = p.IdParcela
JOIN
    Campos c ON P.IdCampo = c.IdCampo
JOIN
    TipoSensores ts ON s.IdTipoSensor = ts.IdTipoSensor
WHERE
    ts.Nombre = 'HUMEDAD' AND c.Nombre = 'Decandido'
