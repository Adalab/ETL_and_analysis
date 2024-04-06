query_creacion_bbdd = "CREATE SCHEMA IF NOT EXISTS `Flights_Evaluacion_3`;"

query_tabla_cliente = """CREATE TABLE IF NOT EXISTS `Flights_Evaluacion_3`.`cliente` (
  `loyalty_number` INT NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `province` VARCHAR(45) NOT NULL, 
  `city` VARCHAR(45) NOT NULL,
  `postal_code` VARCHAR(45) NOT NULL,
  `gender` VARCHAR(45) NOT NULL,
  `education` VARCHAR(45) NOT NULL,
  `salary` FLOAT NULL,
  `marital_status` VARCHAR(45) NOT NULL,
  `loyalty_card` VARCHAR(45) NOT NULL,
  `clv` FLOAT NOT NULL,
  `enrollment_type` VARCHAR(45) NOT NULL,
  `enrollment_year` INT NOT NULL,
  `enrollment_month` INT NOT NULL,
  `cancellation_year` VARCHAR(45) NOT NULL,
  `cancellation_month` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`loyalty_number`));"""

query_tabla_registros = """CREATE TABLE IF NOT EXISTS `Flights_Evaluacion_3`.`registros` (
  `id_registro` INT NOT NULL AUTO_INCREMENT,
  `loyalty_number` INT NOT NULL,
  `flights_booked` INT NOT NULL,
  `flights_with_companions` INT NOT NULL,
  `total_flights` INT NOT NULL,
  `distance` INT NOT NULL,
  `points_accumulated` FLOAT NOT NULL,
  `points_redeemed` INT NOT NULL,
  `dollar_cost_points_redeemed` INT NOT NULL,
  `year` INT NOT NULL,
  `month` INT NOT NULL,
  PRIMARY KEY (`id_registro`),
  INDEX `loyalty_n_idx` (`loyalty_number` ASC) VISIBLE,
  CONSTRAINT `loyalty_n`
    FOREIGN KEY (`loyalty_number`)
    REFERENCES `Flights_Evaluacion_3`.`cliente` (`loyalty_number`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);"""

query_insertar_cliente = "INSERT INTO cliente (loyalty_number, country, province, city, postal_code, gender, education, salary, marital_status, loyalty_card, clv, enrollment_type, enrollment_year, enrollment_month, cancellation_year, cancellation_month) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

query_insertar_registros = "INSERT INTO registros (loyalty_number, year, month, flights_booked, flights_with_companions, total_flights, distance, points_accumulated, points_redeemed, dollar_cost_points_redeemed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"