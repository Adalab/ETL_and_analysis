-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Flights_Evaluacion_3
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Flights_Evaluacion_3
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Flights_Evaluacion_3` DEFAULT CHARACTER SET utf8 ;
USE `Flights_Evaluacion_3` ;

-- -----------------------------------------------------
-- Table `Flights_Evaluacion_3`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Flights_Evaluacion_3`.`cliente` (
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
  PRIMARY KEY (`loyalty_number`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Flights_Evaluacion_3`.`registros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Flights_Evaluacion_3`.`registros` (
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
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
