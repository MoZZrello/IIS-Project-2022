-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 21, 2022 at 10:13 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `iis_mysql`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add user_roles', 7, 'add_user_roles'),
(26, 'Can change user_roles', 7, 'change_user_roles'),
(27, 'Can delete user_roles', 7, 'delete_user_roles'),
(28, 'Can view user_roles', 7, 'view_user_roles'),
(29, 'Can add user', 8, 'add_user'),
(30, 'Can change user', 8, 'change_user'),
(31, 'Can delete user', 8, 'delete_user'),
(32, 'Can view user', 8, 'view_user'),
(33, 'Can add animal', 9, 'add_animal'),
(34, 'Can change animal', 9, 'change_animal'),
(35, 'Can delete animal', 9, 'delete_animal'),
(36, 'Can view animal', 9, 'view_animal'),
(37, 'Can add outing_reservation', 10, 'add_outing_reservation'),
(38, 'Can change outing_reservation', 10, 'change_outing_reservation'),
(39, 'Can delete outing_reservation', 10, 'delete_outing_reservation'),
(40, 'Can view outing_reservation', 10, 'view_outing_reservation'),
(41, 'Can add record', 11, 'add_record'),
(42, 'Can change record', 11, 'change_record'),
(43, 'Can delete record', 11, 'delete_record'),
(44, 'Can view record', 11, 'view_record'),
(45, 'Can add requests', 12, 'add_requests'),
(46, 'Can change requests', 12, 'change_requests'),
(47, 'Can delete requests', 12, 'delete_requests'),
(48, 'Can view requests', 12, 'view_requests');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$390000$p57r7ZJWLSMsVf3TiPnIWp$hB3dif471pJAH0j3w7S9bLmDjOVQ173TWcXFmzginz0=', '2022-10-12 21:35:48.208717', 1, 'admin', '', '', 'test@test.com', 1, 1, '2022-10-12 20:38:31.738614');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(9, 'IISapp', 'animal'),
(10, 'IISapp', 'outing_reservation'),
(11, 'IISapp', 'record'),
(12, 'IISapp', 'requests'),
(8, 'IISapp', 'user'),
(7, 'IISapp', 'user_roles'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(2, 'contenttypes', '0001_initial', '2022-10-11 08:02:22.497947'),
(3, 'auth', '0001_initial', '2022-10-11 08:02:23.003150'),
(4, 'admin', '0001_initial', '2022-10-11 08:02:23.246327'),
(5, 'admin', '0002_logentry_remove_auto_add', '2022-10-11 08:02:23.252328'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2022-10-11 08:02:23.257326'),
(7, 'contenttypes', '0002_remove_content_type_name', '2022-10-11 08:02:23.308364'),
(8, 'auth', '0002_alter_permission_name_max_length', '2022-10-11 08:02:23.954910'),
(9, 'auth', '0003_alter_user_email_max_length', '2022-10-11 08:02:23.971615'),
(10, 'auth', '0004_alter_user_username_opts', '2022-10-11 08:02:23.976667'),
(11, 'auth', '0005_alter_user_last_login_null', '2022-10-11 08:02:24.009162'),
(12, 'auth', '0006_require_contenttypes_0002', '2022-10-11 08:02:24.012355'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2022-10-11 08:02:24.017250'),
(14, 'auth', '0008_alter_user_username_max_length', '2022-10-11 08:02:24.029285'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2022-10-11 08:02:24.040285'),
(16, 'auth', '0010_alter_group_name_max_length', '2022-10-11 08:02:24.052019'),
(17, 'auth', '0011_update_proxy_permissions', '2022-10-11 08:02:24.059693'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2022-10-11 08:02:24.071748'),
(19, 'sessions', '0001_initial', '2022-10-11 08:02:24.107749'),
(21, 'IISapp', '0001_initial', '2022-10-12 18:14:12.985941'),
(22, 'IISapp', '0002_remove_record_record_end_remove_record_record_start_and_more', '2022-10-12 19:07:19.115678'),
(23, 'IISapp', '0003_rename_phone_numb_user_phone_number_user_last_login', '2022-10-12 21:12:53.140595'),
(24, 'IISapp', '0004_alter_user_options_alter_user_managers_and_more', '2022-10-18 12:22:00.047520'),
(25, 'IISapp', '0005_outing_reservation_outing_assigned', '2022-10-18 14:18:15.050885'),
(26, 'IISapp', '0006_user_profile_picture', '2022-10-20 10:27:07.467151'),
(27, 'IISapp', '0007_alter_animal_image_alter_user_profile_picture', '2022-10-20 10:29:37.056086'),
(28, 'IISapp', '0008_alter_animal_image_alter_user_profile_picture', '2022-10-20 10:30:29.469343'),
(29, 'IISapp', '0009_alter_user_profile_picture', '2022-10-20 14:43:37.933142'),
(30, 'IISapp', '0010_alter_user_profile_picture', '2022-10-20 14:55:28.985841'),
(31, 'IISapp', '0011_alter_user_profile_picture', '2022-10-20 15:31:49.681807'),
(32, 'IISapp', '0012_alter_outing_reservation_user_name', '2022-10-21 15:03:22.098352'),
(33, 'IISapp', '0013_alter_outing_reservation_user_name', '2022-10-21 15:04:41.649187'),
(34, 'IISapp', '0014_alter_animal_image', '2022-10-21 19:27:27.336196'),
(35, 'IISapp', '0015_alter_animal_image', '2022-10-21 19:59:46.495702');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('yvwcqeitndet80h7q8rmspidrv5ea1j7', '.eJxVjDsOwjAQRO_iGlnxR96Ykp4zWGvvgAMolvKpEHcnkVJAOfPezFslXpea1hlTGkSdFanTb5e5PDHuQB483psubVymIetd0Qed9bUJXpfD_TuoPNdtbanrUOTWw_ngGEDuxdjQW-Jog7EdTBGbJcKBgyFPbCJtARBPRX2-8ig4aA:1olxWk:-o1BlpBlIpvSYR6ZSieYUcXOwCFb6G2cb4P_4D0u1FQ', '2022-11-04 19:17:54.109602');

-- --------------------------------------------------------

--
-- Table structure for table `iisapp_animal`
--

CREATE TABLE `iisapp_animal` (
  `id` bigint(20) NOT NULL,
  `animal_name` varchar(255) NOT NULL,
  `species` varchar(255) NOT NULL,
  `breed` varchar(255) NOT NULL,
  `age` smallint(6) NOT NULL,
  `animal_description` longtext NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `capture_date` date NOT NULL,
  `outing_suitable` tinyint(1) NOT NULL,
  `animal_verification` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `iisapp_animal`
--

INSERT INTO `iisapp_animal` (`id`, `animal_name`, `species`, `breed`, `age`, `animal_description`, `image`, `capture_date`, `outing_suitable`, `animal_verification`) VALUES
(1, 'Marco', 'Pes', 'Labrador', 3, 'Velice společenský a přátelský (někdy kouše, ale on to tak nemyslí). Vhodný do mafiánských rodin a na mučení lidí.', 'static/img/chihuahua.jpg', '2021-10-06', 1, 1),
(2, 'Al Pacachino', 'Alpaca', '', 4, 'Vhodná na vyrobení svetru, možná i zimní čepice.', 'static/img/alpaca.jpg', '2021-11-26', 1, 0),
(3, 'Macho', 'Pes', 'Bulldog', 4, 'Miluje se oblizovat.', '', '2022-11-08', 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `iisapp_outing_reservation`
--

CREATE TABLE `iisapp_outing_reservation` (
  `id` bigint(20) NOT NULL,
  `outing_start` datetime(6) NOT NULL,
  `outing_end` datetime(6) NOT NULL,
  `outing_verification` tinyint(1) NOT NULL,
  `animal_id` bigint(20) NOT NULL,
  `user_name_id` bigint(20) DEFAULT NULL,
  `outing_assigned` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `iisapp_outing_reservation`
--

INSERT INTO `iisapp_outing_reservation` (`id`, `outing_start`, `outing_end`, `outing_verification`, `animal_id`, `user_name_id`, `outing_assigned`) VALUES
(3, '2022-11-06 08:00:00.000000', '2022-11-06 08:30:00.000000', 1, 1, 6, 1),
(4, '2022-11-06 08:00:00.000000', '2022-11-06 08:30:00.000000', 0, 1, 3, 1),
(6, '2022-12-06 08:00:00.000000', '2022-12-06 08:30:00.000000', 0, 2, 6, 1),
(7, '2021-11-06 08:00:00.000000', '2021-11-06 08:30:00.000000', 1, 1, 6, 1),
(8, '2023-01-06 08:00:00.000000', '2023-01-06 08:30:00.000000', 0, 1, 6, 1),
(9, '2022-11-06 08:00:00.000000', '2022-11-06 08:30:00.000000', 0, 1, 6, 0);

-- --------------------------------------------------------

--
-- Table structure for table `iisapp_record`
--

CREATE TABLE `iisapp_record` (
  `id` bigint(20) NOT NULL,
  `record_name` varchar(255) NOT NULL,
  `record_type` varchar(255) NOT NULL,
  `record_description` longtext NOT NULL,
  `animal_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `iisapp_record`
--

INSERT INTO `iisapp_record` (`id`, `record_name`, `record_type`, `record_description`, `animal_id`) VALUES
(1, 'Nájdení Marca', 'Nájdení', 'V pondělí sme našli marca v drogovém doupěti. Po příjezde na místo sme okamžite odhadli, že byl napíchaný kokainem. Odvykačka však proběhla hladce.', 1);

-- --------------------------------------------------------

--
-- Table structure for table `iisapp_requests`
--

CREATE TABLE `iisapp_requests` (
  `id` bigint(20) NOT NULL,
  `datetime_start` datetime(6) NOT NULL,
  `datetime_end` datetime(6) NOT NULL,
  `veterinary_req` tinyint(1) NOT NULL,
  `request_name` varchar(255) NOT NULL,
  `request_description` longtext NOT NULL,
  `request_verification` tinyint(1) NOT NULL,
  `animal_id` bigint(20) NOT NULL,
  `contractor_id` bigint(20) NOT NULL,
  `solver_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `iisapp_requests`
--

INSERT INTO `iisapp_requests` (`id`, `datetime_start`, `datetime_end`, `veterinary_req`, `request_name`, `request_description`, `request_verification`, `animal_id`, `contractor_id`, `solver_id`) VALUES
(1, '2022-11-30 12:00:00.000000', '2022-11-30 12:30:00.000000', 1, 'Odčervení Marca', 'Marco si už týden škrábe zadek  o beton. Potřebuje odčervit. Vopřed ďekuji.', 1, 1, 2, 3);

-- --------------------------------------------------------

--
-- Table structure for table `iisapp_user`
--

CREATE TABLE `iisapp_user` (
  `id` bigint(20) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `birthdate` date NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `user_verification` tinyint(1) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role_id` bigint(20) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `profile_picture` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `iisapp_user`
--

INSERT INTO `iisapp_user` (`id`, `full_name`, `birthdate`, `phone_number`, `mail`, `user_verification`, `user_name`, `password`, `role_id`, `last_login`, `date_joined`, `email`, `first_name`, `is_active`, `is_staff`, `is_superuser`, `last_name`, `profile_picture`) VALUES
(2, 'Tester Keeper', '1995-03-25', '751175563', 'fakeemail@test.com', 1, 'testerkeeper', 'test123', 2, NULL, '2022-10-18 12:21:59.448135', '', '', 1, 0, 0, '', 'profile_pic_default.jpg'),
(3, 'Tester Vet', '1998-05-01', '456432874', 'imadeupthisemail@test.com', 1, 'testervet', 'test123', 3, NULL, '2022-10-18 12:21:59.448135', '', '', 1, 0, 0, '', 'profile_pic_default.jpg'),
(4, 'Tester Volunteer', '2001-10-10', '777777777', 'ilovepokemon@test.com', 1, 'testervolunteer', 'test123', 4, NULL, '2022-10-18 12:21:59.448135', '', '', 1, 0, 0, '', 'profile_pic_default.jpg'),
(6, 'Tester Drak', '2006-01-26', '+12125552369', 'test@gmail.com', 1, 'regtest1', 'pbkdf2_sha256$390000$ecKMSEJWWxMwyew7whkEJT$3470dXi+YxtthpnPD32HjsHr01FwusFJrOINbvzuVlA=', 4, '2022-10-21 15:06:12.668415', '2022-10-18 12:27:36.627011', 'test@gmail.com', '', 1, 0, 0, '', ''),
(7, 'Jozef Mrkva', '2006-03-09', '+12125552368', 'test@test.com', 1, 'mrkvanaprovazku', 'pbkdf2_sha256$390000$NElZdpbh2AOmQebR8BoK43$MH5EL64Ebp4BFuZPrkWc202b/0r/PD9qCrkSWsBZaCo=', 2, '2022-10-21 19:17:54.106606', '2022-10-19 13:35:31.338733', '', '', 1, 0, 0, '', ''),
(8, 'Admin Tester', '2000-11-02', '+421907777888', 'test@test.com', 1, 'admin', 'pbkdf2_sha256$390000$Sfx8EUo4d45eSiNwU73jJS$7LCninn1Jku+eiFwDjQBMTlQFnuOdV7mVx1dpojt0kM=', 1, '2022-10-20 09:49:27.689744', '2022-10-20 09:49:22.160002', '', '', 1, 0, 0, '', 'profile_pic_default.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `iisapp_user_groups`
--

CREATE TABLE `iisapp_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `iisapp_user_roles`
--

CREATE TABLE `iisapp_user_roles` (
  `id` bigint(20) NOT NULL,
  `role` smallint(5) UNSIGNED NOT NULL CHECK (`role` >= 0),
  `user_manage` tinyint(1) NOT NULL,
  `animal_manage` tinyint(1) NOT NULL,
  `schedule_manage` tinyint(1) NOT NULL,
  `verify_volunteers` tinyint(1) NOT NULL,
  `verify_reservations` tinyint(1) NOT NULL,
  `make_requests` tinyint(1) NOT NULL,
  `make_veterinary_requests` tinyint(1) NOT NULL,
  `handle_requests` tinyint(1) NOT NULL,
  `handle_veterinary_requests` tinyint(1) NOT NULL,
  `edit_reports` tinyint(1) NOT NULL,
  `edit_veterinary_reports` tinyint(1) NOT NULL,
  `make_reservations` tinyint(1) NOT NULL,
  `outing_history_view` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `iisapp_user_roles`
--

INSERT INTO `iisapp_user_roles` (`id`, `role`, `user_manage`, `animal_manage`, `schedule_manage`, `verify_volunteers`, `verify_reservations`, `make_requests`, `make_veterinary_requests`, `handle_requests`, `handle_veterinary_requests`, `edit_reports`, `edit_veterinary_reports`, `make_reservations`, `outing_history_view`) VALUES
(1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(2, 2, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),
(3, 3, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0),
(4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `iisapp_user_user_permissions`
--

CREATE TABLE `iisapp_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `iisapp_animal`
--
ALTER TABLE `iisapp_animal`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `iisapp_outing_reservation`
--
ALTER TABLE `iisapp_outing_reservation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IISapp_outing_reservation_animal_id_8161d4b5_fk_IISapp_animal_id` (`animal_id`),
  ADD KEY `IISapp_outing_reserv_user_name_id_005460fb_fk_IISapp_us` (`user_name_id`);

--
-- Indexes for table `iisapp_record`
--
ALTER TABLE `iisapp_record`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IISapp_record_animal_id_22fe4722_fk_IISapp_animal_id` (`animal_id`);

--
-- Indexes for table `iisapp_requests`
--
ALTER TABLE `iisapp_requests`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IISapp_requests_animal_id_00ab5696_fk_IISapp_animal_id` (`animal_id`),
  ADD KEY `IISapp_requests_contractor_id_aa5765a7_fk_IISapp_user_id` (`contractor_id`),
  ADD KEY `IISapp_requests_solver_id_afa4d480_fk_IISapp_user_id` (`solver_id`);

--
-- Indexes for table `iisapp_user`
--
ALTER TABLE `iisapp_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `IISapp_user_user_name_37459ed8_uniq` (`user_name`),
  ADD KEY `IISapp_user_role_id_ef7a69d0_fk_IISapp_user_roles_id` (`role_id`);

--
-- Indexes for table `iisapp_user_groups`
--
ALTER TABLE `iisapp_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `IISapp_user_groups_user_id_group_id_0b86923c_uniq` (`user_id`,`group_id`),
  ADD KEY `IISapp_user_groups_group_id_ea87111d_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `iisapp_user_roles`
--
ALTER TABLE `iisapp_user_roles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `iisapp_user_user_permissions`
--
ALTER TABLE `iisapp_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `IISapp_user_user_permissions_user_id_permission_id_c90d5dda_uniq` (`user_id`,`permission_id`),
  ADD KEY `IISapp_user_user_per_permission_id_861b18ae_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `iisapp_animal`
--
ALTER TABLE `iisapp_animal`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `iisapp_outing_reservation`
--
ALTER TABLE `iisapp_outing_reservation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `iisapp_record`
--
ALTER TABLE `iisapp_record`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `iisapp_requests`
--
ALTER TABLE `iisapp_requests`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `iisapp_user`
--
ALTER TABLE `iisapp_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `iisapp_user_groups`
--
ALTER TABLE `iisapp_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `iisapp_user_roles`
--
ALTER TABLE `iisapp_user_roles`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `iisapp_user_user_permissions`
--
ALTER TABLE `iisapp_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `iisapp_outing_reservation`
--
ALTER TABLE `iisapp_outing_reservation`
  ADD CONSTRAINT `IISapp_outing_reserv_user_name_id_005460fb_fk_IISapp_us` FOREIGN KEY (`user_name_id`) REFERENCES `iisapp_user` (`id`),
  ADD CONSTRAINT `IISapp_outing_reservation_animal_id_8161d4b5_fk_IISapp_animal_id` FOREIGN KEY (`animal_id`) REFERENCES `iisapp_animal` (`id`);

--
-- Constraints for table `iisapp_record`
--
ALTER TABLE `iisapp_record`
  ADD CONSTRAINT `IISapp_record_animal_id_22fe4722_fk_IISapp_animal_id` FOREIGN KEY (`animal_id`) REFERENCES `iisapp_animal` (`id`);

--
-- Constraints for table `iisapp_requests`
--
ALTER TABLE `iisapp_requests`
  ADD CONSTRAINT `IISapp_requests_animal_id_00ab5696_fk_IISapp_animal_id` FOREIGN KEY (`animal_id`) REFERENCES `iisapp_animal` (`id`),
  ADD CONSTRAINT `IISapp_requests_contractor_id_aa5765a7_fk_IISapp_user_id` FOREIGN KEY (`contractor_id`) REFERENCES `iisapp_user` (`id`),
  ADD CONSTRAINT `IISapp_requests_solver_id_afa4d480_fk_IISapp_user_id` FOREIGN KEY (`solver_id`) REFERENCES `iisapp_user` (`id`);

--
-- Constraints for table `iisapp_user`
--
ALTER TABLE `iisapp_user`
  ADD CONSTRAINT `IISapp_user_role_id_ef7a69d0_fk_IISapp_user_roles_id` FOREIGN KEY (`role_id`) REFERENCES `iisapp_user_roles` (`id`);

--
-- Constraints for table `iisapp_user_groups`
--
ALTER TABLE `iisapp_user_groups`
  ADD CONSTRAINT `IISapp_user_groups_group_id_ea87111d_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `IISapp_user_groups_user_id_39ce48aa_fk_IISapp_user_id` FOREIGN KEY (`user_id`) REFERENCES `iisapp_user` (`id`);

--
-- Constraints for table `iisapp_user_user_permissions`
--
ALTER TABLE `iisapp_user_user_permissions`
  ADD CONSTRAINT `IISapp_user_user_per_permission_id_861b18ae_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `IISapp_user_user_permissions_user_id_f7d80f4b_fk_IISapp_user_id` FOREIGN KEY (`user_id`) REFERENCES `iisapp_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
