-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 06 Jan 2024 pada 04.21
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `obat`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `dbobat`
--

CREATE TABLE `dbobat` (
  `id` int(11) NOT NULL,
  `kdobat` varchar(10) DEFAULT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `berat` varchar(10) DEFAULT NULL,
  `bentuk` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `dbobat`
--

INSERT INTO `dbobat` (`id`, `kdobat`, `nama`, `berat`, `bentuk`) VALUES
(1, '001', 'promaag', '20mg', 'tablet'),
(2, '002', 'Lansoprazole', '15mg', 'kapsul'),
(3, '003', 'Bisolvon', '60ml', 'Flash'),
(4, '004', 'Paracetamol', '25mg', 'tablet');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `dbobat`
--
ALTER TABLE `dbobat`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kdobat` (`kdobat`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `dbobat`
--
ALTER TABLE `dbobat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
