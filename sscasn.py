import requests
import time
from openpyxl import Workbook

def create_headers():
    """Create the headers for the HTTP request."""
    return {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'api-sscasn.bkn.go.id',
        'Origin': 'https://sscasn.bkn.go.id',
        'Pragma': 'no-cache',
        'Referer': 'https://sscasn.bkn.go.id/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }

def get_data(offset, kode_ref_pend, pengadaan_kd):
    """Fetch data from the API."""
    headers = create_headers()
    url = f'https://api-sscasn.bkn.go.id/2024/portal/spf?kode_ref_pend={kode_ref_pend}&pengadaan_kd={pengadaan_kd}&offset={offset}'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def create_excel_workbook():
    """Create an Excel workbook and return the active sheet."""
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "DATA SSCASN"
    sheet.append(['Nama Instansi', 'Formasi', 'Jabatan', 'Unit Kerja', 'Jumlah Kebutuhan', 'Gaji Min', 'Gaji Max', "Link"])
    return workbook, sheet

def save_workbook(workbook, kode_pendidikan):
    """Save the workbook to a file with a timestamp."""
    timestamp = time.strftime('%Y%m%d-%H%M%S')
    filename = f'data-{kode_pendidikan}-{timestamp}.xlsx'
    workbook.save(filename)
    print(f'Workbook saved as {filename}')

def process_and_write_data(sheet, data):
    """Process the API data and write it to the Excel sheet."""
    if data and 'data' in data and 'data' in data['data']:
        for item in data['data']['data']:
            formasi = f"{item['jp_nama']} {item['formasi_nm']}"
            institusi = item['ins_nm'].replace(',', '-')
            sheet.append([
                institusi,
                formasi,
                item['jabatan_nm'],
                item['lokasi_nm'],
                str(item['jumlah_formasi']),
                item['gaji_min'],
                item['gaji_max'],
                f'https://sscasn.bkn.go.id/detailformasi/{item["formasi_id"]}'
            ])
    else:
        print("No data to process")

def main():
    kode_pendidikan = '5101087' # S1-Teknik Informatika (5101087)
    kode_pengadaan = '2'

    workbook, sheet = create_excel_workbook()

    initial_data = get_data(0, kode_pendidikan, kode_pengadaan)
    if not initial_data:
        return

    total_data = initial_data['data']['meta']['total']
    for i in range(0, int(total_data), 10):
        data = get_data(i, kode_pendidikan, kode_pengadaan)
        if data:
            process_and_write_data(sheet, data)
        else:
            print(f"Failed to fetch data for offset {i}")

    save_workbook(workbook, kode_pendidikan)

if __name__ == '__main__':
    main()
