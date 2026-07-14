-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: weather_tracker
-- ------------------------------------------------------
-- Server version	8.0.45

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `weather_data`
--

DROP TABLE IF EXISTS `weather_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `weather_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `city` varchar(100) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `temperature` float DEFAULT NULL,
  `humidity` int DEFAULT NULL,
  `pressure` float DEFAULT NULL,
  `wind_speed` float DEFAULT NULL,
  `weather_condition` varchar(100) DEFAULT NULL,
  `fetched_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weather_data`
--

LOCK TABLES `weather_data` WRITE;
/*!40000 ALTER TABLE `weather_data` DISABLE KEYS */;
INSERT INTO `weather_data` VALUES (1,'Hyderabad','India',17.3753,78.4744,24.4,78,1005,30.6,'Partly Cloudy','2026-07-08 00:18:00'),(3,'Mumbai','India',18.975,72.826,27.2,94,1001,37.4,'Moderate or heavy rain with thunder','2026-07-08 00:26:00'),(5,'Kolkata','India',22.5697,88.3697,29.2,89,1002,20.2,'Mist','2026-07-08 00:27:00'),(6,'Chicago','United States of America',41.85,-87.65,25,50,1018,5.8,'Clear','2026-07-07 22:38:00'),(7,'Hyderabad','India',17.3753,78.4744,26.3,74,1007,39.6,'Mist','2026-07-08 09:12:00'),(8,'Hyderabad','India',17.3753,78.4744,27.1,70,1007,39.6,'Mist','2026-07-08 10:02:00'),(9,'Hyderabad','India',17.3753,78.4744,28.3,66,1008,26.6,'Mist','2026-07-08 23:42:00'),(10,'Hyderabad','India',17.3753,78.4744,28.3,66,1008,26.6,'Mist','2026-07-08 23:42:00'),(11,'Mumbai','India',18.975,72.826,29.2,84,1005,29.5,'Mist','2026-07-08 23:47:00'),(12,'Hyderabad','India',17.3753,78.4744,28.3,66,1008,26.6,'Mist','2026-07-08 23:47:00'),(13,'Jagtial','India',18.8,78.9333,26.9,68,1004,15.8,'Partly Cloudy','2026-07-08 23:48:00'),(14,'Hyderabad','India',17.3753,78.4744,28.3,66,1008,26.6,'Mist','2026-07-08 23:51:00'),(15,'Hyderabad','India',17.3753,78.4744,26.3,72,1006,26.6,'Clear','2026-07-09 00:00:00'),(16,'Mumbai','India',18.975,72.826,29.1,89,1006,30.6,'Mist','2026-07-09 09:24:00'),(17,'Mumbai','India',18.975,72.826,29.3,89,1006,30.6,'Mist','2026-07-09 09:28:00'),(18,'Kolkata','India',22.5697,88.3697,30.4,84,1002,22,'Mist','2026-07-09 09:45:00'),(19,'Jagtial','India',18.8,78.9333,27.1,78,1006,15.8,'Overcast','2026-07-09 09:54:00'),(20,'London','United Kingdom',51.5171,-0.1062,18.2,83,1018,6.5,'Sunny','2026-07-09 05:24:00'),(21,'Hyderabad','India',17.3753,78.4744,24.1,89,1011,29.2,'Light drizzle','2026-07-09 10:07:00'),(22,'Hyderabad','India',17.3753,78.4744,29.1,62,1010,25.2,'Mist','2026-07-10 00:42:00'),(23,'Medchal','India',17.6297,78.4814,29.1,62,1010,25.6,'Mist','2026-07-10 00:42:00'),(24,'Karimnagar','India',18.4333,79.15,27.3,74,1004,15.8,'Patchy rain nearby','2026-07-10 00:42:00'),(25,'Lisbon','Portugal',38.7167,-9.1333,21.3,69,1013,23,'Sunny','2026-07-09 20:32:00'),(26,'Sirsilla','India',18.3833,78.8333,29.7,47,1004,16.9,'Clear','2026-07-12 21:10:00'),(27,'Hyderabad','India',17.3753,78.4744,31.1,49,1007,22.3,'Mist','2026-07-12 22:09:00'),(28,'Hyderabad','India',17.3753,78.4744,31.1,49,1007,22.3,'Mist','2026-07-12 22:12:00'),(29,'Rajiv Gandhi International Airport','India',17.2313,78.4299,26.3,65,1009,26.6,'Mist','2026-07-13 08:44:00'),(30,'Hyderabad','India',17.3753,78.4744,26.4,65,1009,27.7,'Mist','2026-07-13 08:58:00'),(31,'Hyderabad','India',17.3753,78.4744,26.4,65,1009,27.7,'Mist','2026-07-13 09:01:00'),(32,'Hyderabad','India',17.3753,78.4744,26.4,65,1009,27.7,'Mist','2026-07-13 09:01:00'),(33,'Hyderabad','India',17.3753,78.4744,26.4,65,1009,27.7,'Mist','2026-07-13 09:01:00'),(34,'Hyderabad','India',17.3753,78.4744,28.1,58,1010,26.6,'Mist','2026-07-13 10:11:00'),(35,'Hyderabad','India',17.3753,78.4744,28.1,58,1010,26.6,'Mist','2026-07-13 10:15:00'),(36,'Hyderabad','India',17.3753,78.4744,28.1,58,1010,26.6,'Mist','2026-07-13 10:15:00'),(37,'Hyderabad','India',17.3753,78.4744,33.2,41,1008,26.6,'Mist','2026-07-13 13:45:00'),(38,'Jagtial','India',18.8,78.9333,36.4,32,1003,24.5,'Sunny','2026-07-13 13:46:00'),(39,'Mumbai','India',18.975,72.826,31.2,71,1008,26.3,'Mist','2026-07-13 13:46:00'),(40,'Kolkata','India',22.5697,88.3697,27.2,94,999,19.4,'Moderate or heavy rain with thunder','2026-07-13 13:46:00'),(41,'Pune','India',18.5333,73.8667,28.5,59,1008,31.7,'Sunny','2026-07-13 13:46:00'),(42,'Solapur','India',17.6833,75.9167,33.3,56,1009,24.8,'Overcast','2026-07-13 13:46:00'),(43,'Warangal','India',18,79.5833,36.3,32,1003,25.6,'Sunny','2026-07-13 13:46:00'),(44,'Karimnagar','India',18.4333,79.15,36.4,32,1003,24.8,'Sunny','2026-07-13 13:47:00'),(45,'Bengaluru','India',12.9833,77.5833,30.4,55,1013,20.5,'Sunny','2026-07-13 13:47:00'),(46,'Hyderabad','India',17.3753,78.4744,33.2,41,1008,26.6,'Mist','2026-07-13 13:45:00'),(47,'Hyderabad','India',17.3753,78.4744,33.2,41,1008,26.6,'Mist','2026-07-13 13:45:00'),(48,'Secunderabad','India',17.45,78.5,33.3,41,1008,25.9,'Mist','2026-07-13 13:48:00'),(49,'Silguri','India',26.7161,88.4236,30.2,84,999,9.4,'Light rain','2026-07-13 13:48:00'),(50,'London','United Kingdom',51.5171,-0.1062,18,73,1023,22,'Partly cloudy','2026-07-13 09:18:00'),(51,'Chicago','United States of America',41.85,-87.65,22.2,66,1022,3.6,'Clear','2026-07-13 03:18:00'),(52,'Chicago','United States of America',41.85,-87.65,22.2,66,1022,3.6,'Clear','2026-07-13 03:18:00'),(53,'Lisbon','Portugal',38.7167,-9.1333,20.3,83,1016,3.6,'Partly Cloudy','2026-07-13 09:19:00');
/*!40000 ALTER TABLE `weather_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-14  7:47:34
