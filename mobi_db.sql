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
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add set',7,'add_set'),(26,'Can change set',7,'change_set'),(27,'Can delete set',7,'delete_set'),(28,'Can view set',7,'view_set'),(29,'Can add user',8,'add_user'),(30,'Can change user',8,'change_user'),(31,'Can delete user',8,'delete_user'),(32,'Can view user',8,'view_user'),(33,'Can add workout session',9,'add_workoutsession'),(34,'Can change workout session',9,'change_workoutsession'),(35,'Can delete workout session',9,'delete_workoutsession'),(36,'Can view workout session',9,'view_workoutsession'),(37,'Can add workout template',10,'add_workouttemplate'),(38,'Can change workout template',10,'change_workouttemplate'),(39,'Can delete workout template',10,'delete_workouttemplate'),(40,'Can view workout template',10,'view_workouttemplate'),(41,'Can add template exercise',11,'add_templateexercise'),(42,'Can change template exercise',11,'change_templateexercise'),(43,'Can delete template exercise',11,'delete_templateexercise'),(44,'Can view template exercise',11,'view_templateexercise'),(45,'Can add exercise',12,'add_exercise'),(46,'Can change exercise',12,'change_exercise'),(47,'Can delete exercise',12,'delete_exercise'),(48,'Can view exercise',12,'view_exercise'),(49,'Can add session exercise',13,'add_sessionexercise'),(50,'Can change session exercise',13,'change_sessionexercise'),(51,'Can delete session exercise',13,'delete_sessionexercise'),(52,'Can view session exercise',13,'view_sessionexercise'),(53,'Can add user progress',14,'add_userprogress'),(54,'Can change user progress',14,'change_userprogress'),(55,'Can delete user progress',14,'delete_userprogress'),(56,'Can view user progress',14,'view_userprogress'),(57,'Can add Token',15,'add_token'),(58,'Can change Token',15,'change_token'),(59,'Can delete Token',15,'delete_token'),(60,'Can view Token',15,'view_token'),(61,'Can add token',16,'add_tokenproxy'),(62,'Can change token',16,'change_tokenproxy'),(63,'Can delete token',16,'delete_tokenproxy'),(64,'Can view token',16,'view_tokenproxy');
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$0WLcNad4k0mFpNqFLS7Atf$IsOo/gLthZH/uWltwfGf6ds5pbup+MAJHMGC9f8zqeA=','2023-12-21 07:18:53.403255',1,'harshbhatia','','','',1,1,'2023-12-21 07:18:13.692145'),(5,'pbkdf2_sha256$600000$Xi7sgO5uAFNG3y2ZDgfEIB$3a+ehr0TvDVS5W+3bRkSdp9gS+Y7vGFOhpYRQiqRtiE=',NULL,0,'manraj','','','test@gmail.com',0,1,'2023-12-22 04:13:14.000000'),(6,'pbkdf2_sha256$600000$fe0SMBVguNG8DJsVyAKTyy$wuHFHp1DD6/71/LxYA2PI/KkD9SfnrgyHQD7q7wnaD4=',NULL,0,'shaleen','','','test@gmail.com',0,1,'2023-12-22 04:13:14.000000'),(7,'pbkdf2_sha256$600000$UFKPjosghq4FRAjKpB7jPP$u1+2QFUgCOMVA4cSD01kCfJwarXmQkEdWHiH46R/Bdo=',NULL,0,'aryan','','','test@gmail.com',0,1,'2023-12-22 04:13:14.000000'),(8,'pbkdf2_sha256$600000$IbiCSdh1pFDTWq5NS2o1hS$oWWAOysCUAKc0MX5LuFjGxfe6nw0Q+pz8+WReIw+f0k=',NULL,0,'sachveer','','','test@gmail.com',0,1,'2023-12-22 04:13:14.000000'),(9,'pbkdf2_sha256$600000$2ihsBhT1j2FAYz3o4qUNeG$b+WgBTSUiC19oS+UG8ozRgdMKUCjSbE7GSIHh0I/NuM=',NULL,0,'sukhman','','','test@gmail.com',0,1,'2023-12-22 04:13:14.000000'),(10,'pbkdf2_sha256$600000$2HHzQHWuhYxiQwyB9NJp9n$vCA9ZquQAmDtyFZtVtxU612gk09JZqq/NqD/BePTjkM=',NULL,0,'rayman','','','test@gmail.com',0,1,'2023-12-22 04:13:14.000000'),(11,'pbkdf2_sha256$600000$TlOKsMnh67QK954llmLlhV$kAnUhxQ9KydVbDywlvVXY3FbeRMaQsAEprTTIgZ1rqM=',NULL,0,'harry','','','test@gmail.com',0,1,'2023-12-22 04:13:14.000000');
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
INSERT INTO `authtoken_token` VALUES ('8a1b26df7d9d2fe8a633aa1c2e30e9a125c7e0bc','2023-12-23 04:19:19.567681',11),('909453871b49e090369ab3977a28e8890adc9313','2023-12-23 04:19:19.566688',9),('928983875cfb55ad584672b1102a8bd40e6cf2c1','2023-12-23 04:19:19.564096',5),('c4510b5bd4299b712d4bd4d45120804c5ef01edb','2023-12-23 04:19:19.567147',10),('c52bf1c458c884549f70b6d6990b125a7fe57d02','2023-12-23 04:19:19.564884',6),('e5f8878719dc0aeaee6f681dfdc3d6be0a90f9af','2023-12-23 04:19:19.566230',8),('f446066dcc7601ad3abe20f3f5be42a5f0de42c1','2023-12-23 04:19:19.565723',7),('fbec88a0d5fe88d02c977eb71d0bd0c5f7244999','2023-12-23 04:19:19.563262',1);
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-12-22 04:12:10.021120','2','manraj',1,'[{\"added\": {}}]',4,1),(2,'2023-12-22 04:12:59.673176','2','manraj',3,'',4,1),(3,'2023-12-22 04:13:43.964416','1','User object (1)',1,'[{\"added\": {}}]',8,1),(4,'2023-12-22 04:14:38.658625','2','User object (2)',1,'[{\"added\": {}}]',8,1),(5,'2023-12-22 04:14:53.407780','3','User object (3)',1,'[{\"added\": {}}]',8,1),(6,'2023-12-22 04:15:02.914941','4','User object (4)',1,'[{\"added\": {}}]',8,1),(7,'2023-12-22 04:15:17.571921','5','User object (5)',1,'[{\"added\": {}}]',8,1),(8,'2023-12-22 04:15:26.932255','6','User object (6)',1,'[{\"added\": {}}]',8,1),(9,'2023-12-22 04:15:34.685545','7','User object (7)',1,'[{\"added\": {}}]',8,1),(10,'2023-12-22 04:24:30.346980','8','User object (8)',1,'[{\"added\": {}}]',8,1),(11,'2023-12-22 06:17:53.273576','4','oppenheimer',3,'',4,1),(12,'2023-12-22 06:17:53.276108','3','yash',3,'',4,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(15,'authtoken','token'),(16,'authtoken','tokenproxy'),(5,'contenttypes','contenttype'),(12,'mobi_app','exercise'),(13,'mobi_app','sessionexercise'),(7,'mobi_app','set'),(11,'mobi_app','templateexercise'),(8,'mobi_app','user'),(14,'mobi_app','userprogress'),(9,'mobi_app','workoutsession'),(10,'mobi_app','workouttemplate'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-12-21 05:56:44.421104'),(2,'auth','0001_initial','2023-12-21 05:56:44.477580'),(3,'admin','0001_initial','2023-12-21 05:56:44.495230'),(4,'admin','0002_logentry_remove_auto_add','2023-12-21 05:56:44.498292'),(5,'admin','0003_logentry_add_action_flag_choices','2023-12-21 05:56:44.500933'),(6,'contenttypes','0002_remove_content_type_name','2023-12-21 05:56:44.513899'),(7,'auth','0002_alter_permission_name_max_length','2023-12-21 05:56:44.523202'),(8,'auth','0003_alter_user_email_max_length','2023-12-21 05:56:44.529682'),(9,'auth','0004_alter_user_username_opts','2023-12-21 05:56:44.532229'),(10,'auth','0005_alter_user_last_login_null','2023-12-21 05:56:44.540689'),(11,'auth','0006_require_contenttypes_0002','2023-12-21 05:56:44.541283'),(12,'auth','0007_alter_validators_add_error_messages','2023-12-21 05:56:44.544095'),(13,'auth','0008_alter_user_username_max_length','2023-12-21 05:56:44.554106'),(14,'auth','0009_alter_user_last_name_max_length','2023-12-21 05:56:44.563386'),(15,'auth','0010_alter_group_name_max_length','2023-12-21 05:56:44.569081'),(16,'auth','0011_update_proxy_permissions','2023-12-21 05:56:44.572999'),(17,'auth','0012_alter_user_first_name_max_length','2023-12-21 05:56:44.583965'),(18,'sessions','0001_initial','2023-12-21 05:56:44.588951'),(19,'mobi_app','0001_initial','2023-12-21 07:24:33.998856'),(20,'mobi_app','0002_rename_date_of_joining_user_date_joined','2023-12-22 05:48:07.811907'),(21,'authtoken','0001_initial','2023-12-23 04:10:39.842262'),(22,'authtoken','0002_auto_20160226_1747','2023-12-23 04:10:39.852102'),(23,'authtoken','0003_tokenproxy','2023-12-23 04:10:39.853106'),(24,'mobi_app','0003_alter_sessionexercise_exercise_and_more','2023-12-23 04:16:58.520465'),(25,'mobi_app','0004_alter_workouttemplate_created_at','2023-12-23 04:51:49.794857');
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
INSERT INTO `django_session` VALUES ('zwr92q5mnuqxsusn4yhl0d38ua09ftfm','.eJxVjDsOwyAQBe9CHSGMMZ-U6X0GtOxCcBKBZOwqyt2DJRdJ-2bmvZmHfct-b3H1C7ErG9jldwuAz1gOQA8o98qxlm1dAj8UftLG50rxdTvdv4MMLfdaCS30IBJKKYUZLagwGtQiAmlEmkA6tMlO0rjUvdFaBb2RDkJARY59vr4bNzc:1rGDKX:HtXh6ofODxM2sQWGIkb3uFOvp04z1nQJLmpeXJLKgPg','2024-01-04 07:18:53.404199');
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobi_app_exercise`
--

LOCK TABLES `mobi_app_exercise` WRITE;
/*!40000 ALTER TABLE `mobi_app_exercise` DISABLE KEYS */;
INSERT INTO `mobi_app_exercise` VALUES (1,'Incline Smith Machine Bench Press','A Smith machine incline bench press is a weightlifting exercise that involves pressing a barbell fixed on a guided vertical track at an incline to target the upper chest muscles.','Chest'),(2,'Flat Chest Press (Hammer Strength)','The Hammer Strength flat chest press machine is a piece of gym equipment designed for horizontal chest pressing exercises, helping build strength and muscle in the pectoral muscles.','Chest'),(3,'Low to High Rows','Low-to-high rows target upper back and shoulders by pulling from low to high.','Back'),(4,'Dips','Exercise for triceps, chest, and shoulders, performed by lowering and raising the body','Chest'),(5,'Pull Ups','Exercise for upper body strength, performed by pulling up from a hanging position.','Back'),(6,'Incline Chest Flies','Isolation exercise targeting chest muscles, involving a controlled fly motion on an incline bench.','Chest'),(7,'Close Grip Rows','Exercise targeting the upper back and biceps using a narrow hand grip.','Back'),(8,'Shoulder Press (Hammer Strength)','Machine-based exercise for shoulder strength and development using a guided press motion.','Shoulders'),(9,'Incline Curls','Bicep isolation exercise performed on an inclined bench, targeting the upper part of the arm.','Biceps'),(10,'Tricep Pushdowns','Isolation exercise for triceps, involving pushing down a cable attachment.','Triceps'),(11,'Seated Lateral Raises','Shoulder isolation exercise, performed seated, targeting the lateral deltoid muscles for shoulder development.','Shoulders'),(12,'Preacher Curls','Bicep isolation exercise performed on a preacher bench, emphasizing the bicep\'s peak.','Biceps'),(13,'Overhead Tricep Extensions','Isolation exercise for triceps, performed by extending the arms overhead with a weight.','Triceps'),(14,'Hammer Curls','Bicep exercise emphasizing the brachialis muscle, performed with a neutral grip for arm development.','Biceps'),(15,'Lateral Raises (Arsenal Machine)','Isolation exercise for shoulder development, using the Arsenal Machine for lateral deltoid targeting.','Shoulders'),(16,'Rear Delt Fly Machine','Exercise targeting the rear deltoid muscles using a specific machine for posterior shoulder development.','Shoulders'),(17,'Reverse Wrist Curls','Forearm exercise involving wrist flexion in the opposite direction, strengthening the extensor muscles.','Forearms'),(18,'Behind The Back Barbell Wrist Curls','Forearm exercise focusing on wrist flexion using a barbell behind the back.','Forearms');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
  `reps` int NOT NULL,
  `weight` decimal(10,2) NOT NULL,
  `duration` int DEFAULT NULL,
  `notes` longtext NOT NULL,
  `session_exercise_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mobi_app_set_session_exercise_id_2fa4b4dd_fk_mobi_app_` (`session_exercise_id`),
  CONSTRAINT `mobi_app_set_session_exercise_id_2fa4b4dd_fk_mobi_app_` FOREIGN KEY (`session_exercise_id`) REFERENCES `mobi_app_sessionexercise` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
INSERT INTO `mobi_app_templateexercise` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,5,1),(6,6,1),(7,7,1),(8,8,2),(9,9,2),(10,10,2),(11,11,2),(12,12,2),(13,13,2),(14,14,2),(15,15,2),(16,16,2),(17,17,2),(18,18,2);
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
  `end_time` datetime(6) NOT NULL,
  `notes` longtext NOT NULL,
  `user_id` int NOT NULL,
  `workout_template_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mobi_app_workoutsess_workout_template_id_f0de6848_fk_mobi_app_` (`workout_template_id`),
  KEY `mobi_app_workoutsession_user_id_4fd4259f_fk_auth_user_id` (`user_id`),
  CONSTRAINT `mobi_app_workoutsess_workout_template_id_f0de6848_fk_mobi_app_` FOREIGN KEY (`workout_template_id`) REFERENCES `mobi_app_workouttemplate` (`id`),
  CONSTRAINT `mobi_app_workoutsession_user_id_4fd4259f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobi_app_workoutsession`
--

LOCK TABLES `mobi_app_workoutsession` WRITE;
/*!40000 ALTER TABLE `mobi_app_workoutsession` DISABLE KEYS */;
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
  `description` longtext NOT NULL,
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

-- Dump completed on 2023-12-27 16:39:05
