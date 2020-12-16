-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 16, 2020 at 08:35 PM
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
(1, 'Hat', 'mossa.jpg'),
(2, 'T-shirt', 'tsh.jpg'),
(3, 'Watch', 'Watch.jpg');

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
(142, 117, 14, 150, 1),
(143, 117, 14, 150, 1),
(144, 118, 16, 300, 1),
(145, 119, 16, 300, 1),
(146, 119, 16, 300, 1),
(147, 119, 16, 300, 1),
(148, 119, 16, 300, 1),
(149, 119, 16, 300, 1),
(150, 119, 16, 300, 1),
(151, 119, 16, 300, 1),
(152, 119, 16, 300, 1),
(153, 119, 16, 300, 1),
(154, 119, 16, 300, 1);

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
(117, 45, 325, 'Canceled', 'nour', 'bahtite', 'test', 707181110, 'NOUR.BAHTITE@GMAIL.COM', '2020-12-16 16:54:23'),
(118, 46, 325, 'Processing Order', 'tjenis', 'a', 'luleeee', 1234567890, 'A@A.A', '2020-12-16 19:01:20'),
(119, 45, 3025, 'Processing Order', 'nour', 'bahtite', 'test', 707181110, 'NOUR.BAHTITE@GMAIL.COM', '2020-12-16 19:19:15');

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
(14, 'CURREN', 150, 100, 'Dial shape: Round\r\nMovement type: Quartz \r\nDisplay type: Pointer \r\nDial color: As in images', 4, 'cf508a4902f6d34e304c7b8ced614776.jpg'),
(15, 'MiGEER', 100, 100, 'Dial shape: Round\r\nMovement type: Quartz \r\nDisplay type: Pointer \r\nDial color: As in images', 2, 'product-image-74862151.jpg'),
(16, 'CITIZEN', 300, 89, 'Eco-Drive 200m', 0, 'watch-man-citizen-diver-eco-drive-200m-steel-black-dial-bn0190-82e.jpg'),
(17, 'RED', 20, 100, 'Warm and soft hat', 1, '91291359_cw_front.jpg'),
(18, 'Green hat', 20, 100, 'Warm and soft', 0, 'beanie_classic_forest_green.jpg'),
(19, 'Gray hat', 20, 100, 'Warm', 0, '666a-157078802986.jpg'),
(20, 'lilac T-shirt', 10, 100, 'lilac ', 0, '1.jpg'),
(21, 'lilac T-shirt', 10, 100, 'lilac ', 0, 'maglietta-colours-purple.jpg'),
(22, 'Red T-shirt', 20, 100, 'Red', 0, 'roed-t-shirt-med-eget-tryck.jpg'),
(23, 'Black T-shirt', 10, 100, 'Black', 0, 'tshirt-herr-unisex-vit.jpg'),
(24, 'T-shirt', 10, 0, 'orang', 0, '2X351501F.25PQ_1_SPR20_461508v2.jpg'),
(25, 'whiteT-shirt', 20, 0, 'white', 0, '15421803_1200_A.jpg');

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
(18, 14, 3),
(19, 15, 3),
(20, 16, 3),
(21, 17, 1),
(22, 18, 1),
(23, 19, 1),
(24, 20, 2),
(25, 21, 2),
(26, 22, 2),
(27, 23, 2),
(28, 24, 2),
(29, 25, 2);

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
(41, 46, 15, '', 2, '2020-12-16 17:30:05'),
(42, 46, 17, '', 1, '2020-12-16 17:31:40');

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
(45, 'nour', 'bahtite', '0707181110', 'NOUR.BAHTITE@GMAIL.COM', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', 'test'),
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
  MODIFY `CartID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=389;
--
-- AUTO_INCREMENT for table `Categorys`
--
ALTER TABLE `Categorys`
  MODIFY `CategoryID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `OrderDetails`
--
ALTER TABLE `OrderDetails`
  MODIFY `OrderDetailsID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=155;
--
-- AUTO_INCREMENT for table `Orders`
--
ALTER TABLE `Orders`
  MODIFY `OrderID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=120;
--
-- AUTO_INCREMENT for table `Products`
--
ALTER TABLE `Products`
  MODIFY `ProductID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
--
-- AUTO_INCREMENT for table `ProductsCategory`
--
ALTER TABLE `ProductsCategory`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
--
-- AUTO_INCREMENT for table `UserReviews`
--
ALTER TABLE `UserReviews`
  MODIFY `ReviewID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;
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
  ADD CONSTRAINT `OrderDetails_ibfk_1` FOREIGN KEY (`OrderID`) REFERENCES `Orders` (`OrderID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `OrderDetails_ibfk_2` FOREIGN KEY (`ProductID`) REFERENCES `Products` (`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Orders`
--
ALTER TABLE `Orders`
  ADD CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `Users` (`UserID`);

--
-- Constraints for table `ProductsCategory`
--
ALTER TABLE `ProductsCategory`
  ADD CONSTRAINT `ProductsCategory_ibfk_1` FOREIGN KEY (`ProductID`) REFERENCES `Products` (`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ProductsCategory_ibfk_2` FOREIGN KEY (`CategoryID`) REFERENCES `Categorys` (`CategoryID`) ON DELETE CASCADE ON UPDATE CASCADE;

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
