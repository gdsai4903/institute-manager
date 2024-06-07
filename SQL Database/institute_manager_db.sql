-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 22, 2023 at 05:55 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `institute_manager_db`
--
-- Dropping the database
DROP DATABASE IF EXISTS institute_manager_db;

-- Creating new database
CREATE DATABASE IF NOT EXISTS institute_manager_db
CHARSET='utf8mb4'
COLLATE='utf8mb4_unicode_ci';

-- Using new database
USE institute_manager_db;
-- --------------------------------------------------------

--
-- Table structure for table `courses_table`
--

CREATE TABLE `courses_table` (
  `Department` varchar(100) NOT NULL,
  `Course` varchar(100) NOT NULL,
  `Duration` varchar(20) NOT NULL,
  `Fee` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `courses_table`
--

INSERT INTO `courses_table` (`Department`, `Course`, `Duration`, `Fee`) VALUES
('IT', 'BCA', '4 years', 'Rs. 13000'),
('Maths', 'M.A. Maths', '3 years', 'Rs. 300000'),
('English', 'B.A English', '2 years', 'Rs. 150000');

-- --------------------------------------------------------

--
-- Table structure for table `departments_table`
--

CREATE TABLE `departments_table` (
  `Department_Name` varchar(100) NOT NULL,
  `Department_Head` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `departments_table`
--

INSERT INTO `departments_table` (`Department_Name`, `Department_Head`) VALUES
('IT', 'Sandeep Ranjan'),
('Maths', 'Gagandeep SIngh'),
('English', 'Rachna Choudhary');

-- --------------------------------------------------------

--
-- Table structure for table `students_table`
--

CREATE TABLE `students_table` (
  `RollNo` int(11) NOT NULL,
  `S_Name` varchar(35) NOT NULL,
  `F_Name` varchar(35) NOT NULL,
  `M_Name` varchar(35) NOT NULL,
  `DOB` date NOT NULL,
  `Address` text NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `S_Phone` varchar(10) NOT NULL,
  `S_email` varchar(35) NOT NULL,
  `F_Phone` varchar(10) NOT NULL,
  `F_email` varchar(35) NOT NULL,
  `M_Phone` varchar(10) NOT NULL,
  `M_email` varchar(35) NOT NULL,
  `Department` varchar(35) NOT NULL,
  `Course` varchar(35) NOT NULL,
  `S_img` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students_table`
--

INSERT INTO `students_table` (`RollNo`, `S_Name`, `F_Name`, `M_Name`, `DOB`, `Address`, `Gender`, `S_Phone`, `S_email`, `F_Phone`, `F_email`, `M_Phone`, `M_email`, `Department`, `Course`, `S_img`) VALUES
(101, 'Gagandeep  Singh', 'Sukhwinder  Singh', 'Sukhwinder  Kaur', '2003-09-04', '16, New Raja Garden\n', 'male', '981991903', 'gdsai4903@gmail.com', '9501011903', 'artsukhvinder@gmail.com', '9501011903', 'sukh11977kaur@gmail.com', 'Maths', 'M.A. Maths', '1677076335DSC09665.jpg'),
(102, 'Bavleen  Kaur', 'Sukhwinder  Singh', 'Sukhwinder  Kaur', '2001-09-24', '16 New Raja garden\n', 'female', '3435353535', 'abc@gmail.com', '8989898989', 'abc@gmail.com', '2323232332', 'xyz@gmail.com', 'IT', 'BCA', '1677078903women-linkedin-headshot-los-angeles.jpg'),
(103, 'Harmeet  Singh', 'Pritpal  Singh', 'Asha  Rani', '1996-12-25', '335 Bank Enclave\n', 'male', '339483938', 'harmet@yahoo.com', '857485894', 'pritpal@gmail.com', '758593492', 'asha@gmail.com', 'IT', 'BCA', '1677079064JONATHAN_5022P_ppFIN.jpg'),
(104, 'Amandeep  Singh', 'Pritpal  Singh', 'Asha  Rani', '1997-09-18', '335, Bank Enclave\n', 'male', '8427128427', 'aman@icloud.com', '9815996158', 'pritpal@gmail.com', '6545938594', 'asha@gmail.com', 'English', 'B.A English', '1677079205Oscar-1246.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `usertable`
--

CREATE TABLE `usertable` (
  `Username` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `UserType` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students_table`
--
ALTER TABLE `students_table`
  ADD PRIMARY KEY (`RollNo`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `students_table`
--
ALTER TABLE `students_table`
  MODIFY `RollNo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483648;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
