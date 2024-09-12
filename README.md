# Scraping-SSCASN

![Git Badge](https://img.shields.io/badge/GIT-black?style=for-the-badge&logo=GIT&logoColor=F05032)
![Python Badge](https://img.shields.io/badge/PYTHON-black?style=for-the-badge&logo=python&logoColor=gold)

## Overview

This project scrapes public data on government job positions from the SSCASN portal, using the SSCASN API. It collects detailed information on job formations, such as institution names, job titles, unit locations, required qualifications, and salary ranges, and stores them in an Excel file for easy access.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Code Structure](#code-structure)
- [Error Handling](#error-handling)
- [Customization](#customization)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Features

- Scrapes data from the SSCASN API for specific educational qualifications and job procurement codes.
- Handles data pagination and compiles results into an Excel workbook.
- Provides comprehensive job formation details such as institution name, job position, unit, number of positions available, and salary information.
- Saves the output as an Excel file with a timestamped filename.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ms3welz/Scraping-SSCASN.git
   cd Scraping-SSCASN
   ```

2. Manually install the required Python packages:

   ```bash
   pip install requests
   pip install openpyxl
   ```

   - `requests` : Handles HTTP requests to interact with the SSCASN API.
   - `openpyxl` : For creating and writing data into Excel files.

## Usage

To run the sscasn, use the following command:

```bash
python sscasn.py
```

### Output

The script creates an Excel file with the following columns:

- **Nama Instansi**: The name of the institution offering the job.
- **Formasi**: The specific job formation.
- **Jabatan**: The job position title.
- **Unit Kerja**: The work unit or department.
- **Jumlah Kebutuhan**: Number of job positions available.
- **Gaji Min**: Minimum salary offered for the position.
- **Gaji Max**: Maximum salary offered for the position.
- **Link**: A direct link to the job details.

The Excel file is saved as `data-<kode_pendidikan>-<timestamp>.xlsx`, for example: `data-5101087-20240912-150523.xlsx`.

## Code Structure

- `sscasn.py`: Main script that coordinates the entire scraping process.
  - `create_headers()`: Defines headers required for SSCASN API requests.
  - `get_data()`: Fetches paginated data from the API.
  - `create_excel_workbook()`: Sets up the Excel workbook.
  - `process_and_write_data()`: Processes the API response and writes data into the Excel workbook.
  - `save_workbook()`: Saves the Excel workbook to disk with a timestamped filename.
  - `main()`: The main entry point of the script.

## Error Handling

- **API Request Failures**: If an API request fails, an error message is logged, and the process continues.
- **Empty Data Handling**: If no data is available, the script will log a message and skip processing.

## Customization

To scrape data for different qualifications or procurement types, modify the `kode_pendidikan` and `kode_pengadaan` values in the `main()` function:

```python
kode_pendidikan = '5101087'  # Example for S1-Teknik Informatika
kode_pengadaan = '2'  # Example for CPNS procurement
```

These can be adjusted based on your requirements.

## Future Enhancements

- **Multithreading**: Improve performance by adding multithreading to handle large datasets more efficiently.
- **Additional Filters**: Add options to filter data based on specific parameters like location, salary range, etc.
- **Database Support**: Store data directly into a database for further analysis.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute with proper attribution.
