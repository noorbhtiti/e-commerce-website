-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 14, 2020 at 04:03 PM
-- Server version: 5.7.18-log
-- PHP Version: 7.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db941227`
--
CREATE DATABASE IF NOT EXISTS `db941227` DEFAULT CHARACTER SET utf8 COLLATE utf8_swedish_ci;
USE `db941227`;

-- --------------------------------------------------------

--
-- Table structure for table `Admin`
--

CREATE TABLE `Admin` (
  `ID` int(11) NOT NULL,
  `Email` text COLLATE utf8_swedish_ci NOT NULL,
  `DateOfAdmin` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `Admin`
--

INSERT INTO `Admin` (`ID`, `Email`, `DateOfAdmin`) VALUES
(1, 'A@A.A', '2020-11-25 22:02:19'),
(10, 'NOUR.BAHTITE@GMAIL.COM', '2020-11-26 11:39:43'),
(11, 'b@b.b', '2020-11-26 11:53:05');

-- --------------------------------------------------------

--
-- Table structure for table `Cart`
--

CREATE TABLE `Cart` (
  `CartID` int(11) NOT NULL,
  `UserID` int(11) NOT NULL,
  `ProductsID` int(11) NOT NULL,
  `Amount` int(11) NOT NULL,
  `Date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Categorys`
--

CREATE TABLE `Categorys` (
  `CategoryID` int(11) NOT NULL,
  `CategoryName` varchar(255) COLLATE utf8_swedish_ci NOT NULL,
  `Image` varchar(255) COLLATE utf8_swedish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `Categorys`
--

INSERT INTO `Categorys` (`CategoryID`, `CategoryName`, `Image`) VALUES
(1, 'Mössa', 'mossa.jpg'),
(2, 'Tröja', 'tsh.jpg'),
(3, 'Bälte', 'balte.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `OrderDetails`
--

CREATE TABLE `OrderDetails` (
  `OrderDetailsID` int(11) NOT NULL,
  `OrderID` int(11) NOT NULL,
  `ProductID` int(11) NOT NULL,
  `BuyingPrice` int(11) NOT NULL,
  `Amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `OrderDetails`
--

INSERT INTO `OrderDetails` (`OrderDetailsID`, `OrderID`, `ProductID`, `BuyingPrice`, `Amount`) VALUES
(94, 86, 3, 200, 1),
(95, 86, 3, 200, 1),
(96, 86, 3, 200, 1),
(97, 86, 3, 200, 1),
(100, 88, 3, 200, 1),
(109, 94, 3, 200, 1),
(115, 97, 3, 200, 1),
(116, 97, 3, 200, 1),
(120, 100, 7, 10, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Orders`
--

CREATE TABLE `Orders` (
  `OrderID` int(11) NOT NULL,
  `UserID` int(11) NOT NULL,
  `Amount` int(11) NOT NULL,
  `OrderStatus` text COLLATE utf8_swedish_ci NOT NULL,
  `FirstName` varchar(255) COLLATE utf8_swedish_ci NOT NULL,
  `LastName` varchar(255) COLLATE utf8_swedish_ci NOT NULL,
  `ShippingAdress` text COLLATE utf8_swedish_ci NOT NULL,
  `OrderPhoneNumber` int(30) NOT NULL,
  `OrderEmail` char(255) COLLATE utf8_swedish_ci NOT NULL,
  `DataOfOrder` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `Orders`
--

INSERT INTO `Orders` (`OrderID`, `UserID`, `Amount`, `OrderStatus`, `FirstName`, `LastName`, `ShippingAdress`, `OrderPhoneNumber`, `OrderEmail`, `DataOfOrder`) VALUES
(86, 45, 800, 'Processing Order', 'nour', 'bahtite', 'My place', 707181110, 'NOUR.BAHTITE@GMAIL.COM', '2020-12-14 00:19:10'),
(88, 45, 200, 'Processing Order', 'nour', 'bahtite', 'My place', 707181110, 'NOUR.BAHTITE@GMAIL.COM', '2020-12-14 00:23:57'),
(94, 45, 225, 'Processing Order', 'nour', 'bahtite', 'My place', 707181110, 'NOUR.BAHTITE@GMAIL.COM', '2020-12-14 00:34:02'),
(97, 45, 425, 'Processing Order', 'nour', 'bahtite', 'My place', 707181110, 'NOUR.BAHTITE@GMAIL.COM', '2020-12-14 01:15:55'),
(100, 46, 35, 'Processing Order', 'tjenis', 'a', '', 1234567890, 'A@A.A', '2020-12-14 01:41:39');

-- --------------------------------------------------------

--
-- Table structure for table `Products`
--

CREATE TABLE `Products` (
  `ProductID` int(11) NOT NULL,
  `ProductName` char(255) COLLATE utf8_swedish_ci NOT NULL,
  `ProductPrice` int(11) NOT NULL,
  `NumberInStock` int(11) NOT NULL,
  `Description` text COLLATE utf8_swedish_ci NOT NULL,
  `Rating` tinyint(4) DEFAULT '0',
  `imageName` char(255) COLLATE utf8_swedish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `Products`
--

INSERT INTO `Products` (`ProductID`, `ProductName`, `ProductPrice`, `NumberInStock`, `Description`, `Rating`, `imageName`) VALUES
(2, 'Röd Gucci Tröja', 200, 0, 'En otroligt fin röd tröja. Mycket värd pengarna.', 3, 'tsh.jpg'),
(3, 'Gul Kebab', 200, 9990, 'Jätte god kebab. Gjord från Noors händer.', 2, 'tsh.jpg'),
(4, 'Bil', 30, 0, 'En bil till salu', 5, 'tsh.jpg'),
(5, 'Data', 100, 5, 'GTX 3070. Wow!', 4, 'tsh.jpg'),
(6, 'Penna', 5, 500, 'En penna. Bra att skriva ner saker med.', 1, 'tsh.jpg'),
(7, 'En jätte fin tonfisk', 10, 999, 'Jätte god tonfisk som går att äta på dagarna', 4, 'tsh.jpg'),
(10, 'test', 10, 0, '1\r\n', 1, 'tsh.jpg'),
(11, '1', 1, 1, '1', 0, 'tsh.jpg'),
(12, 'New item', 50, 20, 'Fin ', 0, 'tsh.jpg'),
(13, 'abirbi', 10, 20, 'bla bla bla', 0, 'tsh.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `ProductsCategory`
--

CREATE TABLE `ProductsCategory` (
  `ID` int(11) NOT NULL,
  `ProductID` int(11) NOT NULL,
  `CategoryID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `ProductsCategory`
--

INSERT INTO `ProductsCategory` (`ID`, `ProductID`, `CategoryID`) VALUES
(1, 5, 1),
(2, 2, 2),
(4, 2, 1),
(5, 4, 1),
(6, 2, 2),
(7, 2, 2),
(8, 3, 2),
(9, 5, 2),
(10, 5, 2),
(11, 4, 2),
(12, 3, 1),
(13, 6, 1),
(14, 13, 3);

-- --------------------------------------------------------

--
-- Table structure for table `UserReviews`
--

CREATE TABLE `UserReviews` (
  `ReviewID` int(11) NOT NULL,
  `UserID` int(11) NOT NULL,
  `ProductID` int(11) NOT NULL,
  `Review` text COLLATE utf8_swedish_ci NOT NULL,
  `Rating` tinyint(4) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `UserReviews`
--

INSERT INTO `UserReviews` (`ReviewID`, `UserID`, `ProductID`, `Review`, `Rating`, `time`) VALUES
(30, 45, 2, '', 3, '2020-12-13 23:31:44'),
(31, 45, 4, 'Bra bil', 5, '2020-12-14 00:34:45'),
(32, 46, 4, 'noor jag älskar dig <3', 1, '2020-12-14 00:44:30'),
(33, 52, 4, 'Haha', 1, '2020-12-14 00:47:24'),
(34, 46, 7, 'ganska gott', 4, '2020-12-14 01:40:17');

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `UserID` int(11) NOT NULL,
  `FirstName` char(255) COLLATE utf8_swedish_ci NOT NULL,
  `LastName` char(255) COLLATE utf8_swedish_ci NOT NULL,
  `PhoneNumber` char(30) COLLATE utf8_swedish_ci NOT NULL,
  `Email` char(255) COLLATE utf8_swedish_ci NOT NULL,
  `Password` text COLLATE utf8_swedish_ci NOT NULL,
  `Adress` text COLLATE utf8_swedish_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`UserID`, `FirstName`, `LastName`, `PhoneNumber`, `Email`, `Password`, `Adress`) VALUES
(45, 'nour', 'bahtite', '0707181110', 'NOUR.BAHTITE@GMAIL.COM', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', 'My place'),
(46, 'tjenis', 'a', 'a', 'A@A.A', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', ''),
(48, 'b', 'b', 'b', 'B@B.B', '3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d', ''),
(49, 'Nour', 'Bahtite', '+46707181110', 'S@S.S', '043a718774c572bd8a25adbeb1bfcd5c0256ae11cecf9f9c3f925d0e52beaf89', ''),
(50, 'Nour', 'Bahtite', '+46707181110', 'NOUR@GMAIL.COM', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', ''),
(51, 'Nour', 'Bahtite', '+46707181110', 'L@L.L', 'acac86c0e609ca906f632b0e2dacccb2b77d22b0621f20ebece1a4835b93f6f0', 'assssssss'),
(52, '1', '1', '1', '5@5.5', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', NULL),
(53, 'tony', 'tonfisk', '12345678', 'TONY@FISK.COM', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', NULL),
(54, 'Nour', 'Bahtite', '+46707181110', 'D@D.D', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', NULL),
(55, '1', '1', '0734993498', '1@1.1', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Admin`
--
ALTER TABLE `Admin`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `Cart`
--
ALTER TABLE `Cart`
  ADD PRIMARY KEY (`CartID`),
  ADD KEY `UserID` (`UserID`),
  ADD KEY `ProductsID` (`ProductsID`);

--
-- Indexes for table `Categorys`
--
ALTER TABLE `Categorys`
  ADD PRIMARY KEY (`CategoryID`);

--
-- Indexes for table `OrderDetails`
--
ALTER TABLE `OrderDetails`
  ADD PRIMARY KEY (`OrderDetailsID`),
  ADD KEY `OrderID` (`OrderID`),
  ADD KEY `ProductID` (`ProductID`);

--
-- Indexes for table `Orders`
--
ALTER TABLE `Orders`
  ADD PRIMARY KEY (`OrderID`),
  ADD KEY `UserID` (`UserID`),
  ADD KEY `OrderEmail` (`OrderEmail`);

--
-- Indexes for table `Products`
--
ALTER TABLE `Products`
  ADD PRIMARY KEY (`ProductID`);

--
-- Indexes for table `ProductsCategory`
--
ALTER TABLE `ProductsCategory`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ProductsID` (`ProductID`),
  ADD KEY `CategoryID` (`CategoryID`);

--
-- Indexes for table `UserReviews`
--
ALTER TABLE `UserReviews`
  ADD PRIMARY KEY (`ReviewID`),
  ADD KEY `ProductID` (`ProductID`),
  ADD KEY `UserID` (`UserID`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`UserID`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Admin`
--
ALTER TABLE `Admin`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT for table `Cart`
--
ALTER TABLE `Cart`
  MODIFY `CartID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=334;
--
-- AUTO_INCREMENT for table `Categorys`
--
ALTER TABLE `Categorys`
  MODIFY `CategoryID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `OrderDetails`
--
ALTER TABLE `OrderDetails`
  MODIFY `OrderDetailsID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121;
--
-- AUTO_INCREMENT for table `Orders`
--
ALTER TABLE `Orders`
  MODIFY `OrderID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;
--
-- AUTO_INCREMENT for table `Products`
--
ALTER TABLE `Products`
  MODIFY `ProductID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT for table `ProductsCategory`
--
ALTER TABLE `ProductsCategory`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT for table `UserReviews`
--
ALTER TABLE `UserReviews`
  MODIFY `ReviewID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `UserID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `Cart`
--
ALTER TABLE `Cart`
  ADD CONSTRAINT `Cart_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `Users` (`UserID`) ON DELETE CASCADE,
  ADD CONSTRAINT `Cart_ibfk_2` FOREIGN KEY (`ProductsID`) REFERENCES `Products` (`ProductID`) ON DELETE CASCADE;

--
-- Constraints for table `OrderDetails`
--
ALTER TABLE `OrderDetails`
  ADD CONSTRAINT `OrderDetails_ibfk_1` FOREIGN KEY (`OrderID`) REFERENCES `Orders` (`OrderID`),
  ADD CONSTRAINT `OrderDetails_ibfk_2` FOREIGN KEY (`ProductID`) REFERENCES `Products` (`ProductID`);

--
-- Constraints for table `Orders`
--
ALTER TABLE `Orders`
  ADD CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `Users` (`UserID`);

--
-- Constraints for table `ProductsCategory`
--
ALTER TABLE `ProductsCategory`
  ADD CONSTRAINT `ProductsCategory_ibfk_1` FOREIGN KEY (`ProductID`) REFERENCES `Products` (`ProductID`),
  ADD CONSTRAINT `ProductsCategory_ibfk_2` FOREIGN KEY (`CategoryID`) REFERENCES `Categorys` (`CategoryID`);

--
-- Constraints for table `UserReviews`
--
ALTER TABLE `UserReviews`
  ADD CONSTRAINT `UserReviews_ibfk_1` FOREIGN KEY (`ProductID`) REFERENCES `Products` (`ProductID`) ON DELETE CASCADE,
  ADD CONSTRAINT `UserReviews_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `Users` (`UserID`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
