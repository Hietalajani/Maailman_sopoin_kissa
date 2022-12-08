-- MariaDB dump 10.19  Distrib 10.6.9-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: kisupeli2
-- ------------------------------------------------------
-- Server version	10.6.9-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `lentokentta`
--

DROP TABLE IF EXISTS `lentokentta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lentokentta` (
  `icao` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nimi` varchar(70) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `leveyspiiri` double DEFAULT NULL,
  `pituuspiiri` double DEFAULT NULL,
  `maa` varchar(40) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`icao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lentokentta`
--

LOCK TABLES `lentokentta` WRITE;
/*!40000 ALTER TABLE `lentokentta` DISABLE KEYS */;
INSERT INTO `lentokentta` VALUES ('EBBR','Brysselin lentoasema',50.901401519800004,4.48443984985,'Belgia'),('EDDB','Berliinin-Brandenburgin lentoasema',52.351389,13.493889,'Saksa'),('EETN','Lennart Merin lentoasema',59.41329956049999,24.832799911499997,'Viro'),('EFHK','Helsinki-Vantaan lentoasema',60.3172,24.963301,'Suomi'),('EGLL','Lontoo Heathrow lentokenttä',51.4706,-0.461941,'Iso-Britannia'),('EHAM','Schipholin kansainvälinen lentoasema',52.308601,4.76389,'Alankomaat'),('EIDW','Dublinin lentoasema',53.421299,-6.27007,'Irlanti'),('EKCH','Kööpenhaminan lentoasema',55.617900848389,12.656000137329,'Tanska'),('ELLX','Findelin kansainvälinen lentoasema',49.6233333,6.2044444,'Luxemburg'),('ENGM','Oslo lentokenttä, Gardermoen',60.193901,11.1004,'Norja'),('EPWA','Frédéric Chopinin kansainvälinen lentoasema',52.1656990051,20.967100143399996,'Puola'),('ESSA','Arlandan lentoasema',59.651901245117,17.918600082397,'Ruotsi'),('EVRA','Riika kansainvälinen lentokenttä',56.92359924316406,23.971099853515625,'Latvia'),('EYVI','Vilnan lentoasema',54.634102,25.285801,'Liettua'),('LATI','Nënë Terezan kansainvälinen lentoasema',41.4146995544,19.7206001282,'Albania'),('LBSF','Sofian lentoasema',42.696693420410156,23.411436080932617,'Bulgaria'),('LDZA','Franjo Tudmanin lentoasema',45.7429008484,16.0687999725,'Kroatia'),('LEMD','Adolfo Suárezin Barajasin Madridin kansainvälinen lentoasema',40.471926,-3.56264,'Espanja'),('LESU','Andorra-La Seu d\'Urgell -lentokenttä',42.3386,1.40917,'Andorra'),('LFPG','Charles de Gaullen kansainvälinen lentoasema',49.012798,2.55,'Ranska'),('LGAV','Ateenan kansainvälinen lentoasema',37.936401,23.9445,'Kreikka'),('LHBP','Budapestin Ferenc Lisztin kansainvälinen lentoasema',47.42976,19.261093,'Unkari'),('LIRF','Leonardo da Vincin kansainvälinen lentoasema',41.804532,12.251998,'Italia'),('LJLJ','Joze Pucnikin kansainvälinen lentoasema',46.223701,14.4576,'Slovenia'),('LKPR','Václav Havelin kansainvälinen lentoasema',50.1008,14.26,'Tsekki'),('LNMC','Monacon helikopterikenttä',43.725798,7.419673,'Monaco'),('LOWW','Wienin kansainvälinen lentoasema',48.110298,16.5697,'Itävalta'),('LPPT','Portelan lentoasema',38.7813,-9.13592,'Portugali'),('LROP','Henri Coandan kansainvälinen lentoasema',44.5711111,26.085,'Romania'),('LSZH','Zürichin lentoasema',47.458056,8.548056,'Sveitsi'),('LWSK','Skopjen kansainvälinen lentoasema',41.961601,21.621401,'Pohjois-Makedonia'),('LYBE','Belgradin Nikola Teslan lentoasema',44.8184013367,20.3090991974,'Serbia'),('LYPG','Podgorican lentoasema',42.359402,19.2519,'Montenegro'),('LZIB','M. R. Stefánikin lentoasema',48.17020034790039,17.21269989013672,'Slovakia'),('UKBB','Boryspilin kansainvälinen lentoasema',50.345001220703125,30.894699096679688,'Ukraina'),('UMMS','Minskin kansallinen lentoasema',53.888071,28.039964,'Valko-Venäjä');
/*!40000 ALTER TABLE `lentokentta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `peli`
--

DROP TABLE IF EXISTS `peli`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `peli` (
  `id` int(11) NOT NULL,
  `pelaaja_nimi` varchar(16) NOT NULL DEFAULT '',
  `kissa_karsivallisyys` int(11) NOT NULL DEFAULT 0,
  `kaytetty_karsivallisyys` int(11) NOT NULL DEFAULT 0,
  `sijainti` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sijainti` (`sijainti`),
  CONSTRAINT `peli_ibfk_1` FOREIGN KEY (`sijainti`) REFERENCES `lentokentta` (`icao`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `peli`
--

LOCK TABLES `peli` WRITE;
/*!40000 ALTER TABLE `peli` DISABLE KEYS */;
/*!40000 ALTER TABLE `peli` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tavoite`
--

DROP TABLE IF EXISTS `tavoite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tavoite` (
  `id` int(11) NOT NULL,
  `nimi` varchar(40) DEFAULT NULL,
  `kuvaus` varchar(40) DEFAULT NULL,
  `kohde` varchar(40) DEFAULT NULL,
  `kohde_arvo` int(11) DEFAULT NULL,
  `max_maara` int(11) DEFAULT NULL,
  `min_maara` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tavoite`
--

LOCK TABLES `tavoite` WRITE;
/*!40000 ALTER TABLE `tavoite` DISABLE KEYS */;
INSERT INTO `tavoite` VALUES (1,'KISSA','Maailman söpöin kissa','KISSA',NULL,1,NULL),(2,'KISSANMINTTU','Arvokkain herkku','HERKKU',1000,4,0),(3,'TONNIKALA','Toiseksi arvokkain herkku','HERKKU',750,5,0),(4,'HERKKUTIKKU','Vähiten arvokas herkku','HERKKU',500,6,0);
/*!40000 ALTER TABLE `tavoite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tavoite_saavutettu`
--

DROP TABLE IF EXISTS `tavoite_saavutettu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tavoite_saavutettu` (
  `herkkumaara` int(11) DEFAULT NULL,
  `peli_id` int(11) NOT NULL,
  `tavoite_id` int(11) NOT NULL,
  PRIMARY KEY (`peli_id`,`tavoite_id`),
  KEY `tavoite_id` (`tavoite_id`),
  CONSTRAINT `tavoite_saavutettu_ibfk_1` FOREIGN KEY (`peli_id`) REFERENCES `peli` (`id`),
  CONSTRAINT `tavoite_saavutettu_ibfk_2` FOREIGN KEY (`tavoite_id`) REFERENCES `tavoite` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tavoite_saavutettu`
--

LOCK TABLES `tavoite_saavutettu` WRITE;
/*!40000 ALTER TABLE `tavoite_saavutettu` DISABLE KEYS */;
/*!40000 ALTER TABLE `tavoite_saavutettu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-08 16:11:04
