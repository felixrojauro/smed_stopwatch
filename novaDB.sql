-- MySQL Script generated by MySQL Workbench
-- Tue Apr 26 22:24:08 2016
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema FaureciaSmed
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema FaureciaSmed
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `FaureciaSmed` DEFAULT CHARACTER SET utf8 ;
USE `FaureciaSmed` ;

-- -----------------------------------------------------
-- Table `FaureciaSmed`.`Cores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FaureciaSmed`.`Cores` (
  `ID` INT(11) NOT NULL AUTO_INCREMENT,
  `cor` VARCHAR(10) NOT NULL,
  `tempo_max` TINYTEXT NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `idCores_UNIQUE` (`ID` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `FaureciaSmed`.`Paragens`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FaureciaSmed`.`Paragens` (
  `ID` INT(11) NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(20) NOT NULL,
  `tempo_max` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `ID_UNIQUE` (`ID` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `FaureciaSmed`.`Tempos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FaureciaSmed`.`Tempos` (
  `ID` INT(5) NOT NULL AUTO_INCREMENT,
  `linha` VARCHAR(10) NOT NULL,
  `data` DATE NOT NULL,
  `hora` TIME NOT NULL,
  `tempo` VARCHAR(10) NOT NULL,
  `cor` VARCHAR(10) NOT NULL,
  `tipo` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `cor_idx` (`cor` ASC),
  INDEX `tipo_idx` (`tipo` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


/*
-- Query: SELECT * FROM FaureciaSmed.Paragens
LIMIT 0, 1000

-- Date: 2016-04-26 22:51
*/
INSERT INTO `Paragens` (`ID`,`tipo`,`tempo_max`) VALUES (1,'MP','01:00:00');
INSERT INTO `Paragens` (`ID`,`tipo`,`tempo_max`) VALUES (2,'SMED','00:00:00');
INSERT INTO `Paragens` (`ID`,`tipo`,`tempo_max`) VALUES (3,'AVARIA','00:00:00');


/*
-- Query: SELECT * FROM FaureciaSmed.Cores
LIMIT 0, 1000

-- Date: 2016-04-26 22:52
*/
INSERT INTO `Cores` (`ID`,`cor`,`tempo_max`) VALUES (1,'Verde','');
INSERT INTO `Cores` (`ID`,`cor`,`tempo_max`) VALUES (2,'Laranja','');
INSERT INTO `Cores` (`ID`,`cor`,`tempo_max`) VALUES (3,'Vermelho','');

