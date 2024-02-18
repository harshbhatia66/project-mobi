-- MySQL dump 10.13  Distrib 8.2.0, for macos13.5 (arm64)
--
-- Host: localhost    Database: mobi_db
-- ------------------------------------------------------
-- Server version	8.2.0

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add set',7,'add_set'),(26,'Can change set',7,'change_set'),(27,'Can delete set',7,'delete_set'),(28,'Can view set',7,'view_set'),(29,'Can add user',8,'add_user'),(30,'Can change user',8,'change_user'),(31,'Can delete user',8,'delete_user'),(32,'Can view user',8,'view_user'),(33,'Can add workout session',9,'add_workoutsession'),(34,'Can change workout session',9,'change_workoutsession'),(35,'Can delete workout session',9,'delete_workoutsession'),(36,'Can view workout session',9,'view_workoutsession'),(37,'Can add workout template',10,'add_workouttemplate'),(38,'Can change workout template',10,'change_workouttemplate'),(39,'Can delete workout template',10,'delete_workouttemplate'),(40,'Can view workout template',10,'view_workouttemplate'),(41,'Can add template exercise',11,'add_templateexercise'),(42,'Can change template exercise',11,'change_templateexercise'),(43,'Can delete template exercise',11,'delete_templateexercise'),(44,'Can view template exercise',11,'view_templateexercise'),(45,'Can add exercise',12,'add_exercise'),(46,'Can change exercise',12,'change_exercise'),(47,'Can delete exercise',12,'delete_exercise'),(48,'Can view exercise',12,'view_exercise'),(49,'Can add session exercise',13,'add_sessionexercise'),(50,'Can change session exercise',13,'change_sessionexercise'),(51,'Can delete session exercise',13,'delete_sessionexercise'),(52,'Can view session exercise',13,'view_sessionexercise'),(53,'Can add user progress',14,'add_userprogress'),(54,'Can change user progress',14,'change_userprogress'),(55,'Can delete user progress',14,'delete_userprogress'),(56,'Can view user progress',14,'view_userprogress'),(57,'Can add Token',15,'add_token'),(58,'Can change Token',15,'change_token'),(59,'Can delete Token',15,'delete_token'),(60,'Can view Token',15,'view_token'),(61,'Can add token',16,'add_tokenproxy'),(62,'Can change token',16,'change_tokenproxy'),(63,'Can delete token',16,'delete_tokenproxy'),(64,'Can view token',16,'view_tokenproxy'),(65,'Can add user profile',17,'add_userprofile'),(66,'Can change user profile',17,'change_userprofile'),(67,'Can delete user profile',17,'delete_userprofile'),(68,'Can view user profile',17,'view_userprofile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$0WLcNad4k0mFpNqFLS7Atf$IsOo/gLthZH/uWltwfGf6ds5pbup+MAJHMGC9f8zqeA=','2024-02-09 04:54:04.212352',1,'harshbhatia','','','',1,1,'2023-12-21 07:18:13.692145'),(5,'pbkdf2_sha256$600000$Xi7sgO5uAFNG3y2ZDgfEIB$3a+ehr0TvDVS5W+3bRkSdp9gS+Y7vGFOhpYRQiqRtiE=',NULL,0,'manraj','','','test@gmail.com',0,1,'2023-12-22 04:13:14.000000'),(6,'pbkdf2_sha256$600000$fe0SMBVguNG8DJsVyAKTyy$wuHFHp1DD6/71/LxYA2PI/KkD9SfnrgyHQD7q7wnaD4=',NULL,0,'shaleen','','','test@gmail.com',0,1,'2023-12-22 04:13:14.000000'),(7,'pbkdf2_sha256$600000$UFKPjosghq4FRAjKpB7jPP$u1+2QFUgCOMVA4cSD01kCfJwarXmQkEdWHiH46R/Bdo=',NULL,0,'aryan','','','test@gmail.com',0,1,'2023-12-22 04:13:14.000000'),(8,'pbkdf2_sha256$600000$IbiCSdh1pFDTWq5NS2o1hS$oWWAOysCUAKc0MX5LuFjGxfe6nw0Q+pz8+WReIw+f0k=',NULL,0,'sachveer','','','test@gmail.com',0,1,'2023-12-22 04:13:14.000000'),(9,'pbkdf2_sha256$600000$2ihsBhT1j2FAYz3o4qUNeG$b+WgBTSUiC19oS+UG8ozRgdMKUCjSbE7GSIHh0I/NuM=',NULL,0,'sukhman','','','test@gmail.com',0,1,'2023-12-22 04:13:14.000000'),(10,'pbkdf2_sha256$600000$2HHzQHWuhYxiQwyB9NJp9n$vCA9ZquQAmDtyFZtVtxU612gk09JZqq/NqD/BePTjkM=',NULL,0,'rayman','','','test@gmail.com',0,1,'2023-12-22 04:13:14.000000'),(11,'pbkdf2_sha256$600000$TlOKsMnh67QK954llmLlhV$kAnUhxQ9KydVbDywlvVXY3FbeRMaQsAEprTTIgZ1rqM=',NULL,0,'harry','','','test@gmail.com',0,1,'2023-12-22 04:13:14.000000'),(16,'!XpnwvTrsXAI9G8OEXS1bY3fGRpq0ip4K4WiXCgcQ',NULL,0,'jrPse6W3MCduQ9LAVh17Zjucw8i1','','','',0,1,'2024-01-26 05:19:46.817938'),(28,'',NULL,0,'IP6UIPyu7dMoER5sbnPAAEd6mby1','','','harsh@gmail.com',0,1,'2024-01-31 04:18:53.099494');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
INSERT INTO `authtoken_token` VALUES ('e445512134e867f974d0fa91ad5fdd19f97bc1fa','2024-01-31 04:18:53.100755',28);
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-12-22 04:12:10.021120','2','manraj',1,'[{\"added\": {}}]',4,1),(2,'2023-12-22 04:12:59.673176','2','manraj',3,'',4,1),(3,'2023-12-22 04:13:43.964416','1','User object (1)',1,'[{\"added\": {}}]',8,1),(4,'2023-12-22 04:14:38.658625','2','User object (2)',1,'[{\"added\": {}}]',8,1),(5,'2023-12-22 04:14:53.407780','3','User object (3)',1,'[{\"added\": {}}]',8,1),(6,'2023-12-22 04:15:02.914941','4','User object (4)',1,'[{\"added\": {}}]',8,1),(7,'2023-12-22 04:15:17.571921','5','User object (5)',1,'[{\"added\": {}}]',8,1),(8,'2023-12-22 04:15:26.932255','6','User object (6)',1,'[{\"added\": {}}]',8,1),(9,'2023-12-22 04:15:34.685545','7','User object (7)',1,'[{\"added\": {}}]',8,1),(10,'2023-12-22 04:24:30.346980','8','User object (8)',1,'[{\"added\": {}}]',8,1),(11,'2023-12-22 06:17:53.273576','4','oppenheimer',3,'',4,1),(12,'2023-12-22 06:17:53.276108','3','yash',3,'',4,1),(13,'2024-01-26 04:53:38.125089','11','8a1b26df7d9d2fe8a633aa1c2e30e9a125c7e0bc',3,'',16,1),(14,'2024-01-26 04:53:40.857816','10','c4510b5bd4299b712d4bd4d45120804c5ef01edb',3,'',16,1),(15,'2024-01-26 04:53:43.551745','9','909453871b49e090369ab3977a28e8890adc9313',3,'',16,1),(16,'2024-01-26 04:53:46.721829','8','e5f8878719dc0aeaee6f681dfdc3d6be0a90f9af',3,'',16,1),(17,'2024-01-26 04:53:49.517418','7','f446066dcc7601ad3abe20f3f5be42a5f0de42c1',3,'',16,1),(18,'2024-01-26 04:53:52.166620','6','c52bf1c458c884549f70b6d6990b125a7fe57d02',3,'',16,1),(19,'2024-01-26 04:53:54.385871','5','928983875cfb55ad584672b1102a8bd40e6cf2c1',3,'',16,1),(20,'2024-01-26 04:53:56.749708','1','fbec88a0d5fe88d02c977eb71d0bd0c5f7244999',3,'',16,1),(21,'2024-02-01 08:44:54.258234','1','Exercise object (1)',2,'[{\"changed\": {\"fields\": [\"User\"]}}]',12,1),(22,'2024-02-13 05:37:14.082116','32','Exercise object (32)',3,'',12,1),(23,'2024-02-13 05:37:14.084879','31','Exercise object (31)',3,'',12,1),(24,'2024-02-13 05:37:14.085930','30','Exercise object (30)',3,'',12,1),(25,'2024-02-13 05:37:14.086898','29','Exercise object (29)',3,'',12,1),(26,'2024-02-13 05:37:14.087693','28','Exercise object (28)',3,'',12,1),(27,'2024-02-13 05:37:14.088235','27','Exercise object (27)',3,'',12,1),(28,'2024-02-13 05:37:14.088694','26','Exercise object (26)',3,'',12,1),(29,'2024-02-13 05:37:14.089174','25','Exercise object (25)',3,'',12,1),(30,'2024-02-13 05:37:14.089647','24','Exercise object (24)',3,'',12,1),(31,'2024-02-13 05:37:14.090095','23','Exercise object (23)',3,'',12,1),(32,'2024-02-13 05:37:14.090555','22','Exercise object (22)',3,'',12,1),(33,'2024-02-13 05:37:14.091004','21','Exercise object (21)',3,'',12,1),(34,'2024-02-13 05:37:14.091444','20','Exercise object (20)',3,'',12,1),(35,'2024-02-13 05:37:14.092086','19','Exercise object (19)',3,'',12,1),(36,'2024-02-13 05:37:14.092737','18','Exercise object (18)',3,'',12,1),(37,'2024-02-13 05:37:14.093415','17','Exercise object (17)',3,'',12,1),(38,'2024-02-13 05:37:14.094068','16','Exercise object (16)',3,'',12,1),(39,'2024-02-13 05:37:14.094536','15','Exercise object (15)',3,'',12,1),(40,'2024-02-13 05:37:14.094980','14','Exercise object (14)',3,'',12,1),(41,'2024-02-13 05:37:14.095713','13','Exercise object (13)',3,'',12,1),(42,'2024-02-13 05:37:14.096363','12','Exercise object (12)',3,'',12,1),(43,'2024-02-13 05:37:14.097230','11','Exercise object (11)',3,'',12,1),(44,'2024-02-13 05:37:14.097851','10','Exercise object (10)',3,'',12,1),(45,'2024-02-13 05:37:14.098429','9','Exercise object (9)',3,'',12,1),(46,'2024-02-13 05:37:14.098908','8','Exercise object (8)',3,'',12,1),(47,'2024-02-13 05:37:14.099281','7','Exercise object (7)',3,'',12,1),(48,'2024-02-13 05:37:14.099610','6','Exercise object (6)',3,'',12,1),(49,'2024-02-13 05:37:14.099982','5','Exercise object (5)',3,'',12,1),(50,'2024-02-13 05:37:14.100343','4','Exercise object (4)',3,'',12,1),(51,'2024-02-13 05:37:14.100725','3','Exercise object (3)',3,'',12,1),(52,'2024-02-13 05:37:14.102579','2','Exercise object (2)',3,'',12,1),(53,'2024-02-13 05:37:14.103056','1','Exercise object (1)',3,'',12,1),(54,'2024-02-18 00:27:55.805654','64','Exercise object (64)',2,'[{\"changed\": {\"fields\": [\"User\", \"Equipment type\"]}}]',12,1),(55,'2024-02-18 00:28:12.162634','60','Exercise object (60)',2,'[{\"changed\": {\"fields\": [\"Function\"]}}]',12,1),(56,'2024-02-18 00:28:22.169146','59','Exercise object (59)',2,'[{\"changed\": {\"fields\": [\"Function\"]}}]',12,1),(57,'2024-02-18 00:28:28.966418','58','Exercise object (58)',2,'[{\"changed\": {\"fields\": [\"Function\"]}}]',12,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(15,'authtoken','token'),(16,'authtoken','tokenproxy'),(5,'contenttypes','contenttype'),(12,'mobi_app','exercise'),(13,'mobi_app','sessionexercise'),(7,'mobi_app','set'),(11,'mobi_app','templateexercise'),(8,'mobi_app','user'),(17,'mobi_app','userprofile'),(14,'mobi_app','userprogress'),(9,'mobi_app','workoutsession'),(10,'mobi_app','workouttemplate'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-12-21 05:56:44.421104'),(2,'auth','0001_initial','2023-12-21 05:56:44.477580'),(3,'admin','0001_initial','2023-12-21 05:56:44.495230'),(4,'admin','0002_logentry_remove_auto_add','2023-12-21 05:56:44.498292'),(5,'admin','0003_logentry_add_action_flag_choices','2023-12-21 05:56:44.500933'),(6,'contenttypes','0002_remove_content_type_name','2023-12-21 05:56:44.513899'),(7,'auth','0002_alter_permission_name_max_length','2023-12-21 05:56:44.523202'),(8,'auth','0003_alter_user_email_max_length','2023-12-21 05:56:44.529682'),(9,'auth','0004_alter_user_username_opts','2023-12-21 05:56:44.532229'),(10,'auth','0005_alter_user_last_login_null','2023-12-21 05:56:44.540689'),(11,'auth','0006_require_contenttypes_0002','2023-12-21 05:56:44.541283'),(12,'auth','0007_alter_validators_add_error_messages','2023-12-21 05:56:44.544095'),(13,'auth','0008_alter_user_username_max_length','2023-12-21 05:56:44.554106'),(14,'auth','0009_alter_user_last_name_max_length','2023-12-21 05:56:44.563386'),(15,'auth','0010_alter_group_name_max_length','2023-12-21 05:56:44.569081'),(16,'auth','0011_update_proxy_permissions','2023-12-21 05:56:44.572999'),(17,'auth','0012_alter_user_first_name_max_length','2023-12-21 05:56:44.583965'),(18,'sessions','0001_initial','2023-12-21 05:56:44.588951'),(19,'mobi_app','0001_initial','2023-12-21 07:24:33.998856'),(20,'mobi_app','0002_rename_date_of_joining_user_date_joined','2023-12-22 05:48:07.811907'),(21,'authtoken','0001_initial','2023-12-23 04:10:39.842262'),(22,'authtoken','0002_auto_20160226_1747','2023-12-23 04:10:39.852102'),(23,'authtoken','0003_tokenproxy','2023-12-23 04:10:39.853106'),(24,'mobi_app','0003_alter_sessionexercise_exercise_and_more','2023-12-23 04:16:58.520465'),(25,'mobi_app','0004_alter_workouttemplate_created_at','2023-12-23 04:51:49.794857'),(26,'mobi_app','0005_alter_workoutsession_end_time_and_more','2023-12-27 11:31:24.616054'),(27,'mobi_app','0006_alter_set_notes_alter_set_reps_alter_set_weight','2024-01-08 00:25:31.160106'),(28,'mobi_app','0007_exercise_user','2024-01-14 05:04:50.896507'),(29,'mobi_app','0008_alter_exercise_user_and_more','2024-01-19 08:09:47.120724'),(30,'mobi_app','0009_alter_workoutsession_workout_template','2024-01-21 05:47:40.285977'),(31,'mobi_app','0010_alter_workoutsession_workout_template_userprofile','2024-01-26 04:24:52.963874'),(32,'mobi_app','0011_delete_userprofile','2024-01-31 04:18:23.597598'),(33,'mobi_app','0012_exercise_equipment_type_exercise_function_and_more','2024-02-09 04:53:30.634363');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1khpc6yoiamhtzktj4wobru9uamjt1sd','e30:1rTE6U:J1IPVYhHFRm9ICvCHiYVXnap7bEz7Vrg7ftRYAlrpDI','2024-02-09 04:46:10.532567'),('3krm5nug7ugpcbzskl7ppjt9em28taby','e30:1rTE4P:RAaTfJDv2frCNn8VxCv36PTgTw7_pbofudSUywlMPeQ','2024-02-09 04:44:01.349190'),('8aunz60uck5pc2focu45u2kma7xgbeiy','.eJxVjDsOwyAQBe9CHSGMMZ-U6X0GtOxCcBKBZOwqyt2DJRdJ-2bmvZmHfct-b3H1C7ErG9jldwuAz1gOQA8o98qxlm1dAj8UftLG50rxdTvdv4MMLfdaCS30IBJKKYUZLagwGtQiAmlEmkA6tMlO0rjUvdFaBb2RDkJARY59vr4bNzc:1rTEAT:Y_HO4xkMmpkgodbzYOV0RIEpPBxLah6JVERbMaXIFj4','2024-02-09 04:50:17.072720'),('b8ysvx00b9nxjwpvad31fm6waij2lbgo','e30:1rTE1L:dFOjxvG4-oeo2jTTEUJGhp2bYAdMYWpgYZLyJZ1UrWo','2024-02-09 04:40:51.424366'),('zlk2uzp9j54h7acwuhy19p96biy1zusb','.eJxVjDsOwyAQBe9CHSGMMZ-U6X0GtOxCcBKBZOwqyt2DJRdJ-2bmvZmHfct-b3H1C7ErG9jldwuAz1gOQA8o98qxlm1dAj8UftLG50rxdTvdv4MMLfdaCS30IBJKKYUZLagwGtQiAmlEmkA6tMlO0rjUvdFaBb2RDkJARY59vr4bNzc:1rYIto:0tebuGRx0GAACcA3_siNPS9PUbPin_3tA_u-UeILb_M','2024-02-23 04:54:04.213802'),('zwr92q5mnuqxsusn4yhl0d38ua09ftfm','.eJxVjDsOwyAQBe9CHSGMMZ-U6X0GtOxCcBKBZOwqyt2DJRdJ-2bmvZmHfct-b3H1C7ErG9jldwuAz1gOQA8o98qxlm1dAj8UftLG50rxdTvdv4MMLfdaCS30IBJKKYUZLagwGtQiAmlEmkA6tMlO0rjUvdFaBb2RDkJARY59vr4bNzc:1rGDKX:HtXh6ofODxM2sQWGIkb3uFOvp04z1nQJLmpeXJLKgPg','2024-01-04 07:18:53.404199');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mobi_app_exercise`
--

DROP TABLE IF EXISTS `mobi_app_exercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mobi_app_exercise` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `type` varchar(255) NOT NULL,
  `user_id` int DEFAULT NULL,
  `equipment_type` varchar(255) NOT NULL,
  `function` varchar(255) NOT NULL,
  `gif` varchar(100) DEFAULT NULL,
  `history` json DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `instructions` longtext NOT NULL DEFAULT (_utf8mb3''),
  PRIMARY KEY (`id`),
  KEY `mobi_app_exercise_user_id_da3135d6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `mobi_app_exercise_user_id_da3135d6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobi_app_exercise`
--

LOCK TABLES `mobi_app_exercise` WRITE;
/*!40000 ALTER TABLE `mobi_app_exercise` DISABLE KEYS */;
INSERT INTO `mobi_app_exercise` VALUES (33,'Incline Bench Press (Smith Machine)','Incline Smith machine bench press: a compound exercise targeting the upper chest, shoulders, and triceps, performed on an inclined bench with a guided barbell.','Strength',NULL,'Machine','Chest','media/exercise_gifs/0757.gif',NULL,'media/exercise_images/Screenshot_2024-02-17_at_2.16.36pm.png','[\"Adjust bench to 30-45 degree incline.\", \"Sit with back flat, feet on ground.\", \"Grasp barbell shoulder-width apart.\", \"Unrack and lower barbell to upper chest, elbows slightly tucked.\", \"Pause, then push barbell back up.\", \"Repeat desired reps.\"]'),(34,'Iso-Lateral Flat Bench Press','An exercise performed on a bench press machine with independent handles, targeting the chest and triceps.','Strength',NULL,'Machine','Chest','',NULL,'media/exercise_images/3015-2-Exigo-ISO-Lateral-Flat-Chest-Press-2000x2286px.png','[\"Adjust seat and handles.\", \"Sit on bench with back against pad, feet flat.\", \"Grasp handles with arms extended.\", \"Push handles forward until arms are straight, then lower to chest.\", \"Pause briefly, then push handles back up.\", \"Repeat for desired reps.\"]'),(35,'Iso-Lateral D.Y. Row','An exercise performed on a machine with independent handles, targeting the back muscles, particularly the lats and rhomboids.','Strength',NULL,'Machine','Back','',NULL,'media/exercise_images/IL-DRW-MIDBLK-Iso-Lateral-D.Y.-Row-720x720.jpg.png','[\"Adjust the seat and handles to a comfortable position.\", \"Sit on the machine with your chest against the pad and feet flat on the floor.\", \"Grasp the handles with an overhand grip, arms extended.\", \"Pull the handles toward your sides, squeezing your shoulder blades together.\", \"Pause briefly at the peak contraction, then slowly release back to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(36,'Chest Dip','A bodyweight exercise performed on parallel bars, targeting the chest, shoulders, and triceps.','Strength',NULL,'Machine','Chest','media/exercise_gifs/0251.gif',NULL,'media/exercise_images/tmpuymcke3z.jpg','[\"Position yourself on parallel bars with your arms fully extended and your body straight.\", \"Lower your body by bending your elbows until your shoulders are below your elbows.\", \"Push yourself back up to the starting position by straightening your arms.\", \"Repeat for the desired number of repetitions.\"]'),(37,'Lat Pulldown (Cable)','A strength training exercise targeting the latissimus dorsi muscles, performed using a cable machine with a wide, overhand grip.','Strength',NULL,'Machine','Back','media/exercise_gifs/0198.gif',NULL,'media/exercise_images/tmpnl3doe4b.jpg','[\"Adjust the cable pulldown machine so that the seat is at a comfortable height and the knee pad is secured.\", \"Sit on the seat with your back straight and your feet flat on the ground.\", \"Grasp the cable bar with an overhand grip, slightly wider than shoulder-width apart.\", \"Lean back slightly and engage your core.\", \"Pull the cable bar down towards your chest, squeezing your shoulder blades together.\", \"Pause for a moment at the bottom of the movement, then slowly release the bar back to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(38,'Close Grip Seated Row (Cable)','A strength training exercise targeting the back muscles, particularly the latissimus dorsi and rhomboids, performed using a cable machine with a neutral grip.','Strength',NULL,'Machine','Back','media/exercise_gifs/0239.gif',NULL,'media/exercise_images/tmpbt4zaoa7.jpg','[\"Sit on the machine with your feet flat on the footrests and knees slightly bent.\", \"Grasp the handles with a neutral grip (palms facing each other), arms extended.\", \"Pull the handles towards your torso, squeezing your shoulder blades together.\", \"Keep your back straight and chest lifted throughout the movement.\", \"Slowly release the handles back to the starting position, maintaining control.\", \"Repeat for the desired number of repetitions.\"]'),(39,'Incline Chest Fly (Machine)','A strength training exercise targeting the chest muscles, particularly the pectoralis major, performed on a machine with adjustable seat.','Strength',NULL,'Machine','Chest','',NULL,'media/exercise_images/Screenshot_2024-02-14_at_3.45.05pm.png','[\"Adjust the seat and handles to a comfortable position.\", \"Sit on the machine with your back against the pad and feet flat on the floor.\", \"Grasp the handles with a neutral grip (palms facing each other), arms extended.\", \"Bring the handles together in front of your chest, keeping a slight bend in your elbows.\", \"Open your arms wide, lowering the handles out to the sides in a controlled motion.\", \"Squeeze your chest muscles as you bring the handles back together in front of your chest.\", \"Repeat for the desired number of repetitions.\"]'),(40,'Reverse Fly (Machine)','A strength training exercise targeting the rear deltoids and upper back muscles, performed on a machine with adjustable seat and handles.','Strength',NULL,'Machine','Shoulders','media/exercise_gifs/0601.gif',NULL,'media/exercise_images/tmplc1p9rs5.jpg','[\"Adjust the seat height and position yourself on the machine with your chest against the pad and your feet flat on the floor.\", \"Grasp the handles with a parallel grip, palms facing each other, and keep your arms slightly bent.\", \"Exhale and squeeze your shoulder blades together as you pull the handles back and outward, away from your body.\", \"Pause for a moment at the peak contraction, then inhale and slowly return to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(41,'Seated Calf Press','A strength training exercise targeting the calf muscles, particularly the gastrocnemius and soleus, performed on a machine with adjustable seat and foot platform.','Strength',NULL,'Machine','Calves','media/exercise_gifs/2335.gif',NULL,'media/exercise_images/tmppqu8mem4.jpg','[\"Adjust the seat of the machine so that your shoulders are aligned with the lever pad.\", \"Place your toes on the lower portion of the platform and position your knees under the lever pad.\", \"Grasp the handles on the sides of the seat for stability.\", \"Press the lever pad down by extending your ankles, lifting your heels as high as possible.\", \"Pause for a moment at the top of the movement, then slowly lower your heels back down to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(42,'Shoulder Press (Plate Loaded)','A strength training exercise targeting the shoulder muscles, particularly the deltoids, performed on a machine with adjustable seat and handles.','Strength',NULL,'Machine','Shoulders','media/exercise_gifs/0869.gif',NULL,'media/exercise_images/tmp2yrm3hwj.jpg','[\"Adjust the seat height and backrest of the leverage machine to a comfortable position.\", \"Sit on the machine with your back against the backrest and your feet flat on the floor.\", \"Grasp the handles of the machine with an overhand grip, slightly wider than shoulder-width apart.\", \"Push the handles upward and forward until your arms are fully extended, but not locked.\", \"Pause for a moment at the top, then slowly lower the handles back down to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(43,'Preacher Curl (Machine)','A strength training exercise targeting the biceps muscles, performed on a preacher curl bench to isolate the biceps and minimize cheating.','Strength',NULL,'Machine','Biceps','media/exercise_gifs/1614.gif',NULL,'media/exercise_images/tmpstjp8sq8.jpg','[\"Adjust the seat height and position yourself on the machine with your upper arms resting on the pad and your chest against the support.\", \"Grasp the handles with an underhand grip, slightly wider than shoulder-width apart.\", \"Keep your upper arms stationary and exhale as you curl the handles towards your shoulders, contracting your biceps.\", \"Pause for a moment at the top of the movement, squeezing your biceps.\", \"Inhale as you slowly lower the handles back to the starting position, fully extending your arms.\", \"Repeat for the desired number of repetitions.\"]'),(44,'Tricep Pushdown (Cable)','A strength training exercise targeting the triceps muscles, performed on a cable machine with a straight bar attachment to isolate and strengthen the triceps.','Strength',NULL,'Machine','Triceps','media/exercise_gifs/0201.gif',NULL,'media/exercise_images/tmpwiq88q7m.jpg','[\"Attach a straight bar to a high pulley cable machine.\", \"Stand facing the machine with your feet shoulder-width apart and a slight bend in your knees.\", \"Grasp the bar with an overhand grip, hands shoulder-width apart.\", \"Keep your elbows close to your sides and your upper arms stationary.\", \"Exhale and push the bar down until your elbows are fully extended.\", \"Pause for a moment, then inhale and slowly return the bar to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(45,'Lateral Raise (Dumbbell)','A shoulder exercise targeting the lateral deltoids, performed by lifting dumbbells out to the sides until they reach shoulder height.','Strength',NULL,'Dumbbell','Shoulders','media/exercise_gifs/0396.gif',NULL,'media/exercise_images/tmpza3xxwgc.jpg','[\"Sit on a bench with your feet flat on the ground and a dumbbell in each hand, resting on your thighs.\", \"Keep your back straight and core engaged.\", \"Raise the dumbbells to your sides with a slight bend in your elbows, until your arms are parallel to the ground.\", \"Pause for a moment at the top, then slowly lower the dumbbells back down to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(46,'incline Curl (Dumbbell)','A bicep exercise performed on an incline bench to target the biceps from a different angle, promoting muscle growth and strength.','Strength',NULL,'Dumbbell','Biceps','media/exercise_gifs/0318.gif',NULL,'media/exercise_images/tmpv8cfjhca.jpg','[\"Sit on an incline bench with a dumbbell in each hand, palms facing forward and arms fully extended.\", \"Keeping your upper arms stationary, exhale and curl the weights while contracting your biceps.\", \"Continue to raise the dumbbells until your biceps are fully contracted and the dumbbells are at shoulder level.\", \"Hold the contracted position for a brief pause as you squeeze your biceps.\", \"Inhale and slowly begin to lower the dumbbells back to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(47,'Skull Crusher (Dumbbell)','A tricep exercise performed lying down, involving lowering dumbbells towards the temples to target the triceps.','Strength',NULL,'Dumbbell','Triceps','',NULL,'media/exercise_images/Screenshot_2024-02-14_at_4.54.59pm.png','[\"Lie on a flat bench with a dumbbell in each hand, arms extended straight up above your chest.\", \"Lower the dumbbells towards your temples by bending your elbows, keeping them pointed towards the ceiling.\", \"Keep your upper arms stationary and lower the dumbbells until they are near your ears.\", \"Pause briefly, then extend your arms to press the dumbbells back up to the starting position.\", \"Maintain control throughout the movement and avoid locking out your elbows at the top.\", \"Repeat for the desired number of repetitions.\"]'),(48,'Hammer Curl (Dumbbell)','A bicep exercise performed with dumbbells, targeting the brachialis and brachioradialis muscles, with palms facing in towards the body.','Strength',NULL,'Dumbbell','Biceps','media/exercise_gifs/0313.gif',NULL,'media/exercise_images/tmp56v9b_5x.jpg','[\"Stand up straight with a dumbbell in each hand, palms facing your torso.\", \"Keep your elbows close to your torso and rotate the palms of your hands until they are facing forward.\", \"This will be your starting position.\", \"Now, keeping the upper arms stationary, exhale and curl the weights while contracting your biceps.\", \"Continue to raise the weights until your biceps are fully contracted and the dumbbells are at shoulder level.\", \"Hold the contracted position for a brief pause as you squeeze your biceps.\", \"Then, inhale and slowly begin to lower the dumbbells back to the starting position.\", \"Repeat for the recommended amount of repetitions.\"]'),(49,'Standing Lateral Raise (Machine)','A shoulder exercise performed on a machine with handles that allows you to lift weights out to the sides, targeting the lateral deltoids.','Strength',NULL,'Machine','Shoulders','',NULL,'media/exercise_images/9008_BG_WG_1.png','[\"Stand facing the lateral raise machine with your feet shoulder-width apart.\", \"Adjust the handles to a comfortable position and grasp them with an overhand grip.\", \"Keep your arms straight and lift the handles out to the sides until they reach shoulder height.\", \"Pause briefly at the top of the movement, then lower the handles back down under control.\", \"Focus on using your shoulder muscles to lift the weight, avoiding momentum.\", \"Repeat for the desired number of repetitions.\"]'),(50,'Barbell Standing Back Wrist Curl (Barbell)','A forearm exercise performed standing with a barbell held behind the back, targeting the wrist flexors.','Strength',NULL,'Barbell','Forearms','media/exercise_gifs/0104.gif',NULL,'media/exercise_images/tmpl53e_746.jpg','[\"Stand up straight with your feet shoulder-width apart and hold a barbell with an overhand grip.\", \"Rest the barbell on the back of your hands with your palms facing down and your fingers pointing towards your body.\", \"Keeping your upper arms stationary, exhale and curl your wrists upwards as far as possible.\", \"Hold the contracted position for a brief pause, then inhale and slowly lower the barbell back to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(51,'Reverse Grip Curl (Barbell)','A bicep exercise performed with a barbell using an underhand grip, targeting the biceps brachii and brachialis muscles.','Strength',NULL,'Barbell','Forearms','media/exercise_gifs/0110.gif',NULL,'media/exercise_images/tmp8ly_bafk.jpg','[\"Stand up straight with your feet shoulder-width apart and hold a barbell with an underhand grip, palms facing up.\", \"Keep your elbows close to your torso and your upper arms stationary.\", \"Exhale and curl the weights while contracting your biceps, bringing the barbell as close to your shoulders as possible.\", \"Hold the contracted position for a brief pause as you squeeze your biceps.\", \"Inhale and slowly lower the barbell back to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(52,'Standing Calf Raise (Machine)','A calf-strengthening exercise performed by lifting the heels as high as possible while standing, targeting the calf muscles.','Strength',NULL,'Machine','Calves','media/exercise_gifs/0605.gif',NULL,'media/exercise_images/tmptyk1gkje.jpg','[\"Adjust the machine to your height and stand with your feet shoulder-width apart.\", \"Place your shoulders under the pads and hold onto the handles for stability.\", \"Raise your heels as high as possible by extending your ankles.\", \"Pause for a moment at the top, then slowly lower your heels back down to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(53,'Leg Extension (Machine)','A lower body exercise targeting the quadriceps muscles, performed on a leg extension machine by extending the legs against resistance.','Strength',NULL,'Machine','Quadriceps','media/exercise_gifs/0585.gif',NULL,'media/exercise_images/tmpxls1ppr6.jpg','[\"Adjust the seat height and backrest of the machine to fit your body.\", \"Sit on the machine with your back against the backrest and your feet on the footpad.\", \"Grasp the handles or sidebars for stability.\", \"Extend your legs forward by straightening your knees, lifting the weight.\", \"Pause for a moment at the top, then slowly lower the weight back to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(54,'Seated Leg Curl (Machine)','A lower body exercise targeting the hamstrings, performed on a leg curl machine by flexing the knees against resistance.','Strength',NULL,'Machine','Hamstrings','media/exercise_gifs/0599.gif',NULL,'media/exercise_images/tmpbhmn5sdf.jpg','[\"Adjust the machine to fit your body and sit on it with your back against the backrest.\", \"Place your lower legs under the padded lever, just above your ankles.\", \"Grasp the handles on the sides of the machine for support.\", \"Keeping your upper legs stationary, exhale and curl your legs up as far as possible.\", \"Hold the contracted position for a brief pause as you squeeze your hamstrings.\", \"Inhale and slowly lower the lever back to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(55,'Hack Squat (Machine)','A compound lower body exercise targeting the quadriceps, performed on a hack squat machine by squatting with the assistance of a backrest and shoulder pads.','Strength',NULL,'Machine','Quadriceps','media/exercise_gifs/0743.gif',NULL,'media/exercise_images/tmp2qbx4740.jpg','[\"Adjust the sled machine to a comfortable position for your height.\", \"Stand with your feet shoulder-width apart on the platform, toes slightly pointed outwards.\", \"Hold onto the handles or bars for stability.\", \"Lower your body by bending your knees and hips, keeping your back straight and chest up.\", \"Continue lowering until your thighs are parallel to the ground or slightly below.\", \"Pause for a moment, then push through your heels to raise your body back up to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(56,'Captain\'s Chair Leg Raises','A bodyweight exercise targeting the lower abdominal muscles, performed on a captain\'s chair by lifting the legs upward while hanging from the armrests.','Strength',NULL,'Weighted Bodyweight','Abs','media/exercise_gifs/2963.gif',NULL,'media/exercise_images/tmps0vacukc.jpg','[\"Sit on the captain\'s chair with your back against the backrest and your forearms resting on the arm pads.\", \"Keep your upper body stable and your back straight.\", \"Engage your abs and lift your legs up in front of you, keeping them straight.\", \"Continue lifting until your legs are parallel to the ground or as high as you can comfortably go.\", \"Pause for a moment at the top, then slowly lower your legs back down to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(57,'Seated Crunch (Machine)','An abdominal exercise targeting the rectus abdominis, performed on a machine with a backrest and foot pads for stabilization.','Strength',NULL,'Machine','Abs','media/exercise_gifs/1452.gif',NULL,'media/exercise_images/tmp1co6tj8e.jpg','[\"Sit on the leverage machine with your back against the pad and your feet flat on the floor.\", \"Grasp the handles or place your hands on the side pads for support.\", \"Engage your abs and slowly lean back, allowing the pad to move with you.\", \"Once your upper body is at a 45-degree angle, contract your abs and crunch forward, bringing your chest towards your knees.\", \"Pause for a moment at the top, then slowly release and return to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(58,'Single Leg Press (Machine)','A lower body exercise targeting the quadriceps, hamstrings, and glutes, performed on a leg press machine with a single weight plate on the footplate.','Strength',NULL,'Machine','Quadriceps','media/exercise_gifs/2287.gif',NULL,'media/exercise_images/tmprjxb6amb.jpg','[\"Adjust the seat and foot platform of the leverage machine to your desired position.\", \"Sit on the machine with your back against the backrest and your feet on the foot platform.\", \"Place your hands on the handles or sides of the machine for stability.\", \"Push one foot against the foot platform, extending your leg until it is almost fully straight.\", \"Pause for a moment, then slowly bend your leg and return to the starting position.\", \"Repeat with the other leg.\", \"Continue alternating legs for the desired number of repetitions.\"]'),(59,'Leg Press (Machine)','A lower body exercise targeting the quadriceps, hamstrings, and glutes, performed on a leg press machine with a single weight plate on the footplate.','Strength',NULL,'Machine','Quadriceps','media/exercise_gifs/1463.gif',NULL,'media/exercise_images/tmp8ubk7k2d.jpg','[\"Adjust the seat of the sled machine so that your knees are at a 90-degree angle when your feet are on the footplate.\", \"Sit on the sled machine with your back flat against the backrest and your feet shoulder-width apart on the footplate.\", \"Grip the handles on the sides of the seat for stability.\", \"Push against the footplate to extend your legs, straightening them completely.\", \"Pause for a moment at the top, then slowly bend your knees to lower the footplate back to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(60,'Romanian Deadlift (RDLs - Barbell)','A hamstring and glute exercise that involves hinging at the hips to lower a barbell towards the ground while keeping the back straight, focusing on the stretch in the hamstrings.','Strength',NULL,'Barbell','Hamstrings','media/exercise_gifs/0085.gif',NULL,'media/exercise_images/tmp7cgzppc3.jpg','[\"Stand with your feet shoulder-width apart and your toes pointing forward.\", \"Hold the barbell with an overhand grip, hands slightly wider than shoulder-width apart.\", \"Bend at the hips, keeping your back straight and your knees slightly bent.\", \"Lower the barbell towards the ground, keeping it close to your body.\", \"Feel the stretch in your hamstrings as you lower the barbell.\", \"Once you feel a stretch in your hamstrings, push your hips forward and stand up straight.\", \"Squeeze your glutes at the top of the movement.\", \"Lower the barbell back down to the starting position and repeat for the desired number of repetitions.\"]'),(61,'Single Reverse Wrist Curl (Dumbbell)','A forearm exercise targeting the wrist extensor muscles, performed one arm at a time with a dumbbell, focusing on lifting the weight by flexing the wrist.','Strength',NULL,'Dumbbell','Forearms','media/exercise_gifs/0358.gif',NULL,'media/exercise_images/tmp4tw6p4yi.jpg','[\"Sit on a bench or chair with your feet flat on the ground.\", \"Hold a dumbbell in one hand with an overhand grip, palm facing down.\", \"Rest your forearm on your thigh, with your wrist hanging off the edge.\", \"Slowly lower the dumbbell towards the ground by flexing your wrist.\", \"Pause for a moment at the bottom, then slowly curl your wrist back up towards your body.\", \"Repeat for the desired number of repetitions, then switch to the other arm.\"]'),(62,'Iso-Lateral Low Row (Machine)','A back exercise performed on a machine with independent handles, targeting the latissimus dorsi and other back muscles.','Strength',NULL,'Machine','Back','',NULL,'media/exercise_images/IL-LR-MIDBLK-Iso-Lateral-Low-Row.png','[\"Sit on the machine with your chest against the pad and feet flat on the floor.\", \"Grasp the handles with an overhand grip, arms extended.\", \"Pull the handles towards your sides, squeezing your shoulder blades together.\", \"Keep your elbows close to your body and your torso stable throughout the movement.\", \"Pause briefly at the peak contraction, then slowly release back to the starting position.\", \"Repeat for the desired number of repetitions.\"]'),(63,'Pull Ups','An exercise targeting the back, biceps, and core muscles, performed by pulling oneself up to a bar and lowering back down.','Strength',NULL,'Weighted Bodyweight','Back','media/exercise_gifs/0651.gif',NULL,'media/exercise_images/tmp72qdkyu8.jpg','[\"Grab the pull-up bar with an overhand grip, hands slightly wider than shoulder-width apart.\", \"Hang from the bar with your arms fully extended and your feet off the ground.\", \"Engage your core and pull yourself up towards the bar by bending your elbows, squeezing your shoulder blades together.\", \"Continue pulling until your chin clears the bar, keeping your body straight.\", \"Lower yourself back down to the starting position with control, fully extending your arms.\", \"Repeat for the desired number of repetitions.\"]'),(64,'Overhead Tricep Extension (Cable)','A tricep exercise targeting the long head of the triceps, performed by extending the arms overhead.','Strength',NULL,'Machine','Triceps','media/exercise_gifs/0194.gif',NULL,'media/exercise_images/tmpqtoiny8w.jpg','[\"Attach a rope to a cable machine at a high position.\", \"Stand facing away from the machine with your feet shoulder-width apart.\", \"Grasp the rope with both hands, palms facing each other, and bring your hands above your head.\", \"Keep your upper arms close to your head and your elbows pointing forward.\", \"Slowly lower the rope behind your head by bending your elbows.\", \"Pause for a moment, then extend your arms back up to the starting position.\", \"Repeat for the desired number of repetitions.\"]');
/*!40000 ALTER TABLE `mobi_app_exercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mobi_app_sessionexercise`
--

DROP TABLE IF EXISTS `mobi_app_sessionexercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mobi_app_sessionexercise` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `exercise_id` bigint NOT NULL,
  `workout_session_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mobi_app_sessionexer_workout_session_id_d46a772e_fk_mobi_app_` (`workout_session_id`),
  KEY `mobi_app_sessionexer_exercise_id_efb03d68_fk_mobi_app_` (`exercise_id`),
  CONSTRAINT `mobi_app_sessionexer_exercise_id_efb03d68_fk_mobi_app_` FOREIGN KEY (`exercise_id`) REFERENCES `mobi_app_exercise` (`id`),
  CONSTRAINT `mobi_app_sessionexer_workout_session_id_d46a772e_fk_mobi_app_` FOREIGN KEY (`workout_session_id`) REFERENCES `mobi_app_workoutsession` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobi_app_sessionexercise`
--

LOCK TABLES `mobi_app_sessionexercise` WRITE;
/*!40000 ALTER TABLE `mobi_app_sessionexercise` DISABLE KEYS */;
/*!40000 ALTER TABLE `mobi_app_sessionexercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mobi_app_set`
--

DROP TABLE IF EXISTS `mobi_app_set`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mobi_app_set` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `reps` int DEFAULT NULL,
  `weight` decimal(10,2) DEFAULT NULL,
  `duration` int DEFAULT NULL,
  `notes` longtext,
  `session_exercise_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mobi_app_set_session_exercise_id_2fa4b4dd_fk_mobi_app_` (`session_exercise_id`),
  CONSTRAINT `mobi_app_set_session_exercise_id_2fa4b4dd_fk_mobi_app_` FOREIGN KEY (`session_exercise_id`) REFERENCES `mobi_app_sessionexercise` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobi_app_set`
--

LOCK TABLES `mobi_app_set` WRITE;
/*!40000 ALTER TABLE `mobi_app_set` DISABLE KEYS */;
/*!40000 ALTER TABLE `mobi_app_set` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mobi_app_templateexercise`
--

DROP TABLE IF EXISTS `mobi_app_templateexercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mobi_app_templateexercise` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `exercise_id` bigint NOT NULL,
  `workout_template_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mobi_app_templateexe_exercise_id_3267ead5_fk_mobi_app_` (`exercise_id`),
  KEY `mobi_app_templateexe_workout_template_id_d85af760_fk_mobi_app_` (`workout_template_id`),
  CONSTRAINT `mobi_app_templateexe_exercise_id_3267ead5_fk_mobi_app_` FOREIGN KEY (`exercise_id`) REFERENCES `mobi_app_exercise` (`id`),
  CONSTRAINT `mobi_app_templateexe_workout_template_id_d85af760_fk_mobi_app_` FOREIGN KEY (`workout_template_id`) REFERENCES `mobi_app_workouttemplate` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobi_app_templateexercise`
--

LOCK TABLES `mobi_app_templateexercise` WRITE;
/*!40000 ALTER TABLE `mobi_app_templateexercise` DISABLE KEYS */;
/*!40000 ALTER TABLE `mobi_app_templateexercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mobi_app_userprogress`
--

DROP TABLE IF EXISTS `mobi_app_userprogress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mobi_app_userprogress` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` datetime(6) NOT NULL,
  `metric` varchar(255) NOT NULL,
  `value` decimal(10,2) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mobi_app_userprogress_user_id_aa13ee15_fk_auth_user_id` (`user_id`),
  CONSTRAINT `mobi_app_userprogress_user_id_aa13ee15_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobi_app_userprogress`
--

LOCK TABLES `mobi_app_userprogress` WRITE;
/*!40000 ALTER TABLE `mobi_app_userprogress` DISABLE KEYS */;
/*!40000 ALTER TABLE `mobi_app_userprogress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mobi_app_workoutsession`
--

DROP TABLE IF EXISTS `mobi_app_workoutsession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mobi_app_workoutsession` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) DEFAULT NULL,
  `notes` longtext,
  `user_id` int NOT NULL,
  `workout_template_id` bigint DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `mobi_app_workoutsession_user_id_4fd4259f_fk_auth_user_id` (`user_id`),
  KEY `mobi_app_workoutsess_workout_template_id_f0de6848_fk_mobi_app_` (`workout_template_id`),
  CONSTRAINT `mobi_app_workoutsess_workout_template_id_f0de6848_fk_mobi_app_` FOREIGN KEY (`workout_template_id`) REFERENCES `mobi_app_workouttemplate` (`id`),
  CONSTRAINT `mobi_app_workoutsession_user_id_4fd4259f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobi_app_workoutsession`
--

LOCK TABLES `mobi_app_workoutsession` WRITE;
/*!40000 ALTER TABLE `mobi_app_workoutsession` DISABLE KEYS */;
INSERT INTO `mobi_app_workoutsession` VALUES (1,'2023-12-27 11:31:36.811475',NULL,NULL,1,1,NULL),(5,'2024-01-04 05:13:25.127312',NULL,NULL,1,2,NULL);
/*!40000 ALTER TABLE `mobi_app_workoutsession` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mobi_app_workouttemplate`
--

DROP TABLE IF EXISTS `mobi_app_workouttemplate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mobi_app_workouttemplate` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext,
  `created_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mobi_app_workouttemplate_user_id_00384a1a_fk_auth_user_id` (`user_id`),
  CONSTRAINT `mobi_app_workouttemplate_user_id_00384a1a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobi_app_workouttemplate`
--

LOCK TABLES `mobi_app_workouttemplate` WRITE;
/*!40000 ALTER TABLE `mobi_app_workouttemplate` DISABLE KEYS */;
INSERT INTO `mobi_app_workouttemplate` VALUES (1,'Chest and Back','Option 1 out of 2 for training Chest and Back','2023-12-23 04:52:05.719198',1),(2,'Arms and Shoulders','Option 1 out of 2 for training Arms and Shoulders','2023-12-23 04:53:51.742728',1);
/*!40000 ALTER TABLE `mobi_app_workouttemplate` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-18 15:46:05
